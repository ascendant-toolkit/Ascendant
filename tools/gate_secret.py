"""Creates the secret that locks lesson files. Run once per machine: python3 tools/gate_secret.py

Writes .gate_secret (read by build.py) and supabase/gate_secret.sql (paste into the Supabase SQL Editor once).
Both files are git-ignored: this repo is public, so the secret must never be committed.
"""
import secrets
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
secret_file = ROOT / ".gate_secret"
if secret_file.exists():
    raise SystemExit(".gate_secret already exists. Delete it only if you mean to re-lock everything with a new key.")
master = secrets.token_hex(32)
secret_file.write_text(master + "\n")
secret_file.chmod(0o600)
(ROOT / "supabase" / "gate_secret.sql").write_text(
    "-- Run once in the Supabase SQL Editor. Do not commit this file.\n"
    f"insert into public.settings (key, value) values ('gate_master', '{master}')\n"
    "on conflict (key) do update set value = excluded.value;\n")
print("Created .gate_secret and supabase/gate_secret.sql")
