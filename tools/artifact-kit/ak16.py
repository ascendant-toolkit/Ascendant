"""Shared pieces for the A Level Computer Science (9618) chapter 16 pages (System software): Reverse Polish Notation helpers
(infix <-> RPN, stack traces) and a syntax-diagram drawer. Run a page with: python3 tools/artifact-kit/mk_ac1621.py"""
import re
from ak20 import *
from ak15 import ob, bx

# ---------------------------------------------------------------- RPN

PREC = {"+": 1, "-": 1, "*": 2, "/": 2}
OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b}


def toks(s):
    return re.findall(r"\d+|[A-Za-z]\w*|[()+\-*/^–]", s.replace("–", "-"))


def to_rpn(infix):
    """Shunting-yard, left-associative + - * /."""
    out, st = [], []
    for t in toks(infix):
        if t in PREC:
            while st and st[-1] in PREC and PREC[st[-1]] >= PREC[t]:
                out.append(st.pop())
            st.append(t)
        elif t == "(":
            st.append(t)
        elif t == ")":
            while st[-1] != "(":
                out.append(st.pop())
            st.pop()
        else:
            out.append(t)
    return out + st[::-1]


def rpn_str(r):
    return " ".join(r).replace("-", "–")


def to_infix(r):
    """Infix with brackets only where precedence needs them, as in the mark schemes."""
    st = []
    for t in [x.replace("–", "-") for x in r]:
        if t in PREC:
            b, a = st.pop(), st.pop()
            (ea, pa), (eb, pb) = a, b
            if pa < PREC[t]:
                ea = f"({ea})"
            if pb < PREC[t] or (pb == PREC[t] and t in "-/"):
                eb = f"({eb})"
            st.append((f"{ea} {t} {eb}", PREC[t]))
        else:
            st.append((t, 9))
    return st[0][0].replace("-", "–")


def run(r, env=None):
    """Evaluate an RPN token list. Returns (result, trace) where trace is the stack after each token."""
    env = env or {}
    st, trace = [], []
    for t in [x.replace("–", "-") for x in r]:
        if t in OPS:
            b, a = st.pop(), st.pop()
            v = OPS[t](a, b)
            st.append(int(v) if float(v).is_integer() else v)
        else:
            st.append(env[t] if t in env else int(t))
        trace.append(list(st))
    return st[-1], trace


def rpn_table(r, env=None):
    """Stack drawn as columns, one per token, newest value on top of each column (bottom of the stack at the bottom)."""
    res, tr = run(r, env)
    depth = max(len(s) for s in tr)
    h = '<div class="tw"><table class="t mono stk"><tr>' + "".join(f"<th>{t.replace('-', '–')}</th>" for t in r) + "</tr>"
    for row in range(depth, 0, -1):
        h += "<tr>" + "".join(f"<td>{s[row - 1] if len(s) >= row else ''}</td>" for s in tr) + "</tr>"
    return h + "</table></div>", res


# ---------------------------------------------------------------- syntax diagrams

CWID = 7.8
ARROW = "M0,0 L-7,-3.5 L-7,3.5 Z"


class Nd:
    def __init__(self, w, h, r, fn):
        self.w, self.h, self.r, self.fn = w, h, r, fn

    def svg(self, x, y):
        return self.fn(x, y)


def _arrow(x, y):
    return f'<path class="ax" style="fill:var(--ink)" d="M{x},{y} L{x - 7},{y - 3.5} L{x - 7},{y + 3.5} Z"/>'


def _ln(x1, y1, x2, y2):
    return f'<path class="ax" d="M{x1},{y1} L{x2},{y2}"/>'


def T(text):
    """Terminal: a literal character in a circle-ended box."""
    w = max(34, CWID * len(text) + 18)
    return Nd(w, 30, 15, lambda x, y: f'<rect class="ax" style="fill:var(--surface)" x="{x}" y="{y}" width="{w}" height="30" rx="15"/><text class="lbl" x="{x + w / 2}" y="{y + 20}" text-anchor="middle">{text}</text>')


def R(text):
    """Rule: a named syntax element in a rectangle."""
    w = max(44, CWID * len(text) + 20)
    return Nd(w, 30, 15, lambda x, y: f'<rect class="ax" style="fill:var(--surface)" x="{x}" y="{y}" width="{w}" height="30"/><text class="lbl" x="{x + w / 2}" y="{y + 20}" text-anchor="middle">{text}</text>')


def S(*ns, gap=24):
    ns = list(ns)
    rail = max(n.r for n in ns)
    h = max(rail - n.r + n.h for n in ns)
    w = sum(n.w for n in ns) + gap * (len(ns) - 1)

    def fn(x, y):
        o, cx = "", x
        for i, n in enumerate(ns):
            o += n.svg(cx, y + rail - n.r)
            if i:
                o += _ln(cx - gap, y + rail, cx, y + rail) + _arrow(cx, y + rail)
            cx += n.w
            if i < len(ns) - 1:
                cx += gap
        return o
    return Nd(w, h, rail, fn)


def A(*ns, bypass=False, pad=18, gap=12):
    """Choice. bypass=True adds an empty first branch (the element is optional)."""
    items = ([None] if bypass else []) + list(ns)
    mw = max([n.w for n in items if n] + [0])
    ys, cy = [], 0
    for n in items:
        ys.append(cy)
        cy += (n.h if n else 8) + gap
    h = cy - gap
    rails = [ys[i] + (n.r if n else 4) for i, n in enumerate(items)]
    w = mw + 2 * pad

    def fn(x, y):
        o = _ln(x, y + rails[0], x, y + rails[-1]) + _ln(x + w, y + rails[0], x + w, y + rails[-1])
        for i, n in enumerate(items):
            ry = y + rails[i]
            if n:
                nx = x + pad + (mw - n.w) / 2
                o += n.svg(nx, y + ys[i]) + _ln(x, ry, nx, ry) + _arrow(nx, ry) + _ln(nx + n.w, ry, x + w, ry)
            else:
                o += _ln(x, ry, x + w, ry) + _arrow(x + w, ry)
        return o
    return Nd(w, h, rails[0], fn)


def L(n, pad=14, up=24):
    """Repeat: a return path above the element."""
    w = n.w + 2 * pad
    rail = up + n.r

    def fn(x, y):
        r = y + rail
        o = n.svg(x + pad, y + up) + _ln(x, r, x + pad, r) + _arrow(x + pad, r) + _ln(x + pad + n.w, r, x + w, r)
        o += f'<path class="ax" d="M{x + w - 6},{r} V{y + 6} H{x + 6} V{r - 7}"/>' + f'<path class="ax" style="fill:var(--ink)" d="M{x + 6},{r - 2} L{x + 2.5},{r - 9} L{x + 9.5},{r - 9} Z"/>'
        return o
    return Nd(w, n.h + up, rail, fn)


def syntax(name, node, cap=""):
    """Complete diagram: name at the top left, an arrow in, the node, an arrow out."""
    x0, y0 = 34, 22
    W = x0 + node.w + 46
    H = y0 + node.h + 10
    o = f'<svg viewBox="0 0 {W:.0f} {H:.0f}" style="width:{W * 1.05:.0f}px;max-width:100%;display:block" role="img" aria-label="{cap or name}">'
    o += f'<text class="lbl bd" x="4" y="14">{name}</text>'
    r = y0 + node.r
    o += _ln(4, r, x0, r) + _arrow(x0, r) + node.svg(x0, y0) + _ln(x0 + node.w, r, x0 + node.w + 38, r) + _arrow(x0 + node.w + 38, r)
    return o + "</svg>"


def sx(name, node, cap=""):
    return f'<div class="synd">{syntax(name, node, cap)}</div>'


def choice_of(chars, name=None):
    """A simple set of terminals as one choice diagram (digit, letter ...)."""
    return A(*[T(c) for c in chars])


# ---------------------------------------------------------------- scheduling

def schedule(procs, algo, q=3):
    """procs = [(name, arrival, burst)]. Returns (segments [(start, end, name)], stats {name: (finish, turnaround, waiting)})."""
    P = {n: (a, b) for n, a, b in procs}
    order = [n for n, _, _ in procs]
    rem = {n: b for n, _, b in procs}
    segs, done, t = [], {}, 0

    def add(n, s0, e0):
        if segs and segs[-1][2] == n and segs[-1][1] == s0:
            segs[-1] = (segs[-1][0], e0, n)
        else:
            segs.append((s0, e0, n))
    if algo == "FCFS":
        for n in sorted(order, key=lambda n: (P[n][0], order.index(n))):
            t = max(t, P[n][0])
            add(n, t, t + P[n][1])
            t += P[n][1]
            done[n] = t
    elif algo in ("SJF", "SRT"):
        left = set(order)
        while left:
            av = [n for n in left if P[n][0] <= t]
            if not av:
                t = min(P[n][0] for n in left)
                continue
            if algo == "SJF":
                n = min(av, key=lambda n: (P[n][1], P[n][0], order.index(n)))
                add(n, t, t + P[n][1])
                t += P[n][1]
                done[n] = t
                left.discard(n)
            else:
                n = min(av, key=lambda n: (rem[n], P[n][0], order.index(n)))
                add(n, t, t + 1)
                rem[n] -= 1
                t += 1
                if rem[n] == 0:
                    done[n] = t
                    left.discard(n)
    else:
        pend = sorted(order, key=lambda n: (P[n][0], order.index(n)))
        queue = []

        def admit():
            while pend and P[pend[0]][0] <= t:
                queue.append(pend.pop(0))
        admit()
        while queue or pend:
            if not queue:
                t = P[pend[0]][0]
                admit()
                continue
            n = queue.pop(0)
            r = min(q, rem[n])
            add(n, t, t + r)
            t += r
            rem[n] -= r
            admit()
            if rem[n] > 0:
                queue.append(n)
            else:
                done[n] = t
    stats = {n: (done[n], done[n] - P[n][0], done[n] - P[n][0] - P[n][1]) for n in order}
    return segs, stats


def gantt(segs, names):
    """HTML Gantt chart with widths proportional to time."""
    end = segs[-1][1]
    h = '<div class="gantt">' + "".join(f'<div class="gb c{names.index(n) % 5}" style="flex:{e - s}">{n}</div>' for s, e, n in segs) + "</div>"
    h += '<div class="gticks">' + "".join(f'<span style="flex:{e - s}">{e}</span>' for s, e, n in segs) + "</div>"
    return f'<div class="gwrap"><div style="font-size:.7rem;color:var(--muted)">0</div>{h}</div>'


AK16JS = r'''
function schedule(procs, algo, q) {
  const P = {}, rem = {}, order = procs.map((p) => p[0]); procs.forEach(([n, a, b]) => { P[n] = [a, b]; rem[n] = b; });
  const segs = [], done = {}; let t = 0;
  const add = (n, s, e) => { const l = segs[segs.length - 1]; if (l && l[2] === n && l[1] === s) l[1] = e; else segs.push([s, e, n]); };
  const key = (n, k) => [k, P[n][0], order.indexOf(n)];
  const cmp = (x, y) => { for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i]; return 0; };
  if (algo === "FCFS") { [...order].sort((a, b) => cmp([P[a][0], order.indexOf(a)], [P[b][0], order.indexOf(b)])).forEach((n) => { t = Math.max(t, P[n][0]); add(n, t, t + P[n][1]); t += P[n][1]; done[n] = t; }); }
  else if (algo === "SJF" || algo === "SRT") {
    const left = new Set(order);
    while (left.size) { const av = [...left].filter((n) => P[n][0] <= t); if (!av.length) { t = Math.min(...[...left].map((n) => P[n][0])); continue; }
      if (algo === "SJF") { av.sort((a, b) => cmp(key(a, P[a][1]), key(b, P[b][1]))); const n = av[0]; add(n, t, t + P[n][1]); t += P[n][1]; done[n] = t; left.delete(n); }
      else { av.sort((a, b) => cmp(key(a, rem[a]), key(b, rem[b]))); const n = av[0]; add(n, t, t + 1); rem[n]--; t++; if (!rem[n]) { done[n] = t; left.delete(n); } } }
  } else {
    const pend = [...order].sort((a, b) => cmp([P[a][0], order.indexOf(a)], [P[b][0], order.indexOf(b)])), queue = [];
    const admit = () => { while (pend.length && P[pend[0]][0] <= t) queue.push(pend.shift()); };
    admit();
    while (queue.length || pend.length) { if (!queue.length) { t = P[pend[0]][0]; admit(); continue; } const n = queue.shift(), r = Math.min(q, rem[n]); add(n, t, t + r); t += r; rem[n] -= r; admit(); if (rem[n] > 0) queue.push(n); else done[n] = t; }
  }
  const stats = {}; order.forEach((n) => (stats[n] = [done[n], done[n] - P[n][0], done[n] - P[n][0] - P[n][1]]));
  return { segs, stats };
}
'''

RPNJS = r'''
const PREC = { "+": 1, "-": 1, "*": 2, "/": 2 };
const toks = (s) => (s.replace(/–/g, "-").match(/\d+(?:\.\d+)?|[A-Za-z]\w*|[()+\-*\/]/g) || []);
function toRpn(s) { const out = [], st = []; for (const t of toks(s)) { if (PREC[t]) { while (st.length && PREC[st[st.length - 1]] && PREC[st[st.length - 1]] >= PREC[t]) out.push(st.pop()); st.push(t); } else if (t === "(") st.push(t); else if (t === ")") { while (st[st.length - 1] !== "(") out.push(st.pop()); st.pop(); } else out.push(t); } return out.concat(st.reverse()); }
function toInfix(r) { const st = []; for (let t of r) { t = t.replace("–", "-"); if (PREC[t]) { const b = st.pop(), a = st.pop(); let ea = a[0], eb = b[0]; if (a[1] < PREC[t]) ea = "(" + ea + ")"; if (b[1] < PREC[t] || (b[1] === PREC[t] && (t === "-" || t === "/"))) eb = "(" + eb + ")"; st.push([ea + " " + t + " " + eb, PREC[t]]); } else st.push([t, 9]); } return st[0][0].replace(/-/g, "–"); }
function runRpn(r, env) { const st = [], trace = []; for (let t of r) { t = t.replace("–", "-"); if (PREC[t]) { const b = st.pop(), a = st.pop(); if (a === undefined || b === undefined) return { error: "The stack has too few values for the operator " + t, trace }; st.push(t === "+" ? a + b : t === "-" ? a - b : t === "*" ? a * b : a / b); } else { const v = env && t in env ? env[t] : Number(t); if (Number.isNaN(v)) return { error: "No value for " + t, trace }; st.push(v); } trace.push(st.slice()); } return { result: st[st.length - 1], left: st.length, trace }; }
'''


def rpn_check():
    """Run the page's JS RPN code under node and compare with the Python one."""
    import json as _j, subprocess, tempfile, os
    cases = ["(2 – 6) * (13 + 7) / 5", "((6 + 12) / (16 – 10)) * 18", "a * b + b - d + 15", "((7 + 3) - (2 * 8)) / 6", "(7 – 2 + 8) / (9 – 5)", "21 * (15 – 3 + 8) / 7", "((18 – 15 + 3) * 5) / 12", "16 + ((9 – 7) / (18 + 6))"]
    rp = ["a b - c + c a - * d /", "a b / 4 * a b + -", "c d + a b - a c - * /", "b a c - + d b + * c /", "5 2 – 5 4 + * 9 /"]
    js = RPNJS + "const C=" + _j.dumps(cases) + ",R=" + _j.dumps(rp) + ";console.log(JSON.stringify([C.map(c=>toRpn(c).join(' ')),R.map(r=>toInfix(r.split(' ')))]))"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(js)
    out = _j.loads(subprocess.run(["node", f.name], capture_output=True, text=True).stdout)
    os.unlink(f.name)
    assert out[0] == [" ".join(to_rpn(c)) for c in cases], out[0]
    assert out[1] == [to_infix(r.split()) for r in rp], out[1]


AK16CSS = r'''
table.stk td,table.stk th{min-width:34px;text-align:center;padding:2px 8px}
.synd{margin:8px 0;overflow-x:auto}
'''


def sched_check(presets):
    """Run the page's JS scheduler under node and assert it matches the Python one for every preset and algorithm."""
    import json as _j, subprocess, tempfile, os
    cases = [(p, a, q) for p in presets for a in ("FCFS", "SJF", "SRT", "RR") for q in (2, 3, 4)]
    js = AK16JS + "\nconst cases=" + _j.dumps(cases) + ";console.log(JSON.stringify(cases.map(([p,a,q])=>{const r=schedule(p,a,q);return [r.segs,r.stats]})));"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(js)
    out = subprocess.run(["node", f.name], capture_output=True, text=True).stdout
    os.unlink(f.name)
    got = _j.loads(out)
    for (p, a, q), (segs, st) in zip(cases, got):
        ps, pst = schedule(p, a, q)
        assert [list(x) for x in ps] == segs and {k: list(v) for k, v in pst.items()} == st, (p, a, q)
