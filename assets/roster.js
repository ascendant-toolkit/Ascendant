// Helpers for adding students and reading a licence, shared by the Profile page, the teacher dashboard and the plan page.
(function () {
  const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

  // Academic words for assigned passwords: two words and two digits, e.g. OutcomeMethod47.
  const WORDS = ("analyse approach assess assume benefit concept consist context contrast create data define derive "
    + "design device distinct economy element evaluate evidence factor feature final focus formula function "
    + "framework hypothesis identify illustrate impact indicate input interpret issue labour layer logic margin "
    + "method model monitor network norm obtain outcome output parallel phase policy predict principle process "
    + "project quote range ratio region relevant research resource response restrict role sector select sequence "
    + "source specific structure survey symbol target theory tradition transfer trend unique valid variable version "
    + "volume").split(" ");
  const cap = (w) => w[0].toUpperCase() + w.slice(1);
  const rnd = (n) => crypto.getRandomValues(new Uint32Array(1))[0] % n;
  function genPassword(taken = new Set()) {
    for (;;) {
      const a = WORDS[rnd(WORDS.length)], b = WORDS[rnd(WORDS.length)];
      const pw = cap(a) + cap(b) + String(10 + rnd(90));
      if (a !== b && !taken.has(pw)) return pw;
    }
  }

  // "Name, email" or "Name, email, second email" per line, as typed into the add-students boxes.
  function parseStudentLines(text) {
    const rows = [], bad = [];
    text.split("\n").map((l) => l.trim()).filter(Boolean).forEach((l) => {
      const parts = l.split(/[,\t;]/).map((x) => x.trim()).filter(Boolean);
      const emails = parts.filter((x) => x.includes("@")).map((x) => x.toLowerCase());
      const name = parts.filter((x) => !x.includes("@")).join(" ").trim();
      const [email, email2] = emails;
      if (!name || !email || emails.length > 2 || !emails.every((x) => EMAIL_RE.test(x)) || email === email2) bad.push(l);
      else rows.push({ line: l, name, email, email2: email2 || null });
    });
    return { rows, bad };
  }

  const fmt = (d) => (d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "");
  const TIER_NAMES = { free: "Free", basic: "Basic", full: "Full", vip: "VIP" };
  const isLive = (sc) => !sc.expires_at || new Date(sc.expires_at) > new Date();
  // Seats: old-style licences cap total students; per-subject licences cap each subject (seat_limits overrides seats).
  const seatCap = (sc, k) => (sc.per_subject ? Number(sc.seat_limits?.[k] ?? sc.seats) : sc.seats);
  const schoolSubs = (sc, p) => (p.school_subjects == null ? sc.products : p.school_subjects.filter((k) => sc.products.includes(k)));
  const seatsUsed = (sc, studs, k) => studs.filter((p) => schoolSubs(sc, p).includes(k)).length;
  const shortTitle = (catalog, k) => (catalog.courses[k]?.title || k).replace("A-Level", "A").replace("IGCSE", "IG").replace("Computer Science", "CS").replace("Economics", "Econ");
  const seatText = (catalog, sc, studs) => (sc.per_subject
    ? sc.products.map((k) => `${shortTitle(catalog, k)} ${seatsUsed(sc, studs, k)}/${seatCap(sc, k)}`).join(", ") + " seats used"
    : `${studs.length} of ${sc.seats} seats used`);
  const licenceLine = (catalog, sc, studs) => `${TIER_NAMES[sc.tier]} · ${seatText(catalog, sc, studs)} · ${sc.expires_at ? (isLive(sc) ? "ends " : "ended ") + fmt(sc.expires_at) : "no end date"}`;

  window.Roster = { EMAIL_RE, genPassword, parseStudentLines, TIER_NAMES, isLive, seatCap, schoolSubs, seatsUsed, shortTitle, seatText, licenceLine };
})();
