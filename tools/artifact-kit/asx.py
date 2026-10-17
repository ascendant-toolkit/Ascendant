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
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, "P1", "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, "P2", "Q2", g * n);
  return o;
}
'''
