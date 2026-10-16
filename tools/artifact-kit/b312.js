const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}
Lib.stepper($("#st0"), { w: 760, h: 380, label: "How commercial banks create value", base: { n: 0 }, draw: mkChain(["Savers deposit money in the bank", "The bank lends to borrowers at a higher interest rate", "Borrowers invest or spend the loan", "The bank earns the interest gap", "Savings are turned into investment"], "--accent"), steps: chainSteps(["Savers deposit money in the bank", "The bank lends to borrowers at a higher interest rate", "Borrowers invest or spend the loan", "The bank earns the interest gap", "Savings are turned into investment"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Lender of last resort", base: { n: 0 }, draw: mkChain(["A commercial bank faces a sudden run on deposits", "It cannot meet withdrawals at once", "The central bank lends it emergency funds", "Confidence is restored", "The banking system stays stable"], "--bad"), steps: chainSteps(["A commercial bank faces a sudden run on deposits", "It cannot meet withdrawals at once", "The central bank lends it emergency funds", "Confidence is restored", "The banking system stays stable"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const loans = v[0] * v[1] / 100, earned = loans * v[2] / 100, paid = v[0] * v[3] / 100, prof = earned - paid; return { r: ['$' + earned.toFixed(1) + 'm', '$' + paid.toFixed(1) + 'm', (prof >= 0 ? '+' : '−') + '$' + Math.abs(prof).toFixed(1) + 'm'], t: 'Of $' + v[0] + 'm deposits the bank lends $' + loans.toFixed(0) + 'm at ' + v[2] + '%, earning $' + earned.toFixed(1) + 'm, and pays savers ' + v[3] + '% on deposits: $' + paid.toFixed(1) + 'm. The gap is $' + prof.toFixed(1) + 'm before running costs. Lending out less, or a smaller gap between rates, reduces profit.', bars: [['Interest earned', earned, '--good'], ['Interest paid', paid, '--warn'], ['Profit', Math.max(0, prof), '--accent']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Deposits ($m)", min: 100, max: 1000, step: 100, value: 500, fmt: (v) => '$' + v + 'm', onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Share lent out (%)", min: 30, max: 95, step: 5, value: 80, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Interest rate on loans (%)", min: 2, max: 15, step: 1, value: 8, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Interest rate on deposits (%)", min: 0, max: 8, step: 1, value: 2, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "Taking deposits from households", "a": "Commercial bank", "b": "Provides safe saving."}, {"n": "Lending money for a mortgage", "a": "Commercial bank", "b": "A loan to a customer."}, {"n": "Setting the key interest rate", "a": "Central bank", "b": "Monetary policy."}, {"n": "Printing banknotes", "a": "Central bank", "b": "Issues legal tender."}, {"n": "Lending in an emergency to a failing bank", "a": "Central bank", "b": "Lender of last resort."}, {"n": "Offering a current account and cards", "a": "Commercial bank", "b": "Payment services."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Done by</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each done by a <b>central bank</b> or a <b>commercial bank</b>?", buckets: [{"label": "Central bank"}, {"label": "Commercial bank"}], items: [{"text": "Sets interest rates", "b": 0}, {"text": "Issues banknotes", "b": 0}, {"text": "Lender of last resort", "b": 0}, {"text": "Offers savings accounts", "b": 1}, {"text": "Makes loans to firms", "b": 1}, {"text": "Provides debit cards", "b": 1}], done: "Know the two roles." });
Lib.classify($("#cl2"), { prompt: "Which <b>commercial bank service</b> is each?", buckets: [{"label": "Deposits"}, {"label": "Loans"}, {"label": "Payments"}], items: [{"text": "A savings account", "b": 0}, {"text": "A mortgage", "b": 1}, {"text": "A bank transfer", "b": 2}, {"text": "An overdraft", "b": 1}, {"text": "A current account", "b": 0}, {"text": "A contactless card", "b": 2}], done: "Bank services." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Commercial bank", "A bank that takes deposits and makes loans"], ["Central bank", "The government's bank and banking regulator"], ["Lender of last resort", "Lends to banks in a crisis"], ["Monetary policy", "Using interest rates and the money supply"], ["Deposit", "Money placed with a bank by a saver"], ["Overdraft", "Borrowing beyond a bank balance"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a central bank acts as lender of last resort</b>.", items: ["Depositors lose confidence in a bank", "Many withdraw their money at once", "The bank cannot pay them all", "The central bank lends it emergency funds", "Confidence returns and the system stabilises"], done: "Preventing a banking collapse." });
Lib.calc($("#c1"), { qs: [
  { q: "A bank lends $80m at 10% and pays 3% on $100m of deposits. What is the profit before costs ($m)?", a: 5, sol: "Earns 8m, pays 3m: <b>$5m</b>." },
  { q: "Deposits are $200m and the bank lends 75%. How much is lent ($m)?", a: 150, sol: "75% × 200 = <b>$150m</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A function of the central bank is to:", opts: ["Take deposits from households", "Set interest rates", "Sell insurance", "Run supermarkets"], a: 1, why: "Monetary policy." },
  { q: "Commercial banks earn profit from:", opts: ["Taxes", "The gap between interest rates", "Printing money", "Selling goods"], a: 1, why: "Lend high, pay low." },
  { q: "The lender of last resort is:", opts: ["A commercial bank", "The central bank", "A household", "A firm"], a: 1, why: "In a crisis." },
  { q: "Which is a commercial bank service?", opts: ["Printing notes", "Accepting deposits", "Setting policy", "Controlling inflation"], a: 1, why: "Savings." },
  { q: "The central bank is the government's:", opts: ["Customer", "Bank", "Competitor", "Regulator only"], a: 1, why: "Holds accounts." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Central bank", "The government's bank; controls interest rates and the money supply."],
  ["Commercial bank", "A bank that takes deposits and lends to households and firms."],
  ["Lender of last resort", "The central bank lending to banks in a crisis."],
  ["Deposit", "Money placed in a bank."],
  ["Loan", "Money borrowed, repaid with interest."],
  ["Overdraft", "Borrowing beyond the account balance."],
  ["Monetary policy", "Interest rates and money supply management."],
  ["Regulation", "Rules to keep banks safe."],
  ["Interest rate", "The price of borrowing or reward for saving."],
] });
labA(); 
