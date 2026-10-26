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

/* a small logic engine: facts are {p, args}; goals are {p, args, neg} */
const KBS = {
  cats: ["type(leopard, wild)", "type(lion, wild)", "type(cheetah, wild)", "type(savannah, hybrid)", "type(persian, domestic)", "hair(leopard, medium)", "hair(lion, short)", "hair(cheetah, medium)", "hair(savannah, medium)", "hair(persian, long)", "spots(leopard, yes)", "spots(lion, no)", "spots(cheetah, yes)", "spots(savannah, yes)", "spots(persian, no)"],
  school: ["teaches(alan, mathematics)", "teaches(ioana, geography)", "teaches(nina, history)", "teaches(alan, statistics)", "studies(ahmed, history)", "studies(freya, history)", "studies(kim, history)", "studies(freya, geography)", "studies(hua, mathematics)", "studies(hua, statistics)", "studies(hua, geography)", "tutors(alan, kim)", "tutors(alan, hua)", "tutors(alan, freya)", "tutors(nina, ahmed)"],
  cinema: ["device(projector)", "device(large_tv)", "device(medium_tv)", "device(bluray_player)", "device(amplifier)", "device(media_player)", "device(main_speakers)", "customer(petrov)", "customer(margaret)", "customer(steffan)", "customer(susan)", "customer(allan)", "customer(sammy)", "owns(projector, petrov)", "owns(media_player, petrov)", "owns(projector, susan)", "owns(projector, sammy)", "owns(media_player, allan)", "owns(bluray_player, steffan)", "wants(main_speakers, margaret)", "wants(medium_tv, steffan)"],
  hobbies: ["hobby(music)", "hobby(caving)", "hobby(climbing)", "hobby(camping)", "hobby(baking)", "person(toby)", "person(natasha)", "person(fatima)", "person(joseph)", "person(elijah)", "person(nina)", "enjoys(natasha, travelling)", "enjoys(toby, climbing)", "enjoys(nina, climbing)", "enjoys(elijah, camping)", "enjoys(fatima, baking)", "enjoys(joseph, camping)", "dislikes(toby, caving)"]
};
const isVar = (a) => /^[A-Z_]/.test(a);
function parseOne(s) {
  const m = s.trim().replace(/\.$/, "").match(/^(NOT\s+|\\\+\s*)?([a-z][A-Za-z0-9_]*)\(([^()]*)\)$/);
  if (!m) return null;
  return { neg: !!m[1], p: m[2], args: m[3].split(",").map((x) => x.trim()) };
}
function parseGoals(s) {
  s = s.replace(/\bAND\b/g, ",").trim().replace(/\.$/, ""); const parts = []; let d = 0, cur = "";
  for (const ch of s) { if (ch === "(") d++; if (ch === ")") d--; if (ch === "," && d === 0) { parts.push(cur); cur = ""; } else cur += ch; }
  if (cur.trim()) parts.push(cur);
  const g = parts.map(parseOne); return g.some((x) => !x) || !g.length ? null : g;
}
const kbOf = (name) => KBS[name].map(parseOne);
function solve(KB, goals, env) {
  if (!goals.length) return [env];
  const g = goals[0];
  if (g.neg) { const r = solve(KB, [{ ...g, neg: false }], env); return r.length ? [] : solve(KB, goals.slice(1), env); }
  let out = [];
  for (const f of KB) {
    if (f.p !== g.p || f.args.length !== g.args.length) continue;
    const e = { ...env }; let ok = true;
    for (let i = 0; i < g.args.length && ok; i++) { const a = g.args[i]; if (isVar(a)) { if (a in e) ok = e[a] === f.args[i]; else e[a] = f.args[i]; } else ok = a === f.args[i]; }
    if (ok) out = out.concat(solve(KB, goals.slice(1), e));
  }
  return out;
}
const varsOf = (goals) => { const v = []; goals.forEach((g) => !g.neg && g.args.forEach((a) => isVar(a) && !v.includes(a) && v.push(a))); return v; };
const uniq = (a) => a.filter((x, i) => a.indexOf(x) === i);

/* ---- animations ---- */
(function () {
  const facts = [["leopard", "medium"], ["lion", "short"], ["cheetah", "medium"], ["savannah", "medium"], ["persian", "long"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "hair(Cat, medium)  ← the goal", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    const found = [];
    facts.forEach((f, i) => {
      const y = 50 + i * 38, tried = k > i, ok = f[1] === "medium";
      if (tried && ok) found.push(f[0]);
      o += SV.rect(30, y, 300, 32, !tried ? "cell" : ok ? "cell-ok" : "cell-no", { rx: 6, ...op(tried || k === i ? 1 : 0.7) }) + SV.text(44, y + 21, "hair(" + f[0] + ", " + f[1] + ").", "lbl", { style: "font-family:var(--mono);font-size:15px" });
      if (tried) o += SV.text(310, y + 22, ok ? "✓" : "✗", "lbl bd " + (ok ? "t3" : "t2"), { "text-anchor": "end", style: "font-size:18px" });
    });
    o += SV.text(400, 70, "Cat =", "lbl bd", { style: "font-size:17px" }) + SV.text(460, 70, found.join(", "), "lbl bd t3", { style: "font-family:var(--mono);font-size:17px" });
    if (k >= 5) o += SV.text(400, 100, "all matches returned, in fact order", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 260, label: "Matching a goal against the facts", base: { i: 0 }, draw, tween: 350, dwell: 2600, steps: [
    { cap: "The goal <code>hair(Cat, medium)</code> has a variable, <b>Cat</b>, and a constant, <b>medium</b>. The system tries each <code>hair</code> fact in turn.", s: { i: 0 } },
    { cap: "<code>hair(leopard, medium)</code> matches: medium = medium, so Cat = <b>leopard</b>.", s: { i: 1 } },
    { cap: "<code>hair(lion, short)</code>: short is not medium. No match.", s: { i: 2 } },
    { cap: "<code>hair(cheetah, medium)</code> matches: Cat = <b>cheetah</b>.", s: { i: 3 } },
    { cap: "<code>hair(savannah, medium)</code> matches: Cat = <b>savannah</b>.", s: { i: 4 } },
    { cap: "<code>hair(persian, long)</code> does not match. The goal returns <b>leopard, cheetah, savannah</b>.", s: { i: 5 } }] });
})();

(function () {
  const A = ["leopard", "cheetah", "savannah"], B = ["leopard", "lion", "cheetah"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "spots(WildSpotty, yes), type(WildSpotty, wild)", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const col = (x, title, items, hl, v) => { let t = SV.text(x, 70, title, "sm", op(v)); items.forEach((it, i) => { t += SV.rect(x, 80 + i * 36, 180, 30, hl.includes(it) ? "cell-ok" : "cell", { rx: 6, ...op(v) }) + SV.text(x + 12, 101 + i * 36, it, "lbl", { style: "font-family:var(--mono);font-size:15px", ...op(v) }); }); return t; };
    o += col(30, "spots(X, yes) gives", A, k >= 3 ? ["leopard", "cheetah"] : [], k >= 1 ? 1 : 0);
    o += col(280, "type(X, wild) gives", B, k >= 3 ? ["leopard", "cheetah"] : [], k >= 2 ? 1 : 0);
    if (k >= 3) o += SV.text(520, 100, "X must satisfy both:", "lbl bd") + SV.text(520, 130, "leopard", "lbl bd t3", { style: "font-family:var(--mono);font-size:18px" }) + SV.text(520, 160, "cheetah", "lbl bd t3", { style: "font-family:var(--mono);font-size:18px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 200, label: "Two conditions sharing a variable", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "Find the wild cats with spots. The variable <b>WildSpotty</b> appears in both conditions, so it must be the <b>same cat</b> in both.", s: { i: 0 } },
    { cap: "The first condition, <code>spots(WildSpotty, yes)</code>, is satisfied by leopard, cheetah and savannah.", s: { i: 1 } },
    { cap: "The second, <code>type(WildSpotty, wild)</code>, is satisfied by leopard, lion and cheetah.", s: { i: 2 } },
    { cap: "Only values that satisfy <b>both</b> are answers: <b>leopard, cheetah</b>. The comma means AND.", s: { i: 3 } }] });
})();

(function () {
  const rows = [
    ["device(D)", "D = projector", "found: device(projector)", 1],
    ["customer(A)", "A = betty", "found: customer(betty)", 1],
    ["NOT owns(D, A)", "owns(projector, betty)?", "not found, so NOT succeeds", 1],
  ];
  const rows2 = [["device(D)", "D = projector", "found", 1], ["customer(A)", "A = petrov", "found", 1], ["NOT owns(D, A)", "owns(projector, petrov)?", "found, so NOT fails", 0]];
  const draw = (s) => {
    const k = Math.round(s.i), R = k >= 4 ? rows2 : rows, n = k >= 4 ? k - 4 : k; let o = SV.text(30, 26, "may_buy_device(D, A) IF device(D), customer(A), NOT owns(D, A).", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.text(30, 52, k >= 4 ? "Try A = petrov (who owns a projector)" : "Try D = projector, A = betty", "sm");
    R.forEach((r, i) => { if (n <= i) return; const ok = r[3] === 1; o += SV.rect(30, 66 + i * 42, 700, 34, ok ? "cell-ok" : "cell-no", { rx: 6 }) + SV.text(44, 88 + i * 42, r[0], "lbl bd", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(250, 88 + i * 42, r[1], "lbl", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(520, 88 + i * 42, r[2], "lbl"); });
    if (n >= 3) o += SV.text(30, 220, k >= 4 ? "A condition failed: the rule is FALSE for this pair" : "All three conditions succeed: the rule is TRUE, so Betty may buy a projector", "lbl bd " + (k >= 4 ? "t2" : "t3"));
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Evaluating a rule with NOT", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "A rule is true when <b>every condition</b> is true. Betty is a new customer who owns nothing. Try D = projector and A = betty.", s: { i: 0 } },
    { cap: "<code>device(D)</code>: the fact <code>device(projector)</code> exists, so this is true.", s: { i: 1 } },
    { cap: "<code>customer(A)</code>: <code>customer(betty)</code> exists, so this is true.", s: { i: 2 } },
    { cap: "<code>NOT owns(D, A)</code>: the system looks for <code>owns(projector, betty)</code>. It is <b>not found</b>, so NOT succeeds. All true: Betty may buy a projector.", s: { i: 3 } },
    { cap: "Now try A = petrov, who owns a projector. The first two conditions are true again.", s: { i: 6 } },
    { cap: "<code>owns(projector, petrov)</code> <b>is</b> found, so <code>NOT owns(...)</code> fails and the rule is <b>false</b> for this pair: Petrov already owns one.", s: { i: 7 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(20, 20, 350, 200, "f1", { rx: 10, ...op(0.2) }) + SV.text(195, 44, "Imperative: how", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(390, 20, 350, 200, "f2", { rx: 10, ...op(0.2) }) + SV.text(565, 44, "Declarative: what", "lbl bd", { "text-anchor": "middle" });
    const imp = ["pets = []", "for cat in cats:", "    if cat.type == \"domestic\":", "        pets.append(cat)"];
    imp.forEach((l, i) => { if (k >= 1) o += SV.text(36, 80 + i * 26, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre" }); });
    if (k >= 2) o += SV.text(565, 100, "type(Pet, domestic).", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" });
    if (k >= 3) o += SV.text(36, 200, "You write the steps", "sm") + SV.text(410, 200, "You state the goal; the system searches the facts", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "Imperative against declarative", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "The problem: find all the domestic cats.", s: { i: 0 } },
    { cap: "<b>Imperative</b>: write the steps. Make a list, loop through every cat, test the type, add it if it matches.", s: { i: 1 } },
    { cap: "<b>Declarative</b>: state what you want as a goal. <code>type(Pet, domestic)</code> says 'find every Pet that is a domestic type'.", s: { i: 2 } },
    { cap: "The programmer states <i>what</i>; the system works out <i>how</i> by searching the facts and rules.", s: { i: 3 } }] });
})();

/* ---- Lab 1 ---- */
(function () {
  let kb = "cats";
  const names = [["cats", "Cats"], ["school", "School"], ["cinema", "Home cinema"], ["hobbies", "Hobbies"]];
  const ex = { cats: ["hair(Cat, medium)", "type(Pet, domestic)", "spots(WildSpotty, yes), type(WildSpotty, wild)", "hair(lion, short)", "hair(Cat, purple)"], school: ["studies(Student, geography)", "teaches(alan, Subject)", "teaches(R, S), studies(X, S), tutors(R, X)"], cinema: ["owns(projector, Owner)", "owns(media_player, Owner)", "customer(C), NOT owns(projector, C)"], hobbies: ["enjoys(P, camping)", "enjoys(P, climbing), person(P)", "person(P), NOT enjoys(P, climbing)"] };
  const paint = () => {
    $$("#kB button").forEach((b, i) => b.classList.toggle("pri", names[i][0] === kb));
    $("#kF").innerHTML = '<div class="code"><pre class="cp">' + KBS[kb].map((f) => `<span class="ln">${f}.</span>`).join("") + "</pre></div>";
    $("#kE").innerHTML = ex[kb].map((e, i) => `<button class="b" data-i="${i}">${e}</button>`).join("");
    $$("#kE button").forEach((b) => (b.onclick = () => { $("#kQ").value = ex[kb][+b.dataset.i]; run(); }));
    $("#kQ").value = ex[kb][0]; run();
  };
  const run = () => {
    const g = parseGoals($("#kQ").value), out = $("#kV");
    if (!g) { out.textContent = "That is not a valid goal. Use the form predicate(argument, argument), with commas between conditions."; return; }
    const bad = g.find((x) => x.neg && x.args.some((a) => isVar(a)) && !g.some((y) => !y.neg && y.args.some((a) => x.args.includes(a))));
    if (bad) { out.textContent = "Put the condition that gives the variable a value before the NOT condition."; return; }
    const sol = solve(kbOf(kb), g, {}), vs = varsOf(g);
    if (!sol.length) { out.textContent = "false: no values make the goal true."; return; }
    if (!vs.length) { out.textContent = "true"; return; }
    out.innerHTML = vs.map((v) => "<b>" + v + "</b> = " + uniq(sol.map((e) => e[v])).join(", ")).join("<br>");
  };
  $("#kB").innerHTML = names.map((n, i) => `<button class="b" data-i="${i}">${n[1]}</button>`).join("");
  $$("#kB button").forEach((b) => (b.onclick = () => { kb = names[+b.dataset.i][0]; paint(); }));
  $("#kR").onclick = run; $("#kQ").addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  paint();
})();

/* ---- Lab 2 ---- */
(function () {
  const rules = [
    ["cats", "wild_spotty(X)", "spots(X, yes), type(X, wild)"],
    ["school", "student_of_own_tutor(X)", "teaches(R, S), studies(X, S), tutors(R, X)"],
    ["cinema", "may_buy_device(D, A)", "device(D), customer(A), NOT owns(D, A)"],
    ["hobbies", "might_enjoy(N, H)", "person(N), hobby(H), NOT dislikes(N, H)"]
  ];
  let cur = 2;
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#rH").textContent = rules[cur][1]; $("#rQ").value = rules[cur][2]; run();
  };
  const run = () => {
    const g = parseGoals($("#rQ").value), o = $("#rO"), v = $("#rV");
    if (!g) { o.innerHTML = ""; v.textContent = "Check the conditions: predicate(arguments), separated by commas."; return; }
    const vars = rules[cur][1].match(/\(([^)]*)\)/)[1].split(",").map((s) => s.trim());
    const sol = solve(kbOf(rules[cur][0]), g, {}), rows = uniq(sol.map((e) => vars.map((x) => e[x]).join("|"))).map((r) => r.split("|"));
    o.innerHTML = '<div class="tw"><table class="t mono"><tr>' + vars.map((x) => `<th>${x}</th>`).join("") + "</tr>" + rows.slice(0, 12).map((r) => "<tr>" + r.map((c) => `<td>${c}</td>`).join("") + "</tr>").join("") + "</table></div>";
    v.textContent = rows.length ? `The rule is true for ${rows.length} combination${rows.length === 1 ? "" : "s"}${rows.length > 12 ? " (first 12 shown)" : ""}.` : "The rule is not true for any combination.";
  };
  $("#rB").innerHTML = rules.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#rB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  $("#rR").onclick = run; paint();
})();

btnTable("eB", "eO", [
  ["Capital letter on a constant", "customer(Betty).", "Betty is read as a variable, so the fact means 'every thing is a customer'", "customer(betty)."],
  ["Missing 'is a' fact", "owns(large_tv, betty). (and nothing else)", "Betty is never declared a customer, so a rule using customer(A) cannot find her", "customer(betty). owns(large_tv, betty)."],
  ["Wrong argument order", "owns(betty, large_tv).", "Does not match the other facts, which have the device first", "owns(large_tv, betty)."],
  ["Unlinked variables", "teaches(R, S), studies(X, T), tutors(R, X)", "S and T are different variables, so the subject is not linked", "teaches(R, S), studies(X, S), tutors(R, X)"],
  ["NOT first", "NOT owns(D, A), device(D), customer(A)", "D and A have no values yet when NOT is tested", "device(D), customer(A), NOT owns(D, A)"],
  ["Missing a condition", "may_buy_device(D, A) IF device(D) AND NOT owns(D, A)", "A is never said to be a customer", "add customer(A)"],
  ["Missing full stop or extra text", "type(caracal, wild)", "Each clause ends with a full stop", "type(caracal, wild)."]
], ["Mistake", "Example", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Is each clause a fact, a rule or a goal?", buckets: [{"label": "Fact"}, {"label": "Rule"}, {"label": "Goal"}], items: [{"text": "type(caracal, wild).", "b": 0}, {"text": "hair(Cat, long)", "b": 2}, {"text": "may_buy_device(D, A) IF device(D) AND customer(A) AND NOT owns(D, A).", "b": 1}, {"text": "customer(betty).", "b": 0}, {"text": "owns(projector, Owner)", "b": 2}, {"text": "might_enjoy(N, H) IF person(N), hobby(H), NOT dislikes(N, H).", "b": 1}, {"text": "studies(sam, history).", "b": 0}, {"text": "spots(X, yes), type(X, wild)", "b": 2}], done: "Facts end with a full stop and have no variables. Rules have IF. Goals have variables and ask a question." });
Lib.classify($("#cl2"), { prompt: "Is each name a constant or a variable?", buckets: [{"label": "Constant"}, {"label": "Variable"}], items: [{"text": "leopard", "b": 0}, {"text": "Cat", "b": 1}, {"text": "domestic", "b": 0}, {"text": "WildSpotty", "b": 1}, {"text": "Owner", "b": 1}, {"text": "projector", "b": 0}, {"text": "D", "b": 1}, {"text": "yes", "b": 0}], done: "Lower-case first letter: constant. Capital first letter: variable." });
Lib.order($("#o1"), { prompt: "Put the steps for answering a goal in order.", items: ["Take the first condition of the goal", "Look through the facts for ones that match", "Fill in the variables from each match", "Test the next condition using those values", "Return every set of values that satisfies all the conditions"], done: "Match, fill, test the next, collect all." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Fact", "A statement that is true, with a full stop"], ["Rule", "True if its conditions are true: IF with AND and NOT"], ["Goal", "A query the system tries to satisfy"], ["Variable", "A name starting with a capital that the system fills in"], ["Knowledge base", "All the facts and rules together"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Cats knowledge base: how many cats does hair(Cat, medium) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "leopard, cheetah, savannah.", "sol": "<b>3</b>."},
  {"q": "Cats: how many cats does spots(Cat, yes) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "leopard, cheetah, savannah.", "sol": "<b>3</b>."},
  {"q": "Cats: how many does spots(Cat, yes), type(Cat, wild) return?", "a": 2, "unit": "", "tol": 0.01, "hint": "Both conditions: leopard and cheetah.", "sol": "<b>2</b>."},
  {"q": "Cinema: how many customers does owns(projector, Owner) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "petrov, susan, sammy.", "sol": "<b>3</b>."},
  {"q": "School: how many students does studies(Student, history) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "ahmed, freya, kim.", "sol": "<b>3</b>."},
  {"q": "A knowledge base has 5 devices and 4 customers, and one owns fact. How many (device, customer) pairs satisfy device(D), customer(A), NOT owns(D, A)?", "a": 19, "unit": "", "tol": 0.01, "hint": "5 × 4 = 20 pairs, minus the one that is owned.", "sol": "<b>19</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a declarative program state?", opts: ["The steps to follow", "What result is wanted, using facts and rules", "The machine code", "The loop to repeat"], a: 1, why: "Declarative says what, not how." },
  { q: "Which is a variable?", opts: ["betty", "projector", "Owner", "yes"], a: 2, why: "A capital first letter makes it a variable." },
  { q: "Which rule is correct for: D may be bought by A if D is a device, A is a customer and A does not own D?", opts: ["may_buy(D, A) IF device(D) AND customer(A) AND owns(D, A)", "may_buy(D, A) IF device(D) AND customer(A) AND NOT owns(D, A)", "may_buy(D, A) IF NOT owns(D, A)", "may_buy(D, A) IF device(D) OR customer(A)"], a: 1, why: "Two 'is a' conditions and a NOT." },
  { q: "A new customer, Zoe, owns a tablet. Which facts are needed?", opts: ["owns(tablet, zoe).", "customer(zoe). owns(tablet, zoe).", "customer(Zoe). owns(tablet, Zoe).", "zoe(customer). owns(zoe, tablet)."], a: 1, why: "Declare the customer, then what she owns, in the knowledge base's order." },
  { q: "What does NOT owns(D, A) mean in a rule?", opts: ["A owns D", "The fact owns(D, A) cannot be found", "D is a device", "A is a customer"], a: 1, why: "NOT succeeds when the fact is not found." },
  { q: "Which language type is Prolog?", opts: ["Low-level", "Imperative", "Object-oriented", "Declarative (logic)"], a: 3, why: "Facts, rules and goals." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Declarative programming", "States what is wanted using facts and rules; the system works out how."],
  ["Fact", "A true statement: type(lion, wild)."],
  ["Rule", "True if conditions are true: head IF cond AND cond."],
  ["Goal", "A query: hair(Cat, medium)."],
  ["Variable", "Capital first letter. Filled in by the system."],
  ["Constant", "Lower-case first letter. A specific value."],
  ["AND", "A comma between conditions: all must be true."],
  ["NOT", "Succeeds if the fact is not found."],
] });
