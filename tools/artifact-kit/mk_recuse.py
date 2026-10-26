"""Builds the 19.2 recursion use-case pages (one per typical use of recursion).

Shell (CSS, tabs, kit library, trace engine) is cut from the compound interest page; each page's
content lives in tools/artifact-kit/recuse/<id>.html and <id>.js. In the html, a line
<!--PP: <src text>--> is replaced by the matching past-paper block from artifacts_src/recursion/index.html.

    python3 tools/artifact-kit/mk_recuse.py [id ...]     then     python3 build.py
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "artifacts_src"
KIT = Path(__file__).parent / "recuse"
PAGES = {
    "fib": ("recursion-fibonacci", "Recursion in Action: The Fibonacci Sequence"),
    "tree": ("recursion-binary-tree", "Recursion in Action: Binary Tree Traversal"),
    "bs": ("recursion-binary-search", "Recursion in Action: Binary Search"),
    "lst": ("recursion-lists-strings", "Recursion in Action: Lists and Strings, One Item at a Time"),
}

shell = (SRC / "recursion-compound-interest" / "index.html").read_text()
head_end = shell.index('<div class="wrap">') + len('<div class="wrap">')
lib_start = shell.index("<script>")
lib_end = shell.index("/* ===== Compound interest")
head, lib = shell[:head_end], shell[lib_start:lib_end]
head = re.sub(r"<title>.*?</title>", "<title>@@TITLE@@</title>", head, count=1)

# the explore labs step through values with Previous/Next buttons rather than a range slider
rs = (SRC / "recursion" / "index.html").read_text()
btn = rs[rs.index("/* ---------- slider (back / next buttons)"):rs.index("/* ---------- classify")]
a = lib.index("/* ---------- slider ----------")
lib = lib[:a] + btn + lib[lib.index("/* ---------- classify"):]

rec = (SRC / "recursion" / "index.html").read_text()
blocks = re.findall(r'  <details class="eq"><summary><span class="src">.*?</div></details>', rec, flags=re.S)


def paper(key):
    for b in blocks:
        if key in b[:400]:
            return b
    raise SystemExit("past paper block not found: " + key)


def build(pid):
    slug, title = PAGES[pid]
    html = (KIT / f"{pid}.html").read_text()
    html = re.sub(r"<!--PP: (.*?)-->", lambda m: paper(m.group(1)), html)
    js = (KIT / f"{pid}.js").read_text()
    out = head.replace("@@TITLE@@", title) + "\n" + html + "\n" + lib + js + "\nLib.initTabs();\n</script>\n</body></html>\n"
    d = SRC / slug
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(out)
    print("wrote", d / "index.html", len(out))


for p in sys.argv[1:] or PAGES:
    build(p)
