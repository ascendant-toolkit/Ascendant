"""Register pages in site_data.py: reads lines 'slug|at|title|desc|section' from stdin and inserts them before the first A Level entry."""
import sys
p="/Users/garybyatt/Documents/GitHub/Ascendant/site_data.py"; s=open(p).read()
anchor='    {"src": "ac-13-1-1-non-composite-types"'
assert anchor in s
new=""
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    slug,at,title,desc,sec=l.split("|")
    if f'"src": "{slug}"' in s: continue
    new+=f'    {{"src": "{slug}", "role": "review", "at": "{at}", "title": "{title}", "kind": "Interactive",\n     "desc": "{desc}",\n     "places": [("a-cs", "as/{sec}")]}},\n'
s=s.replace(anchor,new+anchor,1); open(p,"w").write(s); print("registered",new.count('"src"'))
