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
const DBT = {"CUSTOMER": {"cols": ["CustomerID", "FirstName", "LastName", "Town"], "rows": [["HJ231", "Ana", "Lopez", "Leeds"], ["KM455", "Ben", "Okoye", "York"], ["PQ802", "Cleo", "Zhang", "Leeds"]]}, "SHOP_ORDER": {"cols": ["OrderNo", "CustomerID", "OrderDate"], "rows": [[1001, "HJ231", "02/03/2024"], [1002, "HJ231", "09/03/2024"], [1003, "KM455", "10/03/2024"]]}, "ITEM": {"cols": ["ItemNumber", "Description", "Price"], "rows": [["A1", "Lamp", 12.5], ["B2", "Desk", 80], ["C3", "Chair", 35]]}, "ORDER_ITEM": {"cols": ["ItemNumber", "OrderNo", "Quantity"], "rows": [["A1", 1001, 2], ["B2", 1001, 1], ["C3", 1002, 4], ["A1", 1003, 1]]}};
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["Ana", "Leeds"], ["Ben", "York"], ["Cleo", "Leeds"]]; let o = SV.text(20, 20, "customers", "sm"); rows.forEach((r, i) => { const keep = k >= 1 ? r[1] === "Leeds" : true; o += SV.rect(20, 32 + i * 30, 220, 24, keep ? (k >= 2 ? "f1" : "f3") : "cell", { rx: 4, ...(keep ? {} : op(0.35)) }) + SV.text(30, 49 + i * 30, r.join("   "), "lbl", { style: "font-size:12px" }); });
    if (k >= 2) o += SV.rect(300, 32, 120, 24, "f1", { rx: 4 }) + SV.text(310, 49, "Ana", "lbl bd") + SV.rect(300, 62, 120, 24, "f1", { rx: 4 }) + SV.text(310, 79, "Cleo", "lbl bd") + SV.text(300, 24, "result", "sm"); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 130, label: "SELECT", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["FROM CUSTOMER: all the rows.", "WHERE keeps only the rows where Town is Leeds.", "SELECT shows just the FirstName of those rows."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["HJ231", 2], ["HJ231", 1], ["KM455", 5], ["HJ231", 4]]; let o = ""; rows.forEach((r, i) => o += SV.rect(20, 14 + i * 28, 200, 24, k >= 1 ? (r[0] === "HJ231" ? "f1" : "f3") : "cell", { rx: 4 }) + SV.text(30, 31 + i * 28, r[0] + "   " + r[1], "lbl", { style: "font-size:12px" }));
    if (k >= 2) o += SV.rect(300, 14, 200, 24, "f1", { rx: 4 }) + SV.text(310, 31, "HJ231   SUM = 7", "lbl bd") + SV.rect(300, 44, 200, 24, "f3", { rx: 4 }) + SV.text(310, 61, "KM455   SUM = 5", "lbl bd"); o += SV.text(20, 135, ["rows of ORDER_ITEM", "GROUP BY CustomerID puts rows with the same ID together", "SUM(Quantity) is worked out for each group: one row per customer"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 155, label: "GROUP BY", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Order lines with a CustomerID and a Quantity.", "<b>GROUP BY</b> groups the rows by CustomerID.", "<b>SUM(Quantity)</b> is calculated for each group."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 190, 30, on ? "f3" : "cell", { rx: 5 }) + SV.text(x + 95, y + 19, t, "lbl", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, 20, "SHOP_ORDER: 1001, HJ231", true) + B(300, 20, "ORDER_ITEM: A1, 1001, 2", true) + B(20, 60, "SHOP_ORDER: 1002, HJ231", true) + B(300, 60, "ORDER_ITEM: C3, 1002, 4", true);
    if (k >= 1) o += SV.path("M210,35 H300", "ax") + SV.path("M210,75 H300", "ax"); o += SV.text(20, 120, ["two tables", "ON matches OrderNo in both tables", "joined rows can be filtered and totalled"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 140, label: "Join", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Order numbers are in both tables.", "<b>INNER JOIN ... ON</b> matches rows with the same OrderNo.", "The joined rows can be filtered and totalled."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#dml", DBT, 'SELECT CUSTOMER.FirstName, SUM(Quantity) AS TotalItems\nFROM CUSTOMER, SHOP_ORDER, ORDER_ITEM\nWHERE CUSTOMER.CustomerID = SHOP_ORDER.CustomerID\nAND SHOP_ORDER.OrderNo = ORDER_ITEM.OrderNo\nGROUP BY CUSTOMER.FirstName\nORDER BY TotalItems DESC;', { rows: 8 });
btnTable("cB", "cO", [
  ["Show only customers from Leeds", "WHERE Town = \"Leeds\"", "A condition"],
  ["Show each customer's total", "GROUP BY CustomerID with SUM", "One row per group"],
  ["Largest total first", "ORDER BY Total DESC", "Descending sort"],
  ["Use fields from two tables", "INNER JOIN ... ON keys", "Match foreign and primary keys"],
  ["Give the total a heading", "SUM(Quantity) AS TotalItems", "AS names the result"]
], ["Need", "SQL", "Why"]);
btnTable("fB", "fO", [
  ["How many orders has a customer placed?", "COUNT(OrderNo)", "A number of records"],
  ["How many items in total were ordered?", "SUM(Quantity)", "A total"],
  ["What is the mean price?", "AVG(Price)", "An average"],
  ["How many containers on a ship?", "COUNT(ContainerID)", "A number of records"]
], ["Question", "Function", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which clause does the job?", buckets: [{"label": "SELECT"}, {"label": "WHERE"}, {"label": "GROUP BY"}, {"label": "ORDER BY"}, {"label": "INNER JOIN"}], items: [{"text": "Chooses the fields to return", "b": 0}, {"text": "Keeps only the rows that match a condition", "b": 1}, {"text": "Makes one row per customer", "b": 2}, {"text": "Sorts the results in descending order", "b": 3}, {"text": "Links two tables on their keys", "b": 4}, {"text": "Contains the condition Paid = FALSE", "b": 1}], done: "Match the job." });
Lib.classify($("#cl2"), { prompt: "Which function does the question need?", buckets: [{"label": "COUNT"}, {"label": "SUM"}, {"label": "AVG"}], items: [{"text": "The number of records for a customer", "b": 0}, {"text": "The total cost of the unpaid orders", "b": 1}, {"text": "The average mark in test A7", "b": 2}, {"text": "How many containers are on a ship", "b": 0}, {"text": "The total quantity of items ordered", "b": 1}, {"text": "The mean age of the horses", "b": 2}], done: "Number: COUNT. Total: SUM. Mean: AVG." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["SELECT ... FROM ... WHERE", "Search for matching records"], ["INSERT INTO ... VALUES", "Add a record"], ["UPDATE ... SET ... WHERE", "Change existing records"], ["DELETE FROM ... WHERE", "Remove records"], ["ORDER BY ... DESC", "Sort largest first"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the SELECT clauses in order.", items: ["SELECT the fields", "FROM the tables", "WHERE the condition", "GROUP BY the grouping field", "ORDER BY the sort field"], done: "SELECT, FROM, WHERE, GROUP BY, ORDER BY." });
Lib.calc($("#c1"), { qs: [
  {"q": "Quantities ordered by customer HJ231 are 2, 1 and 4. What does SUM(Quantity) return?", "a": 7, "unit": "", "tol": 0.01, "hint": "2 + 1 + 4.", "sol": "<b>7</b>."},
  {"q": "The same customer has 3 order lines. What does COUNT(Quantity) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "Number of rows.", "sol": "<b>3</b>."},
  {"q": "Marks in test A7 are 40, 60 and 80. What does AVG(Mark) return?", "a": 60, "unit": "", "tol": 0.01, "hint": "180 ÷ 3.", "sol": "<b>60</b>."},
  {"q": "A table has 12 rows. Without WHERE, DELETE FROM table removes how many rows?", "a": 12, "unit": "", "tol": 0.01, "hint": "All.", "sol": "<b>12</b>."},
  {"q": "SELECT with GROUP BY CustomerID on 3 customers returns how many rows?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per group.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "SELECT chooses:", opts: ["The fields to show", "The table", "The key", "The data type"], a: 0, why: "Fields." },
  { q: "WHERE adds:", opts: ["A condition", "A new table", "A key", "A sort"], a: 0, why: "Condition." },
  { q: "COUNT returns:", opts: ["The number of records", "The total", "The average", "The largest"], a: 0, why: "Number." },
  { q: "UPDATE without WHERE changes:", opts: ["Every record", "No records", "One record", "Only keys"], a: 0, why: "All." },
  { q: "A join links tables using:", opts: ["Primary and foreign keys", "Field lengths", "Passwords", "Dates"], a: 0, why: "Keys." },
  { q: "ORDER BY x DESC sorts:", opts: ["Largest first", "Smallest first", "Randomly", "By length"], a: 0, why: "Descending." },
] });
Lib.cards($("#fc1"), { cards: [
  ["SELECT ... FROM ... WHERE", "Search."],
  ["INNER JOIN ... ON", "Match foreign and primary keys."],
  ["GROUP BY", "One row per group."],
  ["ORDER BY ... DESC", "Sort descending."],
  ["COUNT / SUM / AVG", "Number / total / mean."],
  ["INSERT INTO ... VALUES", "Add a record."],
  ["UPDATE ... SET ... WHERE", "Change records."],
  ["DELETE FROM ... WHERE", "Remove records."],
] });
