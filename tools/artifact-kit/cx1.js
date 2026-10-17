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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;

chainStep("#stA", "One topic, three command words", ["State: parallel transmission sends several bits at the same time", "Describe: add how, each bit on its own wire, in one or both directions", "Explain why: add the reason, so data arrives quickly over a short distance", "Context: the computers are in one room, so the bits stay in step"], [
  "<b>State:</b> one clear fact earns one mark.", "<b>Describe:</b> the features of the method. Still only <i>what</i>.", "<b>Explain:</b> every sentence now has a reason: so, because.", "<b>Context:</b> the scenario decides which reasons count."]);
chainStep("#stB", "Turning a vague answer into marks", ["Vague: 'It is faster'", "Technical: 'The file is transmitted in less time'", "Reason: 'because there are fewer bits to send'", "Context: 'so the report fits under the size limit for the email'"], [
  "<b>Vague:</b> the report says this level of answer is not enough.", "<b>Technical:</b> name what is faster and use the term.", "<b>Reason:</b> say why it is quicker.", "<b>Context:</b> link to this file and this email."]);
chainStep("#stC", "Adding the context", ["Generic: 'Machine learning is when a computer learns from data'", "Linked to the device: 'The vacuum gathers data about the room as it cleans'", "What it does with it: 'and adapts its own route'", "Result: 'so it avoids obstacles and cleans dirtier areas for longer'"], [
  "<b>Generic:</b> true, but it earns no marks in a how-could-X-use-it question.", "<b>Device:</b> now it is about the robot vacuum.", "<b>Adapts:</b> the key idea the mark scheme looks for.", "<b>Benefit:</b> the consequence that completes the point."]);

chooser("h", [
  ["Identify", "A name only", "'The device is a router'", "Explaining when only a name is asked wastes time", 1],
  ["State", "One clear statement per mark", "'Lossless'; 'It is…'", "Adding reasons earns nothing extra", 1],
  ["Define", "The exact meaning with the technical term", "'A text-based address for…'", "Vague wording such as 'an address for a website'", 2],
  ["Outline", "Name plus a short expansion", "'A double entry check: the data is entered twice and compared'", "A name with no expansion earns half", 2],
  ["Describe", "Features or steps: what, not why", "'The packet has a header, a payload and a trailer'", "Listing the contents of a header instead of the structure", 3],
  ["Explain", "A point and its reason", "'…so the data arrives sooner'", "Describing how it works instead of why it is chosen", 5],
  ["Compare", "Both items in each point", "'Binary… whereas hexadecimal…'", "A sentence about one item only", 3],
  ["Suggest", "A fitting answer with a reason", "'A touchscreen, because the watch is small'", "A generic device that does not suit the scenario", 4]
], (it) => `${it[0]}: it wants ${it[1].toLowerCase()}. Start like this: ${it[2]}. Trap: ${it[3].toLowerCase()}.`, "Detail needed");

pick("m", [
  { label: "A", a: "The data is stored on the internet.", m: 0, why: "This repeats what cloud storage is. The report for this question says many candidates repeated the definition instead of giving a benefit." },
  { label: "B", a: "It is better and easier to use.", m: 0, why: "Vague words with no technical term and no reason. No mark scheme point matches." },
  { label: "C", a: "You can get your data on a phone or a laptop.", m: 1, why: "Matches the point that the data can be accessed from other devices, but the consequence is missing." },
  { label: "D", a: "You can get your data on a phone or a laptop, so if the watch breaks or is lost the data is still there.", m: 2, why: "The point plus its consequence: two marks for one benefit. A second benefit is needed for the other two." },
  { label: "E", a: "The watch needs less storage, which keeps it small. The data can also be reached from other devices.", m: 3, why: "The first benefit is a point with its consequence (two marks). The second is a point without a consequence (one mark)." },
  { label: "F", a: "You can get your data on a phone or a laptop, so if the watch breaks or is lost the data is still there. The provider can add more storage on demand, so the watch will not run out of space.", m: 4, why: "Two benefits, each with a consequence that fits the watch: four marks." }
], (it) => `<blockquote style="margin:10px 0">${it.a}</blockquote>${scoreBar(it.m, 4)}<div class="verdict">${it.why}</div>`);

pick("x", [
  { label: "Robot vacuum", g: "Machine learning means the computer learns from data.", b: "The vacuum collects data about the room while it cleans, such as where furniture is and which areas are dirtier. It uses the data to adapt its route, so it avoids obstacles and spends longer on the dirty areas.", w: "Gathers data, adapts its own process, gives an example and a benefit: the pattern in the mark scheme for this question." },
  { label: "Plough", g: "Artificial intelligence is when a machine acts like a human.", b: "The plough gathers data about the field as it works, such as its shape and where obstacles are. It builds a map and chooses the most efficient route, so it makes fewer mistakes the next time.", w: "Every sentence is about the plough and its field. The mark scheme lists a map, the route and fewer mistakes as creditable." },
  { label: "Smart phone", g: "A mouse and a printer.", b: "A touchscreen to enter text and a microphone for calls as input; a screen and a speaker to show and play content as output.", w: "A mouse and a printer are not built into a phone. The examiner report records this exact error." },
  { label: "Smartwatch ROM", g: "ROM is primary storage that cannot be changed.", b: "The ROM stores the start-up instructions, such as the firmware, so the watch can start. It is non-volatile, so the instructions are kept when the battery is flat.", w: "Describes the role in this watch. The generic answer defines ROM but does not say what it does here." }
], (it) => `<div class="grid2"><div><small>Generic answer</small><p style="margin:4px 0">${it.g}</p></div><div><small>Tied to the scenario</small><p style="margin:4px 0">${it.b}</p></div></div><div class="verdict">${it.w}</div>`);

let mode = 2;
function mt() {
  const m = +$("#mk").value, pts = mode === 2 ? Math.ceil(m / 2) : m, mins = m * 1.4;
  $("#r1").textContent = pts + (mode === 2 ? " with reasons" : "");
  $("#r2").textContent = Lib.fmtN(mins, 1) + " min";
  $("#rv").textContent = mode === 2 ? `${m} marks for an explanation: about ${pts} point${pts > 1 ? "s" : ""}, each with the reason that goes with it, in roughly ${Lib.fmtN(mins, 1)} minutes.` : mode === 1 ? `${m} marks for a description: about ${m} separate features or steps, kept short, in roughly ${Lib.fmtN(mins, 1)} minutes.` : `${m} marks for stating: ${m} separate short statements or answers, in roughly ${Lib.fmtN(mins, 1)} minutes.`;
  $("#labA").innerHTML = SV.rect(40, 40, (pts / 8) * 340, 36, "f1", op(0.6)) + SV.text(40, 32, "Points", "sm") + SV.rect(40, 120, Math.min(1, mins / 11.2) * 340, 36, "f2", op(0.6)) + SV.text(40, 112, "Minutes (out of 11.2 for 8 marks)", "sm");
}
$("#g2").innerHTML = [["State or identify", 0], ["Describe", 1], ["Explain", 2]].map(([t, v]) => `<button class="b${v === 2 ? " pri" : ""}" data-v="${v}">${t}</button>`).join("");
$$("#g2 button").forEach((b) => (b.onclick = () => { mode = +b.dataset.v; $$("#g2 button").forEach((x) => x.classList.toggle("pri", x === b)); mt(); }));
Lib.slider($("#g1"), { id: "mk", label: "Marks for the question ", min: 1, max: 8, step: 1, value: 4, fmt: (v) => v, onInput: mt });
mt();
Lib.classify($("#cl1"), { prompt: "Is each answer a fact, a description or an explanation?", buckets: [{"label": "State (a fact)"}, {"label": "Describe (features)"}, {"label": "Explain (a reason)"}], items: [{"text": "Lossless", "b": 0}, {"text": "A text-based address for a web page", "b": 0}, {"text": "The packet has a header, a payload and a trailer", "b": 1}, {"text": "Each bit travels along its own wire and several bits are sent together", "b": 1}, {"text": "Serial is more reliable over a long distance because the bits arrive in order", "b": 2}, {"text": "It has no moving parts, so the data is less likely to be lost if the phone is dropped", "b": 2}, {"text": "A check digit is recalculated after scanning and compared with the original", "b": 1}, {"text": "The checksum is worked out from the data, so a different value means the data has changed", "b": 2}], done: "State gives a fact, describe gives features, explain gives the reason." });
Lib.classify($("#cl2"), { prompt: "Does the answer mention both sides?", buckets: [{"label": "One side only"}, {"label": "Both sides"}], items: [{"text": "Hexadecimal uses letters", "b": 0}, {"text": "Binary uses only 0 and 1 whereas hexadecimal also uses A to F", "b": 1}, {"text": "Symmetric encryption uses one key", "b": 0}, {"text": "Symmetric uses one key whereas asymmetric uses a public and a private key", "b": 1}, {"text": "Serial sends bits one at a time", "b": 0}, {"text": "Serial sends one bit at a time whereas parallel sends several at once", "b": 1}], done: "In a difference, both items must appear in the same answer." });
Lib.order($("#o1"), { prompt: "Put the steps for answering an explain question in order.", items: ["Read the command word and the number of marks", "Underline the key term and the scenario", "Plan a point and a reason for each pair of marks", "Write each point with a link word such as so or because", "Check each pair uses a technical term and fits the scenario"], done: "Read, underline, plan, write, check." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Identify", "Name, select or recognise"], ["State", "Express in clear terms"], ["Describe", "State the points and main features of a topic"], ["Explain", "Set out reasons: say why and how"], ["Outline", "Set out the main points"], ["Compare", "Comment on similarities and/or differences"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Each paper has 75 marks in 105 minutes. How many minutes per mark?", "a": 1.4, "unit": "min", "tol": 0.05, "hint": "105 ÷ 75.", "sol": "<b>1.4 minutes</b>."},
  {"q": "At 1.4 minutes per mark, how many minutes for a 6-mark explanation?", "a": 8.4, "unit": "min", "tol": 0.1, "hint": "6 × 1.4.", "sol": "<b>8.4 minutes</b>."},
  {"q": "A mark scheme gives one mark for each method and one for a further description (max six). How many methods give full marks?", "a": 3, "unit": "", "tol": 0.01, "hint": "Each method is worth 2.", "sol": "<b>3</b> methods, each with a description."},
  {"q": "A 6-mark question allows a maximum of 4 marks for stating features. What is the least number of marks that must come from saying what the features do?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b> marks."},
  {"q": "An explain question awards marks for pairs of point and reason. How many pairs give 4 marks?", "a": 2, "unit": "", "tol": 0.01, "hint": "Each pair is worth 2.", "sol": "<b>2</b> pairs."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which command word asks you to say why or how?", opts: ["State", "Identify", "Explain", "Give"], a: 2, why: "Explain means set out reasons: say why and how." },
  { q: "A question asks for two differences between binary and hexadecimal. Which answer earns a mark?", opts: ["Hexadecimal uses letters", "Binary uses only 0 and 1 whereas hexadecimal also uses A to F", "Binary is a number system", "Hexadecimal is longer"], a: 1, why: "A difference must refer to both." },
  { q: "The mark scheme says 'six from, maximum 4 for stating features'. What does that mean?", opts: ["Four features and nothing else earn full marks", "Features alone earn at most 4; the rest need what each does", "Four features must be wrong", "Only four lines may be written"], a: 1, why: "Naming alone is capped." },
  { q: "Why is a mouse a poor answer to 'suggest an input device for a smart phone'?", opts: ["It is expensive", "It is not built into a smart phone", "It is an output device", "It needs a battery"], a: 1, why: "Answers must fit the scenario." },
  { q: "What does the generic marking principle say about wrong statements?", opts: ["Each loses a mark", "Marks are not deducted for errors", "They cancel a correct point", "They cap the answer at half marks"], a: 1, why: "Marks are awarded positively; errors are not deducted." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Identify", "Name, select, recognise."],
  ["State", "Clear statement, one per mark."],
  ["Describe", "Points and features: what."],
  ["Explain", "Reasons: why and how."],
  ["Compare", "Both items in each point."],
  ["Pairs", "Point plus reason or description."],
  ["Context", "Use the device or scenario."],
  ["Link words", "So, because, which means, this allows."],
] });
