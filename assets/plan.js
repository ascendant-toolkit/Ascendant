// My plan: the plans the signed-in user is registered for. What it shows depends on who pays.
//   individual    : their own paid or free plans, payment history and ways to add or upgrade
//   licence       : a school or tutor teacher sees the licence (subjects, tier, seats, end date); tutors can also pay by card
//   managed       : a student placed by a school or tutor has no plan to manage (the school or tutor pays), so a short note only
(function () {
  const S = window.Site, R = window.Roster;
  const root = document.getElementById("plan-root");
  if (!root) return;
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => (d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "");
  const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;
  const money = (amount, cur) => {
    const n = Number(amount);
    if (!isFinite(n) || amount === null || amount === undefined) return "";
    try { return new Intl.NumberFormat("en-GB", { style: "currency", currency: cur || "USD" }).format(n / 100); } catch (e) { return (n / 100).toFixed(2) + " " + (cur || ""); }
  };
  const PLAN_NAMES = { free: "Free", annual: "Annual", monthly: "Monthly", seasonal: "Seasonal", school: "Licence" };
  const PAY_STATUS = { granted: "Paid", refunded: "Refunded", needs_setup: "Received, being set up" };
  let catalog;

  if (!S || !S.configured) { root.innerHTML = `<div class="placeholder"><h2>Accounts are not switched on yet</h2></div>`; return; }

  const viewOf = (me) => me.plan_view || (me.is_admin ? "admin" : me.is_school_teacher ? "licence" : me.is_teacher ? "none" : me.school ? "managed" : "individual");
  const courseTitle = (k) => catalog.courses[k]?.title || (k === "school-all" ? "All subjects" : k);
  const contactUrl = (topic, role = topic) => `${S.base}contact/?topic=${topic}&role=${role}`;

  function paymentTable(pays) {
    return pays.length ? `<section class="card block"><h3>Payment history</h3><div class="tablewrap"><table class="tbl"><thead><tr><th>Date</th><th>Plan</th><th>Amount</th><th>Status</th></tr></thead><tbody>
      ${pays.map((p) => `<tr><td>${fmt(p.at)}</td><td>${p.product ? esc(courseTitle(p.product)) : "Teacher plan"}${p.tier ? ` · ${esc(R.TIER_NAMES[p.tier] || p.tier)}` : ""}</td>
        <td>${esc(money(p.amount, p.currency))}</td><td>${esc(PAY_STATUS[p.status] || p.status)}</td></tr>`).join("")}</tbody></table></div>
      <p class="hint">Receipts are emailed by Paddle, our payment provider. Refunds: see the <a class="lnk" href="${S.base}refunds/">refund policy</a>.</p></section>` : "";
  }

  const payOptions = (lead, portal) => `<section class="card block"><h3>Payment options</h3><p>${lead}</p>
    <p class="hint">Pay by card or the local payment methods shown at checkout. Annual plans save about 30% against monthly. You are billed in your local currency, with any tax added at checkout, and you keep access until the end of the period you have paid for if you cancel.</p>
    <p><a class="btn" href="${S.base}pricing/">See plans and prices</a> ${portal ? '<button class="btn ghost" id="portal-btn" type="button">Manage billing</button>' : `<a class="btn ghost" href="${S.base}contact/?topic=billing">Change or cancel a plan</a>`}</p><p class="msg err" id="portal-err" hidden></p></section>`;

  async function payments() {
    try { const { data } = await S.sb.rpc("my_payments"); return data || []; } catch (e) { return []; }
  }

  async function individual(me) {
    const seen = new Set();
    const ents = (me.entitlements || []).filter((e) => { const k = e.product + "|" + e.tier; if (seen.has(k)) return false; seen.add(k); return true; });
    const pays = await payments();
    const paid = ents.some((e) => e.source === "payment") || pays.some((p) => p.status === "granted");
    const row = (e) => {
      const live = !e.expires_at || new Date(e.expires_at) > new Date();
      const how = e.source === "payment" ? "Paid" : e.source === "school" ? "Through your school or tutor" : "Added by Ascendant";
      const accent = catalog.courses[e.product]?.accent || "teal";
      return `<tr><td><span class="pill" data-accent="${accent}">${esc(courseTitle(e.product))}</span></td><td><b>${esc(R.TIER_NAMES[e.tier] || e.tier)}</b></td>
        <td>${esc(PLAN_NAMES[e.plan] || e.plan)}</td><td>${how}</td>
        <td>${live ? (e.expires_at ? "Active until " + fmt(e.expires_at) : "Active, no end date") : '<span class="no-txt">Ended ' + fmt(e.expires_at) + "</span>"}</td></tr>`;
    };
    root.innerHTML = `<section class="dash-head"><p class="kicker">My plan</p><h1>${ents.length ? "Your plans" : "You are on the free plan"}</h1>
        <p class="hint">${esc(me.name)} · ${esc(me.email)}</p></section>
      ${ents.length ? `<section class="card block"><div class="tablewrap"><table class="tbl"><thead><tr><th>Subject</th><th>Level</th><th>Billing</th><th>Source</th><th>Status</th></tr></thead><tbody>${ents.map(row).join("")}</tbody></table></div>
          <p class="hint">Basic opens every lesson. Full adds marked assessments, topic tests and your progress tracker.</p></section>`
        : `<section class="card block"><h3>Free access</h3><p class="hint">You can open the free sample lessons and track your progress. A paid plan unlocks the full syllabus for a subject.</p></section>`}
      ${payOptions(paid ? "Add another subject, move up to Full, or switch between monthly and annual billing." : "Choose a subject and a plan to unlock the full syllabus.", paid)}
      ${paymentTable(pays)}`;
    const pb = document.getElementById("portal-btn");
    if (pb) pb.addEventListener("click", async () => {
      const err = document.getElementById("portal-err");
      err.hidden = true; pb.disabled = true; pb.textContent = "Opening...";
      try {
        const { data, error } = await S.sb.functions.invoke("paddle-portal");
        if (error || !data || !data.url) throw new Error("no url");
        location.href = data.url;
      } catch (e) {
        err.innerHTML = `Could not open billing. <a class="lnk" href="${S.base}contact/?topic=billing">Contact us</a> and we will sort it.`;
        err.hidden = false; pb.disabled = false; pb.textContent = "Manage billing";
      }
    });
  }

  async function licence(me) {
    const sc = me.school, active = R.isLive(sc);
    const { data } = await S.sb.rpc("school_dashboard");
    const students = data ? data.students : [];
    const pays = sc.kind === "tutor" ? await payments() : [];
    const seatRows = (sc.per_subject ? sc.products : [null]).map((k) => {
      const used = k ? R.seatsUsed(sc, students, k) : students.length, cap = k ? R.seatCap(sc, k) : sc.seats, p = cap ? Math.min(100, Math.round((100 * used) / cap)) : 0;
      return `<div class="seatrow"><div class="row"><b>${k ? esc(courseTitle(k)) : "Students"}</b><span class="hint">${used} of ${cap} seats</span></div><div class="bar2"><i style="width:${p}%"></i></div></div>`;
    }).join("");
    const left = sc.expires_at ? Math.ceil((new Date(sc.expires_at) - Date.now()) / 864e5) : null;
    root.innerHTML = `<section class="dash-head"><p class="kicker">${sc.kind === "tutor" ? "Tutor licence" : "School licence"}</p><h1>${esc(sc.name)}</h1>
        <p class="hint">${active ? '<span class="pill soft">Active</span>' : '<span class="pill soft">Ended</span>'} ${sc.expires_at ? (active ? "Runs until " + fmt(sc.expires_at) + (left <= 60 ? ` (${plural(left, "day")} left)` : "") : "Ended " + fmt(sc.expires_at)) : "No end date"}</p></section>
      ${active ? "" : `<section class="card block attn"><h3>This licence has ended</h3><p>Your students cannot open lessons until it is renewed. Their progress is kept.</p></section>`}
      <div class="grid two">
        <section class="card block"><h3>What is included</h3>
          <p class="hint">Level: <b>${esc(R.TIER_NAMES[sc.tier] || sc.tier)}</b></p>
          <div class="pills">${sc.products.filter((k) => catalog.courses[k]).map((k) => `<span class="pill" data-accent="${catalog.courses[k].accent}">${esc(catalog.courses[k].title)}</span>`).join("")}</div>
          ${sc.kind === "tutor" ? "" : '<p class="hint" style="margin-top:12px">Teacher accounts on the licence are free and open every subject you have bought.</p>'}</section>
        <section class="card block"><h3>Seats</h3>${seatRows}<p class="hint">A seat is one student in one subject for the length of the licence.</p></section></div>
      <section class="card block"><h3>${sc.kind === "tutor" ? "Renewal and extra students" : "Renewal and extra seats"}</h3>
        <p class="hint">${sc.kind === "tutor" ? "Add students beyond your seats, add a subject, or renew." : "Licences are annual and invoiced. Tell us how many seats you need in each subject and we will update the licence and send the invoice."}</p>
        <p><a class="btn" href="${contactUrl("school", sc.kind === "tutor" ? "tutor" : "school")}">Contact us about this licence</a></p></section>
      ${sc.kind === "tutor" ? payOptions("Renew or add to your plan by card.") : ""}
      ${paymentTable(pays)}`;
  }

  function managed(me) {
    const subs = me.subjects.filter((k) => catalog.courses[k]);
    root.innerHTML = `<section class="dash-head"><p class="kicker">My plan</p><h1>Your access is looked after</h1></section>
      <section class="card block"><p>${me.school ? `<b>${esc(me.school)}</b> manages your account and pays for your lessons, so there is nothing for you to buy or renew.` : "Your teacher manages your account, so there is nothing for you to buy or renew."}</p>
        <div class="pills">${subs.map((k) => `<a class="pill" data-accent="${catalog.courses[k].accent}" href="${S.base}${catalog.courses[k].url}">${esc(catalog.courses[k].title)}</a>`).join("") || '<span class="hint">No subjects yet.</span>'}</div>
        <p class="hint" style="margin-top:12px">Need a different subject? Ask your teacher.</p></section>`;
  }

  function plain(me, text) {
    root.innerHTML = `<section class="dash-head"><p class="kicker">My plan</p><h1>${me.is_admin ? "Admin account" : "Teacher account"}</h1></section>
      <section class="card block"><p>${text}</p><p><a class="btn ghost" href="${S.base}pricing/">See public plans</a></p></section>`;
  }

  async function boot() {
    const me = await S.whoami(true);
    if (!me) {
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      root.innerHTML = `<section class="card block"><h3>Sign in to see your plan</h3><p><a class="btn" href="${S.profileUrl}">Sign in</a> <a class="btn ghost" href="${S.base}pricing/">See plans</a></p></section>`;
      return;
    }
    try { catalog = await S.catalog(); } catch (e) { root.innerHTML = `<p class="msg err">Could not load. Check your connection and refresh.</p>`; return; }
    const v = viewOf(me);
    try {
      if (v === "licence") await licence(me);
      else if (v === "managed") managed(me);
      else if (v === "admin") plain(me, "Admin accounts open every subject at every level. There is nothing to buy.");
      else if (v === "none") plain(me, "Your teacher account is provided by Ascendant and opens every subject. There is nothing to buy.");
      else await individual(me);
    } catch (e) { root.innerHTML = `<p class="msg err">Could not load your plan: ${esc(e.message || String(e))}</p>`; }
  }
  boot();
})();
