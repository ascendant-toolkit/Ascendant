const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 100, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 50, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, "camera image", k >= 0) + B(130, "face found?", k >= 1) + B(250, "measure", k >= 2) + B(370, "compare", k >= 3) + B(490, "match: 96%", k >= 4); for (let i = 0; i < 4; i++) o += SV.path(`M${110 + i * 120},62 H${130 + i * 120}`, "ax"); return o; };
  Lib.stepper($("#stA"), { w: 610, h: 110, label: "Facial recognition", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The camera captures an image.", "Image recognition finds that there is a face.", "The distances between facial features are measured.", "They are compared with the values in the database.", "The system gives a probability of a match."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const n = [0, 6, 24, 60][k]; let o = SV.text(20, 20, "training images: " + n, "lbl bd"); for (let i = 0; i < 60; i++) o += SV.rect(20 + (i % 20) * 24, 30 + Math.floor(i / 20) * 24, 20, 20, i < n ? "f1" : "cell", { rx: 3 }); o += SV.text(20, 125, ["", "few examples: rarely right", "more examples: right more often", "a large amount of data: the AI learns the patterns well"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 140, label: "Training", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["An AI starts with no examples.", "Trained on a few images: it often gets it wrong.", "With more images: it improves.", "Trained on a large number of images it learns the patterns."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const mv = [["now", "start"], ["move A", "score 3"], ["move B", "score 7"], ["move C", "score 5"], ["choose", "move B"]][k]; let o = SV.rect(20, 40, 100, 40, "f3", { rx: 8 }) + SV.text(70, 65, "position", "lbl bd", { "text-anchor": "middle" });
    [["A", 3], ["B", 7], ["C", 5]].forEach(([n, v], i) => { if (i < k) o += SV.path(`M120,60 L220,${35 + i * 40}`, "ax") + SV.rect(220, 20 + i * 40, 120, 30, v === 7 && k === 4 ? "f1" : "cell", { rx: 6 }) + SV.text(280, 40 + i * 40, "move " + n + ": " + v, "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(380, 70, k === 4 ? "picks the best" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 150, label: "Game AI", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The AI looks at the current position.", "It looks ahead at move A: a low score.", "Move B scores higher.", "Move C is middle.", "It chooses the move most likely to be successful."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let th = 80; const same = [96, 91, 88, 74, 99, 85], other = [32, 55, 61, 78, 45, 69]; const paint = () => { const fn = same.filter((v) => v < th).length, fp = other.filter((v) => v >= th).length;
    let o = '<svg viewBox="0 0 420 100" style="width:420px;max-width:100%;display:block"><path d="M20,70 H400" class="ax"/>'; same.forEach((v, i) => o += `<circle cx="${20 + v * 3.7}" cy="${50 - (i % 2) * 14}" r="6" fill="var(--good)"/>`); other.forEach((v, i) => o += `<circle cx="${20 + v * 3.7}" cy="${52 - (i % 2) * 14}" r="6" fill="var(--bad)"/>`); o += `<line x1="${20 + th * 3.7}" y1="10" x2="${20 + th * 3.7}" y2="80" stroke="var(--accent)" stroke-width="2"/><text x="20" y="95" class="sm" style="font-size:11px">probability of match (%)</text></svg>`; $("#tG").innerHTML = o;
    $("#tV").innerHTML = `Access is allowed when the match probability is at least <b>${th}%</b>. Green = the real owner, red = other people. With this threshold <b>${fn}</b> owner scan(s) are wrongly refused and <b>${fp}</b> other person scan(s) are wrongly accepted. A high threshold is safer but refuses the owner more often: AI works with probabilities, so mistakes happen.`; };
  Lib.slider($("#tS"), { id: "t1", label: "Threshold (%) ", min: 30, max: 100, value: th, fmt: (x) => x, onInput: (v) => { th = v; paint(); } }); paint();
})();
btnTable("aB", "aO", [
  ["Unlocking a phone with your face", "Image (facial) recognition", "Compares facial features with stored values"],
  ["Asking a speaker to play music", "Speech recognition + language processing", "Words matched to a command"],
  ["Reading a car's number plate", "Optical character recognition", "Pixels to characters"],
  ["A computer opponent in chess", "Game-playing AI", "Looks ahead, learns from mistakes"],
  ["A car that stays in its lane", "Self-driving AI", "Detects position and avoids collisions"]
], ["Situation", "AI technique", "Key idea"]);
btnTable("iB", "iO", [
  ["Helps visually impaired people choose products", "Social (positive)", "Accessibility"],
  ["Faster fault diagnosis saves a garage money", "Economic (positive)", "Lower costs, higher profit"],
  ["Constant classroom monitoring raises stress", "Ethical (negative)", "Surveillance and wellbeing"],
  ["An AI program is expensive to buy and update", "Economic (negative)", "Reduces profit margins"],
  ["Wrong recognition denies someone access", "Social (negative)", "Mistakes affect people"]
], ["Impact", "Type", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which AI technique does the description use?", buckets: [{"label": "Image recognition"}, {"label": "Speech recognition"}, {"label": "Game-playing AI"}], items: [{"text": "Compares the pixels of a camera image with stored features", "b": 0}, {"text": "Matches spoken words to a database of words", "b": 1}, {"text": "Looks ahead at possible moves and picks the most likely to win", "b": 2}, {"text": "Identifies a face from the distance between features", "b": 0}, {"text": "Turns key phrases heard into a command", "b": 1}, {"text": "Learns from previous mistakes by changing future choices", "b": 2}], done: "Match the technique." });
Lib.classify($("#cl2"), { prompt: "Is it a positive or a negative impact of AI?", buckets: [{"label": "Positive"}, {"label": "Negative"}], items: [{"text": "Helps visually impaired people choose products", "b": 0}, {"text": "Constant surveillance causes privacy concerns", "b": 1}, {"text": "Faster fault diagnosis lowers costs for a garage", "b": 0}, {"text": "Incorrect recognition denies someone access", "b": 1}, {"text": "Personalised support for struggling students", "b": 0}, {"text": "A wrong AI answer gives misinformation", "b": 1}], done: "Helps: positive. Harms: negative." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Image recognition", "Compares pixels with stored features"], ["Speech recognition", "Matches spoken words to a database"], ["Natural language processing", "Works out the meaning of a sentence"], ["Training", "Learning from a large amount of data"], ["Probability of a match", "How likely it is that the image is the person"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put facial recognition in order.", items: ["The camera captures an image", "Image recognition identifies that there is a face", "The distances between facial features are measured", "The values are compared with those in the database", "Access is allowed if the probability of a match is high enough"], done: "Capture, find face, measure, compare, decide." });
Lib.calc($("#c1"), { qs: [
  {"q": "A system compares a face with 1000 stored faces. How many comparisons for one face?", "a": 1000, "unit": "", "tol": 0.01, "hint": "One per stored face.", "sol": "<b>1000</b>."},
  {"q": "A face scanner is right 98% of the time. How many errors in 500 scans?", "a": 10, "unit": "", "tol": 0.01, "hint": "2% of 500.", "sol": "<b>10</b>."},
  {"q": "A garage saves 20 minutes on each of 6 diagnoses a day. How many hours saved per day?", "a": 2, "unit": "h", "tol": 0.01, "hint": "120 minutes.", "sol": "<b>2</b> hours."},
  {"q": "A chess AI looks 3 moves ahead with 10 choices each move. How many move sequences?", "a": 1000, "unit": "", "tol": 0.01, "hint": "10^3.", "sol": "<b>1000</b>."},
  {"q": "An AI trained on 40 000 images uses 80% for training. How many images for training?", "a": 32000, "unit": "", "tol": 0.5, "hint": "0.8 × 40 000.", "sol": "<b>32 000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Facial recognition compares:", opts: ["Facial features with a database", "The phone battery", "Only passwords", "Colours of the room"], a: 0, why: "Features and database." },
  { q: "Speech recognition:", opts: ["Matches words to a database", "Compresses audio", "Prints text only", "Needs no data"], a: 0, why: "Matches words." },
  { q: "A game AI improves by:", opts: ["Learning from past mistakes", "Using a new screen", "Ignoring the rules", "Copying files"], a: 0, why: "Learns." },
  { q: "A negative social impact of AI:", opts: ["Privacy concerns from surveillance", "Faster diagnosis", "Lower costs", "Better translation"], a: 0, why: "Privacy." },
  { q: "An economic impact of AI:", opts: ["Lower costs for a business", "More colourful screens", "Quieter fans", "Bigger buttons"], a: 0, why: "Costs." },
  { q: "OCR is used to:", opts: ["Convert pixels into characters", "Encrypt data", "Record video", "Count users"], a: 0, why: "Pixels to characters." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AI", "Computer performing tasks needing human intelligence."],
  ["Image recognition", "Pixels to features; compare with database."],
  ["Speech recognition", "Words matched to a database."],
  ["OCR", "Pixels to characters."],
  ["Training", "Learning from large amounts of data."],
  ["Social impact", "Privacy, safety, accessibility."],
  ["Economic impact", "Costs, profits, jobs."],
  ["Ethical impact", "Surveillance, bias, consent."],
] });
