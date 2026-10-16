"""Builds the JS for the syllabus 8.3 part pages (ld, ls, mu, mw) from slices of lab.js plus <name>_extra.js.
Run: python3 tools/artifact-kit/mk_ch40.py   (then assemble.py for each part)."""
import pathlib
d = pathlib.Path(__file__).parent
L = (d / "lab.js").read_text().split("\n")
def sl(a, b): return "\n".join(L[a - 1:b]) + "\n"           # 1-based inclusive lines of lab.js
SHARED, STEP_A, STEP_B, STEP_C = sl(1, 9), sl(10, 33), sl(35, 66), sl(68, 99)
LAB2, LAB3 = sl(126, 156), sl(158, 180)
PARTS = {
    "ld": SHARED + STEP_A,
    "ls": SHARED,
    "mu": SHARED,
    "mw": SHARED + STEP_B + STEP_C + LAB2 + LAB3,
}
for name, base in PARTS.items():
    extra = d / f"{name}_extra.js"
    if extra.exists():
        (d / f"{name}.js").write_text(base + extra.read_text())
        print("wrote", name + ".js")
