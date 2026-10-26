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

/* ---- a small SQL engine: SELECT (joins, WHERE, GROUP BY, ORDER BY, aggregates), INSERT, UPDATE, DELETE, CREATE TABLE/DATABASE, ALTER TABLE ---- */
const SQL = (function () {
  function tok(s) {
    const t = []; let i = 0;
    while (i < s.length) { const c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if (c === "'" || c === '"') { let j = i + 1, v = ""; while (j < s.length && s[j] !== c) v += s[j++]; t.push({ k: "s", v }); i = j + 1; continue; }
      if (c === "#") { let j = i + 1, v = ""; while (j < s.length && s[j] !== "#") v += s[j++]; t.push({ k: "s", v }); i = j + 1; continue; }
      if (/[0-9]/.test(c)) { let j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++; t.push({ k: "n", v: parseFloat(s.slice(i, j)) }); i = j; continue; }
      if (/[A-Za-z_]/.test(c)) { let j = i; while (j < s.length && /[A-Za-z0-9_.]/.test(s[j])) j++; t.push({ k: "w", v: s.slice(i, j) }); i = j; continue; }
      const two = s.slice(i, i + 2); if (["<=", ">=", "<>", "!=", "=="].includes(two)) { t.push({ k: "o", v: two }); i += 2; continue; }
      t.push({ k: "o", v: c }); i++; }
    return t;
  }
  const U = (x) => String(x).toUpperCase();
  function P(toks) { let p = 0; const peek = () => toks[p], next = () => toks[p++]; const isW = (w) => peek() && peek().k === "w" && U(peek().v) === w; const eatW = (w) => { if (isW(w)) { p++; return true; } return false; }; const isO = (o) => peek() && peek().k === "o" && peek().v === o; const eatO = (o) => { if (isO(o)) { p++; return true; } return false; };
    const need = (w) => { if (!eatW(w)) throw new Error("Expected " + w + (peek() ? " near '" + peek().v + "'" : " at the end")); };
    const needO = (o) => { if (!eatO(o)) throw new Error("Expected '" + o + "'" + (peek() ? " near '" + peek().v + "'" : " at the end")); };
    function value() { const t = next(); if (!t) throw new Error("Unexpected end"); if (t.k === "n") return { c: "lit", v: t.v }; if (t.k === "s") return { c: "lit", v: t.v }; if (t.k === "w") { const u = U(t.v); if (u === "TRUE") return { c: "lit", v: true }; if (u === "FALSE") return { c: "lit", v: false }; if (u === "NULL") return { c: "lit", v: null }; if (["COUNT", "SUM", "AVG", "MIN", "MAX"].includes(u) && isO("(")) { next(); let arg; if (eatO("*")) arg = { c: "star" }; else arg = value(); needO(")"); return { c: "agg", f: u, a: arg }; } return { c: "col", n: t.v }; } if (t.k === "o" && t.v === "(") { const e = cond(); needO(")"); return e; } if (t.k === "o" && t.v === "-") { const v = value(); return { c: "lit", v: -v.v }; } throw new Error("Unexpected '" + t.v + "'"); }
    function cmp() { if (eatW("NOT")) return { c: "not", a: cmp() }; const a = value(); if (peek() && peek().k === "o" && ["=", "<", ">", "<=", ">=", "<>", "!=", "=="].includes(peek().v)) { const op = next().v; return { c: "cmp", op, a, b: value() }; } if (eatW("LIKE")) return { c: "like", a, b: value() }; if (eatW("BETWEEN")) { const lo = value(); need("AND"); const hi = value(); return { c: "between", a, lo, hi }; } if (eatW("IN")) { needO("("); const l = []; do { l.push(value()); } while (eatO(",")); needO(")"); return { c: "in", a, l }; } if (eatW("IS")) { const n = eatW("NOT"); need("NULL"); return { c: "isnull", a, n }; } return a; }
    function and() { let l = cmp(); while (eatW("AND")) l = { c: "and", a: l, b: cmp() }; return l; }
    function cond() { let l = and(); while (eatW("OR")) l = { c: "or", a: l, b: and() }; return l; }
    function selectStmt() { const q = { t: "select", items: [], from: [], joins: [] }; q.distinct = eatW("DISTINCT"); do { if (eatO("*")) q.items.push({ e: { c: "star" } }); else { const e = value(); let al = null; if (eatW("AS")) { const a = next(); al = a.v; } q.items.push({ e, al }); } } while (eatO(",")); need("FROM"); q.from.push(next().v); while (true) { if (eatO(",")) { q.from.push(next().v); continue; } if (eatW("INNER") || eatW("JOIN")) { eatW("JOIN"); const tn = next().v; need("ON"); q.joins.push({ t: tn, on: cond() }); continue; } break; } if (eatW("WHERE")) q.where = cond(); if (eatW("GROUP")) { need("BY"); q.group = []; do { q.group.push(value()); } while (eatO(",")); } if (eatW("ORDER")) { need("BY"); q.order = []; do { const e = value(); let d = false; if (eatW("DESC")) d = true; else eatW("ASC"); q.order.push({ e, d }); } while (eatO(",")); } return q; }
    return { selectStmt, cond, value, need, needO, eatW, eatO, isW, peek, next, done: () => p >= toks.length, pos: () => p, toks };
  }
  function cellVal(r, name, tabs) { const n = name.toLowerCase(); if (n.includes(".")) { const [t, c] = n.split("."); const k = r[t + "." + c]; if (k !== undefined || (t + "." + c) in r) return r[t + "." + c]; throw new Error("Unknown column " + name); } let hit = null, cnt = 0; for (const k in r) { if (k.split(".")[1] === n) { hit = k; cnt++; } } if (cnt === 0) throw new Error("Unknown column " + name); return r[hit]; }
  function ev(e, r, db) { switch (e.c) { case "lit": return e.v; case "col": return cellVal(r, e.n); case "and": return ev(e.a, r) && ev(e.b, r); case "or": return ev(e.a, r) || ev(e.b, r); case "not": return !ev(e.a, r);
      case "cmp": { let a = ev(e.a, r), b = ev(e.b, r); if (typeof a === "boolean" || typeof b === "boolean") { a = norm(a); b = norm(b); } else if (typeof a === "string" && typeof b === "string") { const da = Date.parse(dfmt(a)), db2 = Date.parse(dfmt(b)); if (!isNaN(da) && !isNaN(db2) && /\d\/\d|\d-\d/.test(a) && /\d\/\d|\d-\d/.test(b)) { a = da; b = db2; } else { a = a.toLowerCase(); b = b.toLowerCase(); } } const o = e.op; return o === "=" || o === "==" ? a === b : o === "<>" || o === "!=" ? a !== b : o === "<" ? a < b : o === ">" ? a > b : o === "<=" ? a <= b : a >= b; }
      case "like": { const a = String(ev(e.a, r)), pat = String(ev(e.b, r)); const rx = new RegExp("^" + pat.replace(/[.+?^${}()|[\]\\]/g, "\\$&").replace(/[%*]/g, ".*").replace(/_/g, ".") + "$", "i"); return rx.test(a); }
      case "between": { const a = ev(e.a, r), lo = ev(e.lo, r), hi = ev(e.hi, r); return a >= lo && a <= hi; } case "in": { const a = ev(e.a, r); return e.l.some((x) => ev(x, r) === a); } case "isnull": { const a = ev(e.a, r); const n = a === null || a === undefined || a === ""; return e.n ? !n : n; } default: throw new Error("Cannot evaluate"); } }
  const norm = (x) => (typeof x === "boolean" ? x : typeof x === "string" ? ["yes", "true", "y"].includes(x.toLowerCase()) : !!x);
  function dfmt(s) { const m = s.match(/^(\d\d)\/(\d\d)\/(\d{4})$/); return m ? m[3] + "-" + m[2] + "-" + m[1] : s; }
  function aggs(e, out) { if (!e) return; if (e.c === "agg") out.push(e); else for (const k of ["a", "b", "lo", "hi"]) if (e[k] && typeof e[k] === "object") aggs(e[k], out); }
  function exprName(e) { return e.c === "col" ? e.n.split(".").pop() : e.c === "agg" ? e.f + "(" + (e.a.c === "star" ? "*" : e.a.n || "") + ")" : e.c === "lit" ? String(e.v) : "expr"; }
  function evalAgg(e, rows) { if (e.c === "agg") { if (e.a.c === "star") return rows.length; const v = rows.map((r) => ev(e.a, r)).filter((x) => x !== null && x !== undefined && x !== ""); if (e.f === "COUNT") return v.length; if (!v.length) return null; if (e.f === "SUM") return Math.round(v.reduce((a, b) => a + Number(b), 0) * 1e6) / 1e6; if (e.f === "AVG") return Math.round(v.reduce((a, b) => a + Number(b), 0) / v.length * 1e6) / 1e6; if (e.f === "MIN") return v.reduce((a, b) => (a < b ? a : b)); return v.reduce((a, b) => (a > b ? a : b)); } return ev(e, rows[0] || {}); }
  function tbl(db, n) { const k = Object.keys(db.tables).find((x) => x.toLowerCase() === n.toLowerCase()); if (!k) throw new Error("No table named " + n); return db.tables[k]; }
  function rowsOf(db, name) { const t = tbl(db, name); const nm = name.toLowerCase(); return t.rows.map((r) => { const o = {}; t.cols.forEach((c, i) => (o[nm + "." + c.toLowerCase()] = r[i])); return o; }); }
  function run(db, sql) {
    sql = sql.trim().replace(/;+\s*$/, ""); const P0 = P(tok(sql)); const first = P0.peek() && U(P0.peek().v);
    if (first === "SELECT") { P0.next(); const q = P0.selectStmt(); if (!P0.done()) throw new Error("Unexpected '" + P0.peek().v + "'"); return select(db, q); }
    if (first === "INSERT") { P0.next(); P0.need("INTO"); const tn = P0.next().v; const t = tbl(db, tn); let cols = null; if (P0.eatO("(")) { cols = []; do { cols.push(P0.next().v); } while (P0.eatO(",")); P0.needO(")"); } P0.need("VALUES"); P0.needO("("); const vals = []; do { vals.push(P0.value().v); } while (P0.eatO(",")); P0.needO(")"); const row = t.cols.map(() => null); (cols || t.cols).forEach((c, i) => { const ix = t.cols.findIndex((x) => x.toLowerCase() === c.toLowerCase()); if (ix < 0) throw new Error("No column " + c); row[ix] = vals[i]; }); if (vals.length !== (cols || t.cols).length) throw new Error("The number of values does not match the number of columns"); t.rows.push(row); return { msg: "1 row inserted into " + tn + "." }; }
    if (first === "DELETE") { P0.next(); P0.need("FROM"); const tn = P0.next().v; const t = tbl(db, tn); let w = null; if (P0.eatW("WHERE")) w = P0.cond(); const keep = [], before = t.rows.length; const all = rowsOf(db, tn); t.rows = t.rows.filter((r, i) => !(w ? ev(w, all[i]) : true)); return { msg: before - t.rows.length + " row(s) deleted from " + tn + "." }; }
    if (first === "UPDATE") { P0.next(); const tn = P0.next().v; const t = tbl(db, tn); P0.need("SET"); const sets = []; do { const c = P0.next().v; P0.needO("="); sets.push([c, P0.value()]); } while (P0.eatO(",")); let w = null; if (P0.eatW("WHERE")) w = P0.cond(); const all = rowsOf(db, tn); let n = 0; t.rows.forEach((r, i) => { if (!w || ev(w, all[i])) { sets.forEach(([c, v]) => { const ix = t.cols.findIndex((x) => x.toLowerCase() === c.toLowerCase()); if (ix < 0) throw new Error("No column " + c); r[ix] = ev(v, all[i]); }); n++; } }); return { msg: n + " row(s) updated in " + tn + "." }; }
    if (first === "CREATE") { P0.next(); if (P0.eatW("DATABASE")) { const n = P0.next().v; return { msg: "Database " + n + " created." }; } P0.need("TABLE"); const tn = P0.next().v; P0.needO("("); const cols = []; while (true) { if (P0.isW("PRIMARY") || P0.isW("FOREIGN")) { let d = 0; while (!P0.done()) { const t = P0.peek(); if (t.v === "(") d++; if (t.v === ")") { if (d === 0) break; d--; } if (t.v === "," && d === 0) break; P0.next(); } } else { const c = P0.next().v; cols.push(c); let d = 0; while (!P0.done()) { const t = P0.peek(); if (t.v === "(") d++; if (t.v === ")") { if (d === 0) break; d--; } if (t.v === "," && d === 0) break; P0.next(); } } if (!P0.eatO(",")) break; } P0.needO(")"); db.tables[tn] = { cols, rows: [] }; return { msg: "Table " + tn + " created with " + cols.length + " column(s)." }; }
    if (first === "ALTER") { P0.next(); P0.need("TABLE"); const tn = P0.next().v; const t = tbl(db, tn); P0.need("ADD"); if (P0.isW("FOREIGN") || P0.isW("PRIMARY")) return { msg: "Key added to " + tn + "." }; const added = []; do { const c = P0.next().v; added.push(c); while (!P0.done() && !(P0.peek().v === ",")) P0.next(); } while (P0.eatO(",")); added.forEach((c) => { t.cols.push(c); t.rows.forEach((r) => r.push(null)); }); return { msg: "Added " + added.join(", ") + " to " + tn + "." }; }
    throw new Error("Not a statement I can run: start with SELECT, INSERT, UPDATE, DELETE, CREATE or ALTER.");
  }
  function select(db, q) {
    let rows = rowsOf(db, q.from[0]); for (let i = 1; i < q.from.length; i++) { const r2 = rowsOf(db, q.from[i]); const out = []; rows.forEach((a) => r2.forEach((b) => out.push(Object.assign({}, a, b)))); rows = out; }
    q.joins.forEach((j) => { const r2 = rowsOf(db, j.t); const out = []; rows.forEach((a) => r2.forEach((b) => { const m = Object.assign({}, a, b); if (ev(j.on, m)) out.push(m); })); rows = out; });
    if (q.where) rows = rows.filter((r) => ev(q.where, r));
    const hasAgg = q.items.some((it) => { const o = []; aggs(it.e, o); return o.length; });
    let cols, res;
    const expand = () => { const cs = [], ex = []; q.items.forEach((it) => { if (it.e.c === "star") { q.from.concat(q.joins.map((j) => j.t)).forEach((tn) => tbl(db, tn).cols.forEach((c) => { cs.push(c); ex.push({ c: "col", n: tn + "." + c }); })); } else { cs.push(it.al || exprName(it.e)); ex.push(it.e); } }); return [cs, ex]; };
    const resolve = (e) => { if (e.c === "col" && !e.n.includes(".")) { const it = q.items.find((x) => x.al && x.al.toLowerCase() === e.n.toLowerCase()); if (it) return it.e; } return e; };
    if (hasAgg || q.group) {
      const groups = new Map(); rows.forEach((r) => { const key = (q.group || []).map((g) => String(ev(g, r))).join("|"); if (!groups.has(key)) groups.set(key, []); groups.get(key).push(r); }); if (!q.group && !groups.size) groups.set("", []);
      const [cs, ex] = expand(); cols = cs; res = [...groups.values()].map((g) => ({ vals: ex.map((e) => evalAgg(e, g)), sample: g[0] || {}, grp: g }));
      if (q.order) res.sort((A, B) => { for (const o of q.order) { const oe = resolve(o.e); const a = oe.c === "agg" ? evalAgg(oe, A.grp) : ev(oe, A.sample), b = oe.c === "agg" ? evalAgg(oe, B.grp) : ev(oe, B.sample); if (a < b) return o.d ? 1 : -1; if (a > b) return o.d ? -1 : 1; } return 0; });
      res = res.map((x) => x.vals);
    } else {
      if (q.order) rows = rows.slice().sort((A, B) => { for (const o of q.order) { const oe = resolve(o.e); const a = ev(oe, A), b = ev(oe, B); if (a < b) return o.d ? 1 : -1; if (a > b) return o.d ? -1 : 1; } return 0; });
      const [cs, ex] = expand(); cols = cs; res = rows.map((r) => ex.map((e) => ev(e, r)));
    }
    if (q.distinct) { const seen = new Set(); res = res.filter((r) => { const k = JSON.stringify(r); if (seen.has(k)) return false; seen.add(k); return true; }); }
    return { cols, rows: res };
  }
  return { run };
})();
function sqlLab(el, tables, start, opts) {
  opts = opts || {}; const root = typeof el === "string" ? $(el) : el; const db = { tables: JSON.parse(JSON.stringify(tables)) }; const orig = JSON.stringify(tables);
  root.innerHTML = '<div data-sch></div><textarea data-q rows="' + (opts.rows || 5) + '" style="width:100%;font:13px/1.4 ui-monospace,Menlo,monospace;padding:8px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:inherit" spellcheck="false"></textarea><div class="btnrow"><button data-run>Run</button><button data-reset>Reset the database</button></div><div data-out></div>';
  const q = root.querySelector("[data-q]"), out = root.querySelector("[data-out]"), sch = root.querySelector("[data-sch]"); q.value = start || "";
  const fmt = (v) => (v === null || v === undefined ? "NULL" : v === true ? "TRUE" : v === false ? "FALSE" : v);
  const showTables = () => { sch.innerHTML = '<p class="note" style="margin:0 0 6px">Tables: ' + Object.entries(db.tables).map(([n, t]) => "<b>" + n + "</b>(" + t.cols.join(", ") + ") " + t.rows.length + " rows").join(" · ") + "</p>"; };
  const go = () => { try { const r = SQL.run(db, q.value); if (r.cols) { out.innerHTML = '<div class="tw"><table class="t mono"><tr>' + r.cols.map((c) => "<th>" + c + "</th>").join("") + "</tr>" + r.rows.map((x) => "<tr>" + x.map((v) => "<td>" + fmt(v) + "</td>").join("") + "</tr>").join("") + "</table></div><p class=\"note\">" + r.rows.length + " row(s)</p>"; } else out.innerHTML = '<div class="verdict">' + r.msg + "</div>"; showTables(); } catch (e) { out.innerHTML = '<div class="verdict" style="border-color:var(--bad)"><b>Error:</b> ' + e.message + "</div>"; } };
  root.querySelector("[data-run]").onclick = go; root.querySelector("[data-reset]").onclick = () => { db.tables = JSON.parse(orig); showTables(); out.innerHTML = ""; };
  showTables(); if (opts.auto !== false && start) go();
}
const DBT = {"CUSTOMER": {"cols": ["CustomerID", "FirstName", "LastName", "Town"], "rows": [["HJ231", "Ana", "Lopez", "Leeds"], ["KM455", "Ben", "Okoye", "York"], ["PQ802", "Cleo", "Zhang", "Leeds"]]}, "SHOP_ORDER": {"cols": ["OrderNo", "CustomerID", "OrderDate"], "rows": [[1001, "HJ231", "02/03/2024"], [1002, "HJ231", "09/03/2024"], [1003, "KM455", "10/03/2024"]]}};

(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = ["Ana  Lopez  12 High St  order: chair", "Ana  Lopez  12 High St  order: desk", "Ana  Lopez  12 High St  order: lamp"]; let o = SV.text(20, 18, k === 0 ? "File-based: the address is repeated in every order" : "Relational: the address is stored once", "lbl bd", { style: "font-size:13px" });
    if (k === 0) rows.forEach((r, i) => o += SV.rect(20, 30 + i * 30, 480, 24, i === 1 ? "f2" : "cell", { rx: 4 }) + SV.text(30, 47 + i * 30, r, "lbl", { style: "font-size:12px" })); else { o += SV.rect(20, 30, 220, 28, "f1", { rx: 4 }) + SV.text(30, 49, "CUSTOMER: Ana Lopez, 12 High St", "lbl", { style: "font-size:12px" }); ["chair", "desk", "lamp"].forEach((r, i) => o += SV.rect(280, 30 + i * 30, 220, 24, "cell", { rx: 4 }) + SV.text(290, 47 + i * 30, "ORDER: " + r + " (CustomerID)", "lbl", { style: "font-size:12px" })); }
    return o; };
  Lib.stepper($("#stA"), { w: 520, h: 130, label: "Redundancy", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["In a file the address is stored again for every order: <b>redundancy</b>. If it changes, one copy may be missed: <b>inconsistency</b>.", "In a relational database the address is stored <b>once</b> in CUSTOMER and each order links to it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 18, "CUSTOMER", "lbl bd") + SV.text(300, 18, "SHOP_ORDER", "lbl bd");
    [["HJ231", "Ana"], ["KM455", "Ben"]].forEach(([id, n], i) => o += SV.rect(20, 28 + i * 34, 210, 28, k >= 1 && i === 0 ? "f3" : "cell", { rx: 4 }) + SV.text(30, 47 + i * 34, id + "  " + n + "   (PK: CustomerID)", "lbl", { style: "font-size:12px" }));
    [[1001, "HJ231"], [1002, "HJ231"], [1003, "KM455"]].forEach(([n, c], i) => o += SV.rect(300, 28 + i * 34, 220, 28, k >= 1 && c === "HJ231" ? "f3" : "cell", { rx: 4 }) + SV.text(310, 47 + i * 34, n + "  " + c + "   (FK)", "lbl", { style: "font-size:12px" }));
    o += SV.text(20, 150, ["", "CustomerID is the primary key in CUSTOMER", "and a foreign key in SHOP_ORDER: one customer, many orders"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 170, label: "Keys", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Two linked tables.", "<b>CustomerID</b> is the <b>primary key</b> in CUSTOMER.", "It is a <b>foreign key</b> in SHOP_ORDER, giving a <b>one-to-many</b> relationship."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 130, 34, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + 65, y + 22, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, 40, "ORDER", true) + B(390, 40, "PRODUCT", true);
    if (k === 0) o += SV.path("M150,57 H390", "ax") + SV.text(270, 50, "many : many", "sm", { "text-anchor": "middle" }); else { o += B(205, 40, "ORDER_ITEM", true) + SV.path("M150,57 H205", "ax") + SV.path("M335,57 H390", "ax") + SV.text(177, 50, "1:M", "sm", { "text-anchor": "middle" }) + SV.text(362, 50, "M:1", "sm", { "text-anchor": "middle" }); }
    o += SV.text(20, 110, ["cannot be directly implemented", "a linking table with both keys: two one-to-many relationships", "ORDER_ITEM(OrderNo, ItemNumber, Quantity): composite primary key"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 540, h: 130, label: "Linking table", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["An order has many products and a product is in many orders: <b>many-to-many</b>.", "A <b>linking table</b> holds the primary keys of both as foreign keys.", "The pair of keys forms a <b>composite primary key</b>; each side is now one-to-many."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#dbLab", DBT, "SELECT CUSTOMER.FirstName, SHOP_ORDER.OrderNo\nFROM CUSTOMER INNER JOIN SHOP_ORDER\nON CUSTOMER.CustomerID = SHOP_ORDER.CustomerID;", { rows: 4 });
btnTable("rB", "rO", [
  ["Customer and the login details they have", "One-to-one", "Each customer has one set of login details"],
  ["Customer and the orders they place", "One-to-many", "Many orders for one customer"],
  ["Order and the products it contains", "Many-to-many", "Needs a linking table"],
  ["Ship and the containers it carries", "One-to-many", "ShipID is a foreign key in CONTAINER"],
  ["Character and the items they buy", "Many-to-many", "Linking table CHARACTER_ITEM"]
], ["Situation", "Relationship", "Why"]);
btnTable("kB", "kO", [
  ["CustomerID in CUSTOMER", "Primary key", "Identifies each customer"],
  ["CustomerID in SHOP_ORDER", "Foreign key", "Links to CUSTOMER"],
  ["(ActorID, FilmID) in FILM_ACTOR", "Composite primary key", "Neither is unique alone"],
  ["SerialNumber in TELESCOPE", "Candidate key", "Could be the primary key"],
  ["OrderNo in ORDER_ITEM", "Part of the key and a foreign key", "Links to the order"]
], ["Field", "Kind of key", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which term does the description give?", buckets: [{"label": "Field"}, {"label": "Record (tuple)"}, {"label": "Entity"}, {"label": "Foreign key"}, {"label": "Referential integrity"}], items: [{"text": "A column in a table", "b": 0}, {"text": "A row in a table", "b": 1}, {"text": "Anything data can be stored about", "b": 2}, {"text": "A field linked to a primary key in another table", "b": 3}, {"text": "Every foreign key has a matching primary key", "b": 4}, {"text": "One instance of an entity in a table", "b": 1}], done: "Column: field. Row: record." });
Lib.classify($("#cl2"), { prompt: "Primary key or foreign key (in the table given)?", buckets: [{"label": "Primary key"}, {"label": "Foreign key"}], items: [{"text": "CustomerID in CUSTOMER", "b": 0}, {"text": "CustomerID in SHOP_ORDER", "b": 1}, {"text": "OrderNo in SHOP_ORDER", "b": 0}, {"text": "ShipID in CONTAINER (ShipID is the primary key of SHIP)", "b": 1}, {"text": "ContainerID in CONTAINER", "b": 0}, {"text": "StudentID in PLACEMENT (the key of STUDENT)", "b": 1}], done: "Primary: identifies the record. Foreign: links to another table." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Primary key", "Uniquely identifies each record"], ["Candidate key", "A field that could be the primary key"], ["Composite key", "A primary key made of two or more fields"], ["Linking table", "Removes a many-to-many relationship"], ["Orphaned record", "A record whose foreign key has no matching primary key"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for removing a many-to-many relationship in order.", items: ["Spot a many-to-many relationship (orders and products)", "Create a new linking table (ORDER_ITEM)", "Add the primary key of each table as a foreign key in it", "Make the pair of foreign keys the composite primary key", "The relationship is now two one-to-many relationships"], done: "Spot, create, add keys, composite key, two 1:M." });
Lib.calc($("#c1"), { qs: [
  {"q": "A customer table has 500 customers. If their address is stored in every order record (average 6 orders each), how many times is each address stored? (Answer: copies per customer.)", "a": 6, "unit": "", "tol": 0.01, "hint": "Once per order.", "sol": "<b>6</b>: this redundancy is why the address belongs in CUSTOMER once."},
  {"q": "A table has 8 fields and 40 records. How many data items (cells)?", "a": 320, "unit": "", "tol": 0.01, "hint": "8 × 40.", "sol": "<b>320</b>."},
  {"q": "A table SHIP has 12 rows and each ship carries 10 containers. How many rows in CONTAINER?", "a": 120, "unit": "", "tol": 0.01, "hint": "12 × 10.", "sol": "<b>120</b>."},
  {"q": "How many foreign keys does a linking table between two tables have?", "a": 2, "unit": "", "tol": 0.01, "hint": "One for each table.", "sol": "<b>2</b>."},
  {"q": "Order 1 has 3 items and order 2 has 2 items. How many rows are in the linking table ORDER_ITEM?", "a": 5, "unit": "", "tol": 0.01, "hint": "3 + 2.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A primary key:", opts: ["Uniquely identifies each record", "Links to another table", "Is a column that repeats", "Stores a password"], a: 0, why: "Unique." },
  { q: "A foreign key:", opts: ["Links to another table's primary key", "Is the first field", "Must be a number", "Is a candidate key"], a: 0, why: "Link." },
  { q: "Many-to-many is implemented with:", opts: ["A linking table", "A bigger field", "Two files", "Nothing"], a: 0, why: "Linking table." },
  { q: "A record is:", opts: ["A row", "A column", "A table", "A key"], a: 0, why: "Row." },
  { q: "Referential integrity prevents:", opts: ["Orphaned records", "Typing errors", "Big tables", "Passwords"], a: 0, why: "Orphans." },
  { q: "A flat-file problem is:", opts: ["Data redundancy", "Easy queries", "Linked tables", "Views"], a: 0, why: "Redundancy." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Entity", "Something data is stored about."],
  ["Field", "Column (attribute)."],
  ["Record", "Row (tuple)."],
  ["Primary key", "Unique identifier."],
  ["Foreign key", "Links to a primary key."],
  ["Candidate key", "Could be the primary key."],
  ["Linking table", "Removes many-to-many."],
  ["Referential integrity", "No orphaned records."],
] });
