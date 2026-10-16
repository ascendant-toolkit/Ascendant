"""Pushes supabase/artifact_access_seed.sql to the artifact_courses table over the Supabase REST API.
Needs SUPABASE_URL and SUPABASE_SERVICE_KEY in the environment (a GitHub secret in CI). Safe to rerun."""
import json, os, pathlib, re, sys, urllib.parse, urllib.request

url, key = os.environ["SUPABASE_URL"].rstrip("/"), os.environ["SUPABASE_SERVICE_KEY"]
seed = pathlib.Path(__file__).resolve().parent.parent / "supabase" / "artifact_access_seed.sql"
rows = [{"slug": s, "courses": re.findall(r"'([^']+)'", c)} for s, c in re.findall(r"\('([^']+)', array\[([^\]]*)\]\)", seed.read_text(encoding="utf-8"))]
if not rows:
    sys.exit("No rows parsed from the seed file; refusing to touch the table.")

def call(method, path, body=None, extra=None):
    req = urllib.request.Request(url + "/rest/v1/" + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"apikey": key, "Authorization": "Bearer " + key, "Content-Type": "application/json", **(extra or {})})
    with urllib.request.urlopen(req) as r:
        return r.status

call("POST", "artifact_courses?on_conflict=slug", rows, {"Prefer": "resolution=merge-duplicates,return=minimal"})
keep = ",".join('"%s"' % r["slug"] for r in rows)
call("DELETE", "artifact_courses?slug=not.in.(" + urllib.parse.quote(keep, safe='",') + ")", extra={"Prefer": "return=minimal"})
print(f"Synced {len(rows)} lessons to artifact_courses.")
