"""Our own wording for exam questions that had been copied from the papers.

reword.json maps the old text to the new. build.py applies it to every lesson, so a question shared by several
lessons is changed everywhere at once. The new text uses curly apostrophes, so it is safe inside HTML and any kind of
script string. Meaning, figures, command words and answer order are unchanged.
"""
import json
from pathlib import Path

_PAIRS = json.loads((Path(__file__).parent / "reword.json").read_text(encoding="utf-8"))


def _forms(old):
    """The ways a piece of text can be written in a page: as it is, or escaped inside a script string."""
    return list(dict.fromkeys([old, json.dumps(old, ensure_ascii=False)[1:-1], json.dumps(old)[1:-1], old.replace("'", "\\'")]))


def _curly(new):
    assert '"' not in new and "\\" not in new and "`" not in new, new
    new = new.replace(" '", " ‘").replace("('", "(‘")
    if new.startswith("'"):
        new = "‘" + new[1:]
    return new.replace("'", "’")


# longest first, so a short option is never replaced inside a longer question that contains it
TABLE = [(form, _curly(p["new"])) for p in sorted(_PAIRS, key=lambda p: -len(p["old"])) for form in _forms(p["old"])]


def apply(page):
    for old, new in TABLE:
        if old in page:
            page = page.replace(old, new)
    return page
