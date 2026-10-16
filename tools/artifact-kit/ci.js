/* ===== 19.2 Recursion: trace engine ===== */
const RW = 720, RH = 372;

/* Records every call/return of a recursive function as snapshots, then draws stack + call tree. */
function Trace(o = {}) {
  const nodes = [], stack = [], snaps = [], out = [];
  let phase = "down", pdata = null, alert = null;
  const clonePanel = () => (pdata ? JSON.parse(JSON.stringify(pdata)) : null);
  const snap = (cap, ps, py) => snaps.push({
    cap, ps, py, phase, alert, out: [...out], n: nodes.length, panel: clonePanel(),
    ns: nodes.map((n) => [n.st, n.val]),
    stack: stack.map((f) => ({ label: f.label, ra: f.ra, status: f.status, st: f.st })),
  });
  const T = {
    nodes, out, o,
    setPanel(d) { pdata = d; },
    print(t) { out.push(t); },
    setStatus(nd, s) { nd.fr.status = s; },
    call(label, short, parent, ra, cap, ps, py, status = "", st = "run") {
      if (parent) { parent.st = "wait"; parent.fr.st = "wait"; }
      const nd = { label, short, parent, kids: [], st: "act", val: null };
      nodes.push(nd); parent && parent.kids.push(nd);
      nd.fr = { label, ra, status, st }; stack.push(nd.fr);
      phase = "down"; snap(cap, ps, py); return nd;
    },
    note(nd, status, cap, ps, py, st = "run") { nd.fr.status = status; nd.fr.st = st; nd.st = "act"; snap(cap, ps, py); },
    ret(nd, val, cap, ps, py, outLine, status) {
      nd.fr.status = status || (val === undefined || val === null ? "finished" : "returns " + val); nd.fr.st = "ret"; nd.st = "done"; nd.val = val ?? "";
      if (outLine) out.push(outLine);
      phase = "up"; snap(cap, ps, py); stack.pop();
    },
    finish(cap, ps, py, al) { alert = al || null; snap(cap, ps, py); },
    alertNow(a) { alert = a; },
  };
  T.build = () => {
    layout(nodes);
    return snaps.map((s) => ({ cap: s.cap, ps: s.ps, py: s.py, svg: drawSnap(s, nodes, o) }));
  };
  T.maxDepth = () => 0;
  return T;
}

/* tree layout: leaves spaced evenly, parents centred over children */
function layout(nodes) {
  if (!nodes.length) return;
  let leaf = 0; const depthOf = (n) => (n.parent ? depthOf(n.parent) + 1 : 0);
  const go = (n) => { if (!n.kids.length) n.lx = leaf++; else { n.kids.forEach(go); n.lx = (n.kids[0].lx + n.kids[n.kids.length - 1].lx) / 2; } };
  go(nodes[0]); nodes.forEach((n) => (n.d = depthOf(n)));
  nodes.leaves = leaf; nodes.depth = Math.max(...nodes.map((n) => n.d)) + 1;
}

function maxStack(snaps) { return Math.max(1, ...snaps.map((s) => s.stack.length)); }

function drawSnap(s, nodes, o) {
  const maxD = o.maxDepth || 5, fh = Math.max(34, Math.min(50, Math.floor(272 / maxD) - 5)), gap = 5, X = 14, FW = 340, base = 322;
  let g = "";
  // left: call stack
  g += SV.text(X, 22, "CALL STACK", "sm bd", { "text-anchor": "start", style: "letter-spacing:.1em" });
  g += SV.text(X + FW, 22, s.phase === "down" ? "▼ WINDING (calls)" : "▲ UNWINDING (returns)", "lbl bd " + (s.phase === "down" ? "t1" : "t3"), { "text-anchor": "end" });
  g += SV.line(X - 4, base + 3, X + FW + 4, base + 3, "ax");
  g += SV.text(X, base + 20, "bottom of stack: main program", "sm", { "text-anchor": "start" });
  s.stack.forEach((f, i) => {
    const y = base - fh - i * (fh + gap), c = { run: "cell-cur", wait: "", ret: "cell-ok", base: "cell-warn" }[f.st];
    g += SV.rect(X, y, FW, fh, "cell " + c, { rx: 8 });
    g += SV.text(X + 10, y + (fh > 40 ? 20 : 15), esc(f.label), "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:14px" });
    g += SV.text(X + FW - 10, y + fh - (fh > 40 ? 10 : 6), "↩ " + esc(f.ra), "sm", { "text-anchor": "end" });
    if (f.status) g += SV.text(X + 10, y + fh - (fh > 40 ? 10 : 6), esc(f.status), "lbl", { "text-anchor": "start", style: "font-size:12.5px" });
  });
  if (!s.stack.length) g += SV.text(X + FW / 2, base - 40, "stack is empty", "lbl", { "text-anchor": "middle", style: "font-style:italic;fill:var(--muted)" });
  // right: call tree
  const RX = 388, RWd = RW - RX - 10;
  g += SV.text(RX, 22, "CALL TREE  " + (o.treeName || ""), "sm bd", { "text-anchor": "start", style: "letter-spacing:.1em" });
  const lv = nodes.depth || 1, lvs = nodes.leaves || 1, r = nodes.length > 12 ? 14 : nodes.some((n) => String(n.short).length > 3) ? 22 : 17, dy = Math.min(52, 190 / Math.max(1, lv - 1 || 1)), sp = lvs > 1 ? Math.min(54, (RWd - 2 * r) / (lvs - 1)) : 0;
  const tw = (lvs - 1) * sp, ox = RX + RWd / 2 - tw / 2, oy = 52;
  const px = (n) => ox + n.lx * sp, py = (n) => oy + n.d * dy;
  nodes.forEach((n, i) => { if (n.parent) { const live = i < s.n; g += SV.line(px(n.parent), py(n.parent), px(n), py(n), live ? "edge" : "edge", { opacity: live ? 1 : 0.18 }); } });
  nodes.forEach((n, i) => {
    const live = i < s.n, st = live ? s.ns[i][0] : "new", val = live ? s.ns[i][1] : null;
    const cls = { new: "nd", wait: "nd", act: "nd nd-cur", done: "nd nd-ok" }[st];
    g += `<g opacity="${live ? 1 : 0.22}">` + SV.circle(px(n), py(n), r, cls, st === "wait" ? { style: "stroke:var(--warn);stroke-width:3.5;fill:var(--warn-soft)" } : {}) + SV.text(px(n), py(n) + 5, esc(n.short), "lbl bd", { "text-anchor": "middle", style: "font-size:" + (String(n.short).length > 3 ? 10 : String(n.short).length > 2 ? 10.5 : r < 16 ? 11 : 13) + "px" });
    if (st === "done" && val !== "" && val !== null) g += SV.text(px(n) + r + 3, py(n) + 4, esc(val), "sm bd t3", { "text-anchor": "start", style: "font-family:var(--mono);font-size:11.5px" });
    g += "</g>";
  });
  // bottom right: output / returned values / custom panel
  const BY = 268;
  g += SV.rect(RX, BY, RWd, 90, "cell", { rx: 8 });
  if (s.panel && o.panelFn) g += o.panelFn(s.panel, RX, BY, RWd);
  else {
    g += SV.text(RX + 10, BY + 16, (o.outTitle || "OUTPUT").toUpperCase(), "sm bd", { "text-anchor": "start", style: "letter-spacing:.1em" });
    s.out.forEach((t, i) => { const col = i < 5 ? 0 : 1, row = i % 5; g += SV.text(RX + 10 + col * (RWd / 2), BY + 33 + row * 13.5, esc(t), "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:12px" }); });
  }
  if (s.alert) { g += SV.rect(RX, BY, RWd, 90, "cell cell-no", { rx: 8 }) + SV.text(RX + RWd / 2, BY + 52, esc(s.alert), "lbl bd t2", { "text-anchor": "middle", style: "font-size:17px" }); }
  return g;
}

/* helper: run a simulation and hand the frames to Lib.algo */
function showAlgo(sel, T, code, label, dwell = 2600) {
  const frames = T.build();
  Lib.algo($(sel), { w: RW, h: RH, label, pseudo: code.ps, py: code.py, dwell, frames });
}

/* ===== Compound interest: recursive function, trace tables, past papers ===== */
const r4 = (x) => Math.round(x * 1e4) / 1e4;
const f2 = (x) => String(r4(x));
const cc = (p, y, r) => `compoundInt(${f2(p)}, ${r}, ${y})`;

const PS_A = ["FUNCTION compoundInt(principal, rate : REAL, years : INTEGER) RETURNS REAL", "   IF years = 0", "      THEN", "         total ← principal", "      ELSE", "         total ← compoundInt(principal, rate, years - 1) * rate", "   ENDIF", "   RETURN total", "ENDFUNCTION"];
const PY_A = ["def compound_int(principal, rate, years):", "    if years == 0:", "        total = principal", "    else:", "        total = compound_int(principal, rate, years - 1) * rate", "    return total"];
const PS_B = PS_A.map((l, i) => (i === 5 ? "         total ← compoundInt(principal * rate, rate, years - 1)" : l));
const PY_B = PY_A.map((l, i) => (i === 4 ? "        total = compound_int(principal * rate, rate, years - 1)" : l));
const CODE = { A: { ps: PS_A, py: PY_A }, B: { ps: PS_B, py: PY_B } };

/* Trace-table rows for either version. Version A multiplies on the way up (coursebook Table 19.28 and its RETURN column);
   Version B passes principal * rate down (the coursebook's printed code). */
function rowsFor(ver, P, r, y) {
  const v = [P]; for (let j = 1; j <= y; j++) v.push(r4(v[j - 1] * r));
  const fin = v[y], rows = [];
  for (let k = 0; k <= y; k++) {
    const yrs = y - k, no = k + 1, pk = ver === "A" ? P : v[k], fc = cc(pk, yrs, r);
    if (yrs > 0) {
      const tot = ver === "A" ? `${cc(P, yrs - 1, r)} * ${r}` : cc(v[k + 1], yrs - 1, r);
      rows.push({ no, fc, yrs, tot, ret: "", kind: "down", ps: [1, 5], py: [1, 4],
        cap: ver === "A"
          ? `<b>Call ${no}: ${fc}.</b> years is ${yrs}, not 0, so this is the <b>general case</b>. The total cell holds the calculation it cannot finish yet: ${tot}. The call waits, so nothing is returned.`
          : `<b>Call ${no}: ${fc}.</b> years is ${yrs}, so this is the <b>general case</b>. It passes principal × rate = ${f2(v[k + 1])} down to the next call. The money grows <i>on the way down</i>; the call then waits.` });
    } else {
      const val = ver === "A" ? P : fin;
      rows.push({ no, fc, yrs, tot: f2(val), ret: f2(val), kind: "base", ps: [1, 3, 7], py: [1, 2, 5],
        cap: ver === "A"
          ? `<b>Call ${no}: ${fc}.</b> years = 0: the <b>base case</b>. total ← principal = ${f2(P)}, and it returns ${f2(P)}. First RETURN, so <b>unwinding starts here</b>.`
          : `<b>Call ${no}: ${fc}.</b> years = 0: the <b>base case</b>. total ← principal. By now the principal has grown to ${f2(fin)}, so it returns ${f2(fin)}.` });
    }
  }
  for (let j = 1; j <= y; j++) {
    const no = y - j + 1, fc = cc(ver === "A" ? P : v[y - j], j, r);
    rows.push({ no: no + " cont", fc, yrs: j, tot: ver === "A" ? `${f2(v[j - 1])} * ${r}` : f2(fin), ret: f2(v[j]), kind: "up", ps: ver === "A" ? [5, 7] : [5, 7], py: ver === "A" ? [4, 5] : [4, 5],
      cap: ver === "A"
        ? `<b>Call ${no} resumes</b> (${fc}). The call below returned ${f2(v[j - 1])}, so total = ${f2(v[j - 1])} × ${r} = <b>${f2(v[j])}</b>, which it returns upwards.`
        : `<b>Call ${no} resumes.</b> The call below returned ${f2(fin)}; total ← ${f2(fin)} and it returns that <b>unchanged</b>. Nothing is calculated on the way up.` });
  }
  return rows;
}

const COLS = [["Call no.", 0, 62], ["Function call", 62, 232], ["years", 294, 50], ["total", 344, 276], ["RETURN", 620, 100]];
function tableSvg(rows, n) {
  const RH2 = 30, top = 40, H = top + rows.length * RH2 + 8;
  let g = `<g>`;
  COLS.forEach(([t, x, w]) => { g += SV.text(x + 8, 26, t, "sm bd", { style: "font-size:11px;text-transform:uppercase;letter-spacing:.03em" }); });
  g += SV.line(0, 34, 720, 34, "ax");
  rows.forEach((r, i) => {
    const y = top + i * RH2;
    if (i >= n) { g += SV.rect(0, y, 720, RH2, "cell", { style: "opacity:.35;stroke-width:1" }); return; }
    const cls = i === n - 1 ? "cell cell-cur" : r.kind === "base" ? "cell cell-warn" : r.kind === "up" ? "cell cell-ok" : "cell";
    g += SV.rect(1, y + 1, 718, RH2 - 2, cls, { style: "stroke-width:" + (i === n - 1 ? 2.5 : 1.2) });
    const cells = [r.no, r.fc, r.yrs, r.tot, r.ret];
    cells.forEach((c, k) => { const [, x, w] = COLS[k], mid = k === 0 || k === 2 || k === 4; g += SV.text(mid ? x + w / 2 : x + 8, y + 20, esc(c), "lbl" + (k === 4 ? " bd" : ""), { "text-anchor": mid ? "middle" : "start", style: "font-family:var(--mono);font-size:12px" }); });
  });
  COLS.slice(1).forEach(([, x]) => { g += SV.line(x, 34, x, top + rows.length * RH2, "gr"); });
  return g + "</g>";
}

function tableAlgo(sel, ver, P, r, y, label) {
  const rows = rowsFor(ver, P, r, y), fc = (i) => rows[i];
  const frames = [{ cap: `A <b>trace table</b> has one row per call. The first rows go <b>down</b> (the calls), then the rows marked “cont” go <b>up</b> (the same calls finishing). The code line being worked on is highlighted. Press Next to fill in call 1.`, ps: [0], py: [0], svg: tableSvg(rows, 0) }];
  rows.forEach((r2, i) => frames.push({ cap: r2.cap, ps: r2.ps, py: r2.py, svg: tableSvg(rows, i + 1) }));
  Lib.algo($(sel), { w: 720, h: 40 + rows.length * 30 + 10, label, pseudo: CODE[ver].ps, py: CODE[ver].py, dwell: 3400, frames });
}

/* Stack + call tree animation */
function ciTrace(ver, P, r, y) {
  const T = Trace({ treeName: "years", outTitle: "Values returned so far", maxDepth: y + 1 });
  const lab = (p, yy) => cc(p, yy, r);
  const run = (p, yy, parent, ra) => {
    const nd = T.call(lab(p, yy), yy, parent, ra, `<b>${lab(p, yy)}</b> is called. A new frame is pushed holding principal = ${f2(p)}, rate = ${r} and years = ${yy}.`, [0], [0]);
    if (yy === 0) {
      T.note(nd, "years = 0: BASE CASE", `Is years = 0? <b>Yes</b>: the <b>base case</b>. total ← principal, so total = ${f2(p)}. No further call is made.`, [1, 3], [1, 2], "base");
      T.print(`years 0 returns ${f2(p)}`);
      T.ret(nd, f2(p), `RETURN total sends <b>${f2(p)}</b> back to the waiting call. The frame is popped and <b>unwinding begins</b>.`, [7], [5]);
      return p;
    }
    if (ver === "A") {
      T.note(nd, "general case: must wait", `Is years = 0? No (${yy}). General case: total ← compoundInt(principal, rate, ${yy - 1}) * rate. The multiplication <b>cannot happen yet</b>, because the call has to return first.`, [1, 5], [1, 4]);
      T.setStatus(nd, `paused: waiting for years = ${yy - 1}`);
      const v = run(p, yy - 1, nd, "line 6"), t = r4(v * r);
      T.note(nd, `${f2(v)} * ${r} = ${f2(t)}`, `The call below returned ${f2(v)}. This frame <b>resumes</b> at the same line: total ← ${f2(v)} * ${r} = <b>${f2(t)}</b>.`, [5], [4]);
      T.print(`years ${yy} returns ${f2(t)}`);
      T.ret(nd, f2(t), `RETURN total sends ${f2(t)} up. The frame is popped.`, [7], [5]);
      return t;
    }
    const np = r4(p * r);
    T.note(nd, `passes ${f2(np)} down`, `General case: the new principal is principal * rate = ${f2(p)} * ${r} = <b>${f2(np)}</b>. It is worked out <b>before</b> the call and handed down.`, [1, 5], [1, 4]);
    T.setStatus(nd, `paused: waiting for years = ${yy - 1}`);
    const v = run(np, yy - 1, nd, "line 6");
    T.note(nd, `total ← ${f2(v)}`, `The call below returned ${f2(v)}. total ← ${f2(v)}. There is <b>nothing left to calculate</b>.`, [5], [4]);
    T.print(`years ${yy} returns ${f2(v)}`);
    T.ret(nd, f2(v), `RETURN total passes ${f2(v)} up <b>unchanged</b>. The frame is popped.`, [7], [5]);
    return v;
  };
  const res = run(P, y, null, "main");
  T.finish(ver === "A" ? `The stack is empty. The answer is ${f2(res)}. The money grew one year at a time <b>during the unwinding</b>: ${P} → ${Array.from({ length: y }, (_, i) => f2(P * Math.pow(r, i + 1))).join(" → ")}.` : `The stack is empty. The answer is ${f2(res)}. The money grew <b>on the way down</b>; the unwinding only passed the finished answer back up.`, [], []);
  return T;
}
function stackAlgo(sel, ver, P, r, y, label) { showAlgo(sel, ciTrace(ver, P, r, y), CODE[ver], label, 2800); }

stackAlgo("#aStackA", "A", 100, 1.05, 3, "Animated call stack and call tree for compoundInt(100, 1.05, 3), Version A");
tableAlgo("#aTabA", "A", 100, 1.05, 3, "Trace table being filled in for compoundInt(100, 1.05, 3), Version A");
stackAlgo("#aStackB", "B", 100, 1.05, 3, "Animated call stack and call tree for compoundInt(100, 1.05, 3), Version B");
tableAlgo("#aTabB", "B", 100, 1.05, 3, "Trace table being filled in for compoundInt(100, 1.05, 3), Version B");

/* trace table as plain HTML (Learn, Explore, exam answers) */
function tableHtml(rows) {
  const bg = { base: "var(--warn-soft)", up: "var(--good-soft)", down: "transparent" };
  return `<div class="tw"><table class="t mono"><tr><th>Call number</th><th>Function call</th><th>years</th><th>total</th><th>RETURN</th></tr>${rows.map((r) => `<tr style="background:${bg[r.kind]}"><td>${r.no}</td><td>${esc(r.fc)}</td><td>${r.yrs}</td><td>${esc(r.tot)}</td><td><b>${esc(r.ret)}</b></td></tr>`).join("")}</table></div>`;
}
$$("[data-tt]").forEach((el) => { const [ver, P, r, y] = el.dataset.tt.split(","); el.innerHTML = tableHtml(rowsFor(ver, +P, +r, +y)); });

/* ===== Explore lab: sliders, bars, live trace table ===== */
(() => {
  const S = {}; let ver = "A";
  const bars = (P, r, y) => {
    const W = 720, H = 250, n = y + 1, bw = Math.min(64, (W - 40) / n - 10), g = (W - 40 - n * bw) / Math.max(1, n - 1 || 1), base = 205, vals = [P];
    for (let j = 1; j <= y; j++) vals.push(r4(vals[j - 1] * r));
    const mx = vals[y] * 1.12;
    let s = SV.line(20, base, W - 20, base, "ax");
    vals.forEach((v, i) => {
      const x = n === 1 ? W / 2 - bw / 2 : 20 + i * (bw + g), hp = (P / mx) * 170, ht = (v / mx) * 170;
      s += SV.rect(x, base - hp, bw, hp, "", { rx: 3, style: "fill:var(--accent)" });
      if (ht - hp > 0.5) s += SV.rect(x, base - ht, bw, ht - hp, "", { rx: 3, style: "fill:var(--good)" });
      s += SV.text(x + bw / 2, base - ht - 7, f2(Math.round(v * 100) / 100), "lbl bd", { "text-anchor": "middle", style: "font-size:13px;font-family:var(--mono)" });
      s += SV.text(x + bw / 2, base + 18, "year " + i, "sm", { "text-anchor": "middle" });
    });
    s += SV.rect(20, 232, 12, 12, "", { style: "fill:var(--accent)" }) + SV.text(38, 243, "principal", "sm") + SV.rect(120, 232, 12, 12, "", { style: "fill:var(--good)" }) + SV.text(138, 243, "interest added", "sm");
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Bar chart of the balance each year">${s}</svg>`;
  };
  const draw = () => {
    if (!S.p || !S.r || !S.y) return;
    const P = S.p.get(), pct = S.r.get(), y = S.y.get(), r = r4(1 + pct / 100);
    let v = P; for (let j = 0; j < y; j++) v = r4(v * r);
    $("#ciChart").innerHTML = bars(P, r, y);
    $("#ciRO").innerHTML = `<div><small>Rate argument</small><strong>${r}</strong></div><div><small>Final amount</small><strong>${f2(Math.round(v * 100) / 100)}</strong></div><div><small>Interest earned</small><strong>${f2(Math.round((v - P) * 100) / 100)}</strong></div><div><small>Calls made</small><strong>${y + 1}</strong></div><div><small>Deepest stack</small><strong>${y + 1} frames</strong></div>`;
    $("#ciCall").textContent = `compoundInt(${P}, ${r}, ${y})`;
    $("#ciTbl").innerHTML = tableHtml(rowsFor(ver, P, r, y));
  };
  S.p = Lib.slider($("#slP"), { id: "sP", label: "principal: ", min: 100, max: 1000, step: 50, value: 100, onInput: draw });
  S.r = Lib.slider($("#slR"), { id: "sR", label: "interest rate (%): ", min: 1, max: 15, step: 1, value: 5, fmt: (v) => v + "%", onInput: draw });
  S.y = Lib.slider($("#slY"), { id: "sY", label: "years: ", min: 0, max: 8, step: 1, value: 3, onInput: draw });
  $("#ciVer").addEventListener("change", (e) => { ver = e.target.value; draw(); });
  draw();
})();

/* ===== Activities ===== */
Lib.order($("#o1"), { prompt: "compoundInt(100, 1.05, 2) is called (Version A). Put the events in the order they happen.", items: ["compoundInt(100, 1.05, 2) is called and its frame is pushed", "compoundInt(100, 1.05, 1) is called and its frame is pushed", "compoundInt(100, 1.05, 0) is called: base case, returns 100", "The years = 1 call works out 100 × 1.05 and returns 105", "The years = 2 call works out 105 × 1.05 and returns 110.25"], done: "Calls go down to the base case; the multiplications happen one at a time on the way back up." });

Lib.classify($("#cl1"), { prompt: "Drag each piece of the function to the part of recursion it plays (Version A).", buckets: [{ label: "Base case" }, { label: "General case (calls itself)" }, { label: "Moves towards the base case" }, { label: "Runs during unwinding" }], items: [
  { text: "IF years = 0", b: 0 }, { text: "total ← principal", b: 0 }, { text: "compoundInt(principal, rate, years - 1)", b: 1 }, { text: "years - 1", b: 2 }, { text: "… * rate (done after the call returns)", b: 3 }, { text: "105 × 1.05 = 110.25 in the row “2 cont”", b: 3 }], done: "The base case stops it, the general case repeats it, years - 1 guarantees it ends." });

Lib.classify($("#cl2"), { prompt: "Which version is each statement true of? Version A multiplies by rate after the call returns. Version B passes principal * rate down.", buckets: [{ label: "Version A: × rate on the way up" }, { label: "Version B: principal * rate passed down" }], items: [
  { text: "The principal in every call stays at 100", b: 0 }, { text: "Call 3 is compoundInt(110.25, 1.05, 1)", b: 1 }, { text: "RETURN column from the base case upwards: 100, 105, 110.25, 115.76", b: 0 }, { text: "RETURN column shows 115.76 in every row", b: 1 }, { text: "The base case returns the original principal", b: 0 }, { text: "The base case returns the final amount", b: 1 }, { text: "The multiplying happens while unwinding", b: 0 }, { text: "The multiplying happens while winding down", b: 1 }], done: "Same answer, 115.7625, from two different routes." });

Lib.match($("#m1"), { prompt: "Match each term to what it means in this function.", pairs: [
  ["Base case", "years = 0, so total is just the principal"], ["General case", "the call that passes years - 1 to compoundInt itself"], ["Winding", "the calls being made, years counting down towards 0"], ["Unwinding", "the calls finishing and returning, in reverse order"], ["rate", "the yearly growth factor, e.g. 1.05 for 5%"], ["Stack frame", "one call's copy of principal, rate, years and its return address"]], done: "Those six ideas are all you need to explain this function." });

/* ===== Practise ===== */
Lib.calc($("#c1"), { qs: [
  { q: "Trace compoundInt(200, 1.1, 3) (Version A). What does the <b>base-case</b> call, years = 0, return?", a: 200, hint: "years = 0, so total is the principal.", sol: "total ← principal = 200." },
  { q: "What does compoundInt(200, 1.1, 1) return?", a: 220, hint: "It multiplies what the base case returned by the rate.", sol: "200 × 1.1 = 220." },
  { q: "What does compoundInt(200, 1.1, 2) return?", a: 242, hint: "Take the previous answer × 1.1.", sol: "220 × 1.1 = 242." },
  { q: "What does the original call compoundInt(200, 1.1, 3) return?", a: 266.2, tol: 0.01, hint: "Take the previous answer × 1.1.", sol: "242 × 1.1 = 266.2." },
  { q: "How many calls to compoundInt are made in total for compoundInt(200, 1.1, 3), counting the first and the base case?", a: 4, tol: 0, hint: "years = 3, 2, 1, 0.", sol: "years goes 3, 2, 1, 0: four calls." },
  { q: "A bank pays 8% a year. What value should be passed as rate?", a: 1.08, tol: 0.001, hint: "rate is the growth factor, not the percentage.", sol: "100% + 8% = 108% = 1.08." },
  { q: "compoundInt(500, 1.08, 5) to the nearest 0.01 (a calculator helps).", a: 734.66, tol: 0.011, hint: "500 × 1.08, five times over.", sol: "500 × 1.08⁵ = 734.66 (734.664…)." }] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What is the base case of compoundInt?", opts: ["years = 0, which returns the principal", "rate = 1, which returns the principal", "principal = 0, which returns 0", "years = 1, which returns principal * rate"], a: 0, why: "When years is 0 no interest has been added, so the total is just the principal." },
  { q: "How many times is compoundInt called by compoundInt(100, 1.05, 4), counting the first call?", opts: ["4", "5", "6", "1"], a: 1, why: "years takes the values 4, 3, 2, 1 and 0. The base case call counts, so 5 calls." },
  { q: "In Version A, when are the multiplications by rate carried out?", opts: ["On the way down, before each call", "Only in the base case", "On the way back up, as each call returns", "Before the function starts"], a: 2, why: "total ← compoundInt(…) * rate cannot be worked out until the inner call has returned." },
  { q: "The recursive line is changed to compoundInt(principal, rate, years + 1) * rate. What happens when it is called with years = 3?", opts: ["It returns the right answer", "It returns 0", "It never reaches the base case and the stack overflows", "It returns the principal"], a: 2, why: "years moves away from 0, so the base case is never reached. Every call adds a frame until the stack runs out." },
  { q: "The base case is changed to return 0 instead of principal. What does compoundInt(100, 1.05, 3) return?", opts: ["115.7625", "100", "105", "0"], a: 3, why: "0 × 1.05 × 1.05 × 1.05 = 0. The program runs, but gives the wrong answer." },
  { q: "Which argument is correct for 3.5% interest?", opts: ["3.5", "0.035", "1.035", "35"], a: 2, why: "The rate is the growth factor: 1 + 0.035 = 1.035." },
  { q: "In Table 19.29 style, a row labelled “2 cont” shows…", opts: ["call 2 being made for the first time", "call 2 resuming after the call below it returned", "the base case", "an error"], a: 1, why: "“cont” rows are the unwinding rows: the call carries on from where it paused and finishes." }] });

Lib.cards($("#fc1"), { cards: [
  ["Base case", "The input for which the answer is known without a further call. Here: years = 0, total = principal. Also called the terminating condition."],
  ["General case", "The branch where the function calls itself with a simpler value (years - 1)."],
  ["Winding", "The phase where calls are made, one after another, and frames are pushed, until the base case is reached."],
  ["Unwinding", "The phase after the base case where each call returns and its frame is popped, in reverse order."],
  ["Stack frame", "The block pushed on the call stack for each call: parameters, local variables and the return address."],
  ["Return address", "Where the program carries on once a call finishes."],
  ["Trace table", "A table that records the calls, parameter values and returned values step by step."],
  ["Growth factor (rate)", "The number the amount is multiplied by each year: 1.05 for 5% interest."],
  ["Stack overflow", "An error when the call stack runs out of memory, for example because the base case is never reached."],
  ["Compound interest", "Interest calculated on the principal plus the interest already added, so each year’s growth is bigger than the last."],
  ["Iteration", "Repeating with a loop (FOR, WHILE) instead of the subroutine calling itself."]] });

Lib.codePanel($("#codeA"), { pseudo: PS_A, py: PY_A });
