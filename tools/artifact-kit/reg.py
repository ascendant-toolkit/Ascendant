"""Registers split part reviews in site_data.py and demotes the old single page to a resource.
Usage (from mk_ch*.py or by hand): reg.split("government-policies-market-failure", "ch-38", "38", [(slug, "38.1", title, desc), ...], "New resource title")"""
import re, pathlib
SD = pathlib.Path(__file__).resolve().parents[2] / "site_data.py"

def split(old_slug, place, chapter, parts, old_title, old_desc=None):
    s = SD.read_text()
    m = re.search(r'    \{"src": "%s",.*?\n     "places": \[[^\]]*\]\},\n' % re.escape(old_slug), s, re.S)
    assert m, old_slug
    old = m.group(0)
    new = old.replace('"role": "review", ', "")
    new = re.sub(r'"at": "[^"]*"', '"at": "%s.9"' % chapter, new)
    new = re.sub(r'"title": "[^"]*"', '"title": "%s"' % old_title, new, count=1)
    if old_desc: new = re.sub(r'\n     "desc": "[^"]*"', '\n     "desc": "%s"' % old_desc, new, count=1)
    ents = ""
    for slug, at, title, desc in parts:
        if f'"src": "{slug}"' in s: continue
        ents += f'    {{"src": "{slug}", "role": "review", "at": "{at}", "title": "{title}", "kind": "Interactive",\n     "desc": "{desc}",\n     "places": [("a-econ", "a-level/{place}")]}},\n'
    s = s.replace(old, ents + new)
    SD.write_text(s)
    print("registered", len(parts), "parts; old page now a resource")
