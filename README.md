# Ascendant

Static site for IGCSE and A-Level Economics and Computer Science classroom activities. Hosted on GitHub Pages from `docs/`.

## Adding an artifact

1. Drop its HTML (plus any supporting files) in `artifacts_src/<slug>/`, main page as `index.html`.
2. Add an entry to `ARTIFACTS` in `site_data.py` with its chapter placement. The first placement is where the back link goes.
3. `python3 build.py`, commit, push. Pages redeploys.

Course structure (chapters, sections, AS/A Level split) also lives in `site_data.py`. `docs/` is generated, don't edit it by hand.

## Profile setup (Supabase)

No emails and no self sign-up. The Admin panel creates each student's login with a generated password (two academic words plus two digits, e.g. `OutcomeMethod47`), which you give to the student. Students sign in on the Profile page with their email and that password. A student can have up to two login emails (any provider), both using the same password.

1. Create a Supabase project. Put its URL and public (publishable) key in `assets/config.js`, run `python3 build.py`, push.
2. SQL Editor: paste the contents of `supabase/schema.sql` and run it. Safe to re-run.
3. Set admin passwords by hand (never commit them), then re-run the last two statements of the schema:
   `update public.admins set initial_password = '...' where email = '...';`
4. Optional hardening: Authentication > Sign In / Providers > turn off "Allow new users to sign up".
5. Sign in on the Profile page as an admin, then add students from the Admin panel.

Admin panel: add students, edit name/subjects/password, collapsible list of assigned passwords, Reset login (recreates the login with the listed password, keeps progress), delete student, progress CSV.

## Access and entitlements (Supabase)

The site decides which courses someone sees from `whoami().subjects`, so the front end is the same whether the site is free or paid. Behind it, `supabase/schema.sql` (section "Entitlements (v5)") adds `products`, `entitlements` and a `paywall_enabled` setting.

- **Paywall off (now):** subjects are the ones an admin sets on a student's profile, plus any active entitlement. Setting subjects on a profile also writes `manual` entitlements, so the two stay in step.
- **Paywall on (later):** subjects come from active entitlements only. An entitlement has a product (`ig-econ`, `ig-cs`, `a-econ`, `a-cs` or `school-all`), a plan (`annual`, `seasonal`, `school`, `free`) and an optional `expires_at`.
- `select admin_paywall_check();` lists anyone who would lose a subject if the paywall were switched on. `select admin_set_paywall(true);` refuses while that list is not empty.
- `admin_grant(email, product, plan, expires, org, note)` and `admin_revoke(email, product)` manage passes and school licences.
- This controls what the site shows. The lesson files are still public static pages, so real protection of paid content needs the content served from Supabase (not built yet).

## Schools (Supabase)

A school licence (`schools` in `supabase/schema.sql`, section "Schools (v8)") covers some subjects at one tier for a number of student seats until an end date. Create and edit them from the Admin panel's "Schools & tutors" tab, then add the teacher there; they get a generated password like students do. A private tutor is the same thing with type "Tutor" (a label for the list and pricing; access works the same), usually with a handful of seats.

- A school teacher signs in on the Profile page and sees their own school: they add students (up to the seat limit), copy logins, reset logins, remove students and see each student's progress and scores. They can open the licence's lessons at its tier, but not submit assessments.
- Students on a school get its subjects at its tier on top of anything set on their own profile, and lose them when the end date passes. Removing a student frees the seat and keeps their progress.
- The seat limit is enforced in the database (`check_school_seats`), so it holds for teachers and admins alike.
- An admin can move a student between schools, or set the tier of a student's own subjects, from the student's Edit dialog.

## Locked lessons

Every lesson that belongs to a course is published as an encrypted `payload.bin` plus a tiny shell page (`assets/gateload.js`). The shell asks Supabase for the lesson's key (`artifact_key()` in `schema.sql`); the database only releases it to admins, co-teachers and members whose subjects include the lesson's course. Without a key the file is unreadable, so view-source or the GitHub repo shows nothing useful. Course pages, titles and descriptions stay public. Artifacts marked `"public": True` in `site_data.py`, and ones in no course (Investing), stay open.

- **First time on a machine:** `python3 tools/gate_secret.py` creates `.gate_secret` (git-ignored) and `supabase/gate_secret.sql`. Paste `schema.sql`, then `gate_secret.sql`, then `artifact_access_seed.sql` into the Supabase SQL Editor. Never commit the secret: the repo is public. If `.gate_secret` is lost, make a new one and rerun `gate_secret.sql`; the build re-encrypts everything.
- **Every new or re-homed artifact:** run `python3 build.py`, then paste `supabase/artifact_access_seed.sql` (safe to rerun) so the database knows which courses unlock it. Until then that lesson shows "not ready yet". A student who has the subject but too low a tier sees "Upgrade to <tier>".
- **Emergency rollback:** `GATE=off python3 build.py` builds plain, open pages again.
- A signed-in member can still save a lesson they are allowed to open. This stops casual access and sharing of links, not a determined member.
