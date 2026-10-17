"""Helpers for the AS Level (9708) syllabus-numbered pages."""
from syl import *

_M = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}

def L(code, n, tail=", reworded"):
    """Label for a past paper question: L('m21_12', 1) -> 'Feb/March 2021 · 12 · Q1, reworded'."""
    ser, var = code.split("_")
    return f"{_M[ser[0]]} 20{ser[1:]} · {var} · Q{n}{tail}"

def P(code, q):
    """Source line for a written question: P('s20_21', '2(a)') -> 'Based on May/June 2020 · 9708/21 · Q2(a)'."""
    ser, var = code.split("_")
    return f"Based on {_M[ser[0]]} 20{ser[1:]} · 9708/{var} · Q{q}"

def mcq(code, n, q, opts, a, why):
    """One reworded Paper 1 question with its source in the stem."""
    return (f"{q} ({L(code, n)})", opts, a, why)

_ep = exam_page
def exam_page(*a, **k):
    k.setdefault("mcq_h", "Multiple choice questions (Paper 1)")
    return _ep(*a, **k)

EYAS = lambda sub: f"AS Level Economics · 9708 · Syllabus {sub}"

# Shared supply and demand plotting for AS topic 2 pages. D: p = 90 - 0.8(q - d), S: p = 10 + 0.8(q - s); start equilibrium (50, 50).
SDJS = '''
const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}
'''

# Tax and subsidy incidence diagram. Demand p = 50 + m(50 - q), supply p = 50 + n(q - 50) + t (t > 0 tax, t < 0 subsidy), start equilibrium (50, 50).
INCJS = '''
const incEq = (m, n, t) => { const q = 50 - t / (m + n), pc = 50 + m * (t / (m + n)); return { q, pc, pp: pc - t, sc: m / (m + n) }; };
function incPlot(x0, w, m, n, t, k, name, o = {}) {
  const X = (q) => x0 + q * (w / 110), Y = (p) => 250 - p * 1.7, e = incEq(m, n, t), ax = Math.abs(t) > 0.05, dEnd = Math.min(100, 50 + 45 / m);
  let s = SV.line(x0, 250, x0 + w, 250) + SV.line(x0, 250, x0, 50) + SV.text(x0 + 6, 46, "Price", "sm") + SV.text(x0 + w, 270, "Quantity", "sm", { "text-anchor": "end" });
  if (name) s += SV.text(x0 + w / 2, 30, name, "lbl bd", { "text-anchor": "middle" });
  s += SV.line(X(0), Y(50 + 50 * m), X(dEnd), Y(50 + m * (50 - dEnd)), "c2", { "stroke-width": 3 }) + tag(X(dEnd) + 4, Y(50 + m * (50 - dEnd)) + 4, "D", "c2");
  s += SV.line(X(0), Y(50 - 50 * n), X(100), Y(50 + 50 * n), "c1", { "stroke-width": 3, ...op(ax && k > 0 ? 0.4 : 1) }) + tag(X(100) + 4, Y(50 + 50 * n), "S", "c1", ax && k > 0 ? 0.4 : 1);
  s += SV.circle(X(50), Y(50), 5, "dot1", op(ax && k > 0 ? 0.6 : 1)) + SV.line(x0, Y(50), X(50), Y(50), "dash", op(0.6)) + SV.line(X(50), Y(50), X(50), 250, "dash", op(0.6)) + SV.text(x0 - 6, Y(50) + 4, "50", "sm", { "text-anchor": "end" });
  if (ax && k > 0) {
    s += SV.line(X(0), Y(50 - 50 * n + t), X(100), Y(50 + 50 * n + t), "c3", { "stroke-width": 3, ...op(k) }) + tag(X(100) + 4, Y(50 + 50 * n + t), t > 0 ? "S + tax" : "S + subsidy", "c3", k);
    const mid = 50;
    s += SV.rect(X(0), Math.min(Y(e.pc), Y(mid)), X(e.q) - X(0), Math.abs(Y(mid) - Y(e.pc)), "f3", op(0.45 * k)) + SV.rect(X(0), Math.min(Y(e.pp), Y(mid)), X(e.q) - X(0), Math.abs(Y(e.pp) - Y(mid)), "f2", op(0.45 * k));
    s += SV.circle(X(e.q), Y(e.pc), 6, "dot3", op(k)) + SV.circle(X(e.q), Y(e.pp), 5, "dot2", op(k)) + SV.line(x0, Y(e.pc), X(e.q), Y(e.pc), "dash", op(k)) + SV.line(x0, Y(e.pp), X(e.q), Y(e.pp), "dash", op(k)) + SV.line(X(e.q), Y(e.pc), X(e.q), 250, "dash", op(k));
    s += SV.text(x0 - 6, Y(e.pc) + 4, Lib.fmtN(e.pc, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(x0 - 6, Y(e.pp) + 4, Lib.fmtN(e.pp, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(X(e.q), 268, Lib.fmtN(e.q, 1), "sm", { "text-anchor": "middle", ...op(k) });
  }
  return s;
}
'''

# AD/AS plotting on top of the same linear geometry as sdPlot. AD p = 90 - 0.8(q - a); SRAS p = 10 + 0.8(q - s); LRAS vertical at 75 + l.
ADASJS = '''
const adLab = { x: "Real output (Y)", y: "Price level", D1: "AD1", D2: "AD2", S1: "SRAS1", S2: "SRAS2", P1: "P1", Q1: "Y1", P2: "P2", Q2: "Y2" };
function adasPlot(st, o = {}) {
  const l = st.l || 0, ln = o.lras !== false;
  let s = sdPlot({ d: st.a || 0, s: st.s || 0, g: st.g === undefined ? 1 : st.g, n: st.n === undefined ? 1 : st.n }, adLab);
  if (ln) s += SV.line(SDX(75 + l), SDY(0), SDX(75 + l), SDY(100), "c4", { "stroke-width": 3, "stroke-dasharray": "7 4" }) + tag(SDX(75 + l) + 6, SDY(98), "LRAS", "c4");
  return s;
}
'''
