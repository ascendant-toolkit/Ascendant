"""Shared pieces for the A Level Paper 3/4 AO1, AO2, AO3 lessons (mk_pa1.py, mk_pa2.py, mk_pa3.py)."""
from as6k import *
EYP = "A Level Economics · 9708 · Exam technique"

STRIP = '''
function strip(el, aria, L) {
  const n = L.length, w = Math.floor((740 - (n - 1) * 10) / n), C = ["f3", "f3", "f1", "f1", "f2", "f2"];
  let o = "";
  L.forEach(([a, b], i) => {
    const x = 10 + i * (w + 10);
    o += SV.rect(x, 12, w, 84, C[i % 6], { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, a, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" });
    b.split(" | ").forEach((p, j) => { o += SV.text(x + w / 2, 62 + j * 18, p, "sm", { "text-anchor": "middle" }); });
  });
  $(el).innerHTML = `<svg viewBox="0 0 760 108" role="img" aria-label="${aria}">${o}</svg>`;
}
'''

def exam_intro(kind):
    return (f"These are practice questions in the style of Paper 4, written for this site, so they are safe to set as practice. "
            f"Each one shows what the mark scheme would reward in our own words. For real past questions with their sources, use the Paper 4 essay page and the Paper 4 Section A page. {kind}")
