// Shared auth + progress layer. Loaded on chapter pages, artifact pages and the profile page.
(function () {
  const cfg = window.SITE_CONFIG || {};
  const base = new URL("../", document.currentScript.src).href; // site root
  // A password-reset link can land on any page (Supabase falls back to its Site URL). Hand the token to the Profile page, which owns the set-new-password screen.
  if (location.hash.includes("type=recovery") && !location.pathname.endsWith("/profile/")) { location.replace(base + "profile/" + location.hash); return; }
  const configured = !!(cfg.supabaseUrl && cfg.anonKey && window.supabase);
  const sb = configured ? window.supabase.createClient(cfg.supabaseUrl, cfg.anonKey) : null;

  const Site = { configured, sb, base, profileUrl: base + "profile/", done: new Map(), me: null };
  window.Site = Site;

  // The catalog holds each artifact's default role (review or resource). Admin overrides live in the
  // artifact_roles table and are layered on here, so progress totals follow whatever the admin chose.
  let catPromise = null;
  Site.catalog = () => (catPromise = catPromise || (async () => {
    const cat = await fetch(base + "assets/catalog.json", { cache: "no-cache" }).then((r) => r.json());
    if (sb) {
      try {
        const { data } = await Promise.race([sb.from("artifact_roles").select("slug,role"), new Promise((_, rej) => setTimeout(rej, 4000))]);
        (data || []).forEach((r) => { if (cat.artifacts[r.slug]) cat.artifacts[r.slug].role = r.role; });
      } catch (e) {}
    }
    // cat.roles keeps every artifact's role; "hidden" ones (admin-deleted) are dropped from the rest of the catalog.
    cat.roles = {};
    Object.entries(cat.artifacts).forEach(([s, x]) => { cat.roles[s] = x.role; if (x.role === "hidden") delete cat.artifacts[s]; });
    const rev = (s) => cat.roles[s] === "review";
    Object.values(cat.courses).forEach((c) => {
      const seen = new Set();
      c.groups.forEach((g) => g.chapters.forEach((ch) => { ch.slugs = (ch.all || ch.slugs).filter(rev); ch.slugs.forEach((s) => seen.add(s)); }));
      c.slugs = [...seen];
    });
    cat.order = cat.order.filter(rev);
    return cat;
  })());

  // Admin only: set an artifact to "review", "resource" or "hidden" (deleted: gone for students, restorable).
  Site.setRole = async (slug, role) => {
    const { error } = await sb.from("artifact_roles").upsert({ slug, role, updated_at: new Date().toISOString() });
    if (error) return false;
    const cat = await Site.catalog();
    cat.roles[slug] = role;
    document.dispatchEvent(new CustomEvent("site:rolechange", { detail: { slug, role } }));
    return true;
  };

  Site.session = async () => (sb ? (await sb.auth.getSession()).data.session : null);

  // Returns {email, name, subjects, requested, is_admin} or null when signed out / not on the roster.
  // Cached briefly so every page load does not wait on the database; pass force to refresh.
  Site.whoami = async (force) => {
    if (!sb || !(await Site.session())) { sessionStorage.removeItem("site.me"); Site.me = null; return null; }
    if (!force) {
      try {
        const c = JSON.parse(sessionStorage.getItem("site.me") || "null");
        if (c && Date.now() - c.t < 60000) return (Site.me = c.me);
      } catch (e) {}
    }
    const { data } = await sb.rpc("whoami");
    Site.me = data || null;
    try { sessionStorage.setItem("site.me", JSON.stringify({ t: Date.now(), me: Site.me })); } catch (e) {}
    return Site.me;
  };

  Site.loadProgress = async () => {
    Site.done = new Map();
    if (!Site.me) return Site.done;
    const { data } = await sb.from("progress").select("slug,done_at").eq("email", Site.me.email);
    (data || []).forEach((r) => Site.done.set(r.slug, r.done_at));
    return Site.done;
  };

  Site.toggle = async (slug) => {
    if (!Site.me) return false;
    if (Site.done.has(slug)) {
      const { error } = await sb.from("progress").delete().eq("email", Site.me.email).eq("slug", slug);
      if (error) return false;
      Site.done.delete(slug);
    } else {
      const { error } = await sb.from("progress").insert({ email: Site.me.email, slug });
      if (error) return false;
      Site.done.set(slug, new Date().toISOString());
    }
    return true;
  };

  // "Mark done" buttons: any element with data-done-slug. Lessons that have an assessment are completed by
  // passing it, so their button becomes a link to the assessment.
  Site.assessed = {};
  Site.attempts = new Map();
  const assessUrl = (slug) => base + "assess/?a=" + encodeURIComponent(slug);

  const staffMe = () => !!(Site.me && (Site.me.is_admin || Site.me.is_teacher));

  // Taught ticks per class. The admin's class groups are fixed (same ids as the admin console); school and tutor
  // teachers use the classes they made on the dashboard. Co-teachers have no classes, so their button is a plain tick.
  Site.adminGroups = [
    { id: "ig1-cs", name: "IG1 CS", subject: "ig-cs" }, { id: "ig2-cs", name: "IG2 CS", subject: "ig-cs" },
    { id: "ig2-econ", name: "IG2 Econ", subject: "ig-econ" }, { id: "a-cs", name: "AL CS", subject: "a-cs" }, { id: "a-econ", name: "AL Econ", subject: "a-econ" },
  ];
  Site.classes = []; Site.taught = null;   // taught: Map slug -> Set of class keys, or null when per-class ticking is unavailable
  async function loadTaught() {
    Site.classes = []; Site.taught = null;
    if (!staffMe()) return;
    if (Site.me.is_admin) Site.classes = Site.adminGroups;
    else if (Site.me.is_school_teacher) {
      const { data, error } = await sb.rpc("teacher_classes");
      if (!error) Site.classes = (data || []).map((c) => ({ id: String(c.id), name: c.name, subject: c.subject }));
    }
    if (!Site.classes.length) return;
    const { data, error } = await sb.rpc("my_taught");
    if (error) return;
    Site.taught = new Map();
    (data || []).forEach((r) => { if (!Site.taught.has(r.slug)) Site.taught.set(r.slug, new Set()); Site.taught.get(r.slug).add(r.class); });
  }
  const perClass = () => !!(Site.taught && Site.classes.length);
  const courseOf = (slug) => { const c = Site.cat && Object.entries(Site.cat.courses).find(([, v]) => v.slugs.includes(slug)); return c ? c[0] : null; };
  const classesFor = (slug) => { const k = courseOf(slug); return Site.classes.filter((c) => !c.subject || !k || c.subject === k); };

  // Teacher clicked "Mark taught" on a lesson: choose which classes it was taught to.
  function chooseClasses(slug) {
    return new Promise((resolve) => {
      const list = classesFor(slug), have = Site.taught.get(slug) || new Set();
      const dlg = document.createElement("dialog");
      dlg.innerHTML = `<form method="dialog"><h3>Taught to which classes?</h3>
        ${list.length ? `<div class="chks" style="flex-direction:column;gap:8px">${list.map((c) => `<label class="chk"><input type="checkbox" value="${c.id}" ${have.has(c.id) ? "checked" : ""}> ${c.name.replace(/</g, "&lt;")}</label>`).join("")}</div>`
          : '<p class="hint">None of your classes take this subject. Set a subject on a class from your dashboard.</p>'}
        <div class="row"><button class="btn" value="save" ${list.length ? "" : "disabled"}>Save</button><button class="btn ghost" value="cancel" formnovalidate>Cancel</button></div></form>`;
      document.body.appendChild(dlg);
      dlg.addEventListener("close", () => {
        const ok = dlg.returnValue === "save", picked = [...dlg.querySelectorAll("input:checked")].map((i) => i.value);
        dlg.remove();
        resolve(ok ? { picked, list } : null);
      });
      dlg.showModal();
    });
  }
  async function markTaught(slug) {
    const r = await chooseClasses(slug);
    if (!r) return true;
    const have = Site.taught.get(slug) || new Set(), now = new Set(r.picked);
    for (const c of r.list) {
      if (now.has(c.id) === have.has(c.id)) continue;
      const { error } = await sb.rpc("set_taught", { _class: c.id, _slugs: [slug], _taught: now.has(c.id) });
      if (error) return false;
    }
    const kept = new Set([...have].filter((k) => !r.list.some((c) => c.id === k)));   // classes the dialog did not offer stay as they were
    r.picked.forEach((k) => kept.add(k));
    if (kept.size) Site.taught.set(slug, kept); else Site.taught.delete(slug);
    // The teacher's own tick means taught to at least one class, so the Profile course map follows.
    if ((kept.size > 0) !== Site.done.has(slug)) return await Site.toggle(slug);
    return true;
  }
  function paint(btn) {
    const slug = btn.dataset.doneSlug, a = Site.assessed[slug], staff = staffMe();
    if (a && !staff) {
      const t = Site.attempts.get(slug);
      btn.title = `Complete by scoring ${a.pass}% or more`;
      btn.classList.toggle("is-done", Site.done.has(slug));
      btn.textContent = !Site.me ? "Sign in to take assessment"
        : Site.done.has(slug) ? `✓ Passed${t ? " (" + t.pct + "%)" : ""}` : t ? `Assessment ${t.pct}%` : "Take assessment";
      return;
    }
    if (!Site.me) {
      btn.textContent = "Sign in to track";
      btn.classList.remove("is-done");
      btn.title = "Sign in on the Profile page to record your progress";
    } else if (Site.done.has(slug)) {
      const ks = staff && perClass() ? Site.taught.get(slug) : null;
      btn.textContent = staff ? "✓ Taught" + (ks && ks.size ? (ks.size === 1 ? ": " + (Site.classes.find((c) => c.id === [...ks][0])?.name || "1 class") : ` (${ks.size} classes)`) : "") : "✓ Done";
      btn.classList.add("is-done");
      btn.title = "Click to undo";
    } else {
      btn.textContent = staff ? "Mark taught" : "Mark done";
      if (staff && perClass()) btn.title = "Choose which classes you taught this to";
      btn.classList.remove("is-done");
      btn.title = "";
    }
  }

  Site.bindButtons = () => bindButtons();
  async function bindButtons() {
    const btns = document.querySelectorAll("[data-done-slug]");
    if (!btns.length) return;
    if (!configured) { btns.forEach((b) => (b.hidden = true)); return; }
    await Site.whoami();
    await Site.loadProgress();
    let cat = null;
    try { cat = await Site.catalog(); Site.assessed = cat.assessed || {}; Site.cat = cat; } catch (e) {}
    try { await loadTaught(); } catch (e) {}
    if (Site.me && !Site.me.is_admin && !Site.me.is_teacher && Object.keys(Site.assessed).length) {
      const { data } = await sb.rpc("my_attempts");
      (data || []).forEach((r) => Site.attempts.set(r.slug, r));
    }
    const isRev = (s) => !cat || cat.roles[s] === "review";
    btns.forEach((b) => {
      if (b.dataset.bound) return;
      b.dataset.bound = "1";
      b.hidden = !isRev(b.dataset.doneSlug);
      paint(b);
      // Teachers mark assessed lessons taught like any other, so the assessment preview gets its own link beside the button.
      if (staffMe() && Site.assessed[b.dataset.doneSlug] && isRev(b.dataset.doneSlug)) {
        const l = document.createElement("a");
        l.className = "mini"; l.textContent = "Preview assessment"; l.href = assessUrl(b.dataset.doneSlug);
        b.after(l);
      }
      b.addEventListener("click", async (e) => {
        e.preventDefault();
        if (!Site.me) { location.href = Site.profileUrl; return; }
        if (Site.assessed[b.dataset.doneSlug] && !staffMe()) { location.href = assessUrl(b.dataset.doneSlug); return; }
        b.disabled = true;
        const ok = staffMe() && perClass() ? await markTaught(b.dataset.doneSlug) : await Site.toggle(b.dataset.doneSlug);
        b.disabled = false;
        if (!ok) { alert(staffMe() ? "That could not be saved. Has the latest supabase/schema.sql been run?" : "That could not be saved. If this lesson has an assessment, pass it to complete the lesson."); location.reload(); return; }
        document.querySelectorAll(`[data-done-slug="${b.dataset.doneSlug}"]`).forEach(paint);
      });
    });
  }


  // Admin-only controls: [data-role-toggle], [data-role-delete], [data-role-restore] buttons, each holding a slug.
  async function bindRoleToggles() {
    const sel = "[data-role-toggle],[data-role-delete],[data-role-restore]";
    const btns = document.querySelectorAll(sel);
    if (!btns.length || !configured) return;
    await Site.whoami();
    if (!Site.me || !Site.me.is_admin) return;
    const cat = await Site.catalog();
    const slugOf = (b) => b.dataset.roleToggle || b.dataset.roleDelete || b.dataset.roleRestore;
    const paintT = (b) => {
      const r = cat.roles[slugOf(b)];
      if ("roleToggle" in b.dataset) b.textContent = r === "review" ? "Admin: move to Resources" : "Admin: make Chapter review";
      else if ("roleDelete" in b.dataset) b.textContent = "Admin: delete";
      else b.textContent = "Admin: restore";
      b.title = "Only admins see this. It changes the artifact for everyone.";
      const inPill = !!b.closest(".site-pill");
      // On cards, CSS decides which buttons show per tab; in the pill, show by role.
      b.hidden = inPill && ("roleRestore" in b.dataset ? r !== "hidden" : r === "hidden");
    };
    btns.forEach((b) => {
      paintT(b);
      b.addEventListener("click", async (e) => {
        e.preventDefault();
        const slug = slugOf(b), r = cat.roles[slug];
        let next;
        if ("roleDelete" in b.dataset) {
          if (!confirm("Delete this artifact? It disappears for students and from progress. You can restore it from the Deleted tab on its chapter page.")) return;
          next = "hidden";
        } else if ("roleRestore" in b.dataset) next = "resource";
        else next = r === "review" ? "resource" : "review";
        b.disabled = true;
        const ok = await Site.setRole(slug, next);
        b.disabled = false;
        if (!ok) alert("Could not save. Has the artifact_roles SQL been run in Supabase?");
      });
    });
    document.addEventListener("site:rolechange", () => btns.forEach(paintT));
  }

  // Artifact pages: a deleted artifact shows a notice instead of its content (admins get a banner).
  async function guardHidden() {
    const pill = document.querySelector(".site-pill [data-role-toggle]");
    if (!pill || !configured) return;
    const slug = pill.dataset.roleToggle;
    await Site.whoami();
    const cat = await Site.catalog();
    if (cat.roles[slug] !== "hidden") return;
    if (Site.me && Site.me.is_admin) {
      const bar = document.createElement("div");
      bar.style.cssText = "position:sticky;top:0;z-index:2147483000;background:#b3372f;color:#fff;padding:8px 14px;font:600 14px -apple-system,sans-serif";
      bar.textContent = "Deleted: students cannot see this. Use the pill at bottom right to restore.";
      document.body.prepend(bar);
    } else {
      document.body.innerHTML = '<div style="max-width:460px;margin:12vh auto;padding:24px;font:16px/1.5 -apple-system,Segoe UI,sans-serif"><h2>This activity has been removed</h2><p><a href="' + base + '">Back to the site</a></p></div>';
    }
  }

  // Teacher notification bell, to the right of Profile in the navbar.
  Site.refreshBell = async () => {
    const nav = document.querySelector("nav.main");
    if (!nav || !Site.me || !Site.me.is_admin) return;
    const { data } = await sb.rpc("admin_notifications");
    const n = data ? (data.approvals || 0) + (data.retakes || 0) + (data.resets || 0) : 0;
    let a = nav.querySelector(".bell");
    if (!a) {
      a = document.createElement("a");
      a.className = "bell"; a.href = Site.profileUrl;
      a.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 3a6 6 0 0 0-6 6v3.5L4.5 16h15L18 12.5V9a6 6 0 0 0-6-6zm-2 15a2 2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><b></b>';
      a.addEventListener("click", () => { try { sessionStorage.setItem("site.admintab", "approvals"); } catch (e) {} });
      nav.appendChild(a);
    }
    a.querySelector("b").textContent = n || "";
    a.title = n ? `${data.approvals || 0} subject request(s), ${data.retakes || 0} retake request(s), ${data.resets || 0} password reset(s)` : "No notifications";
    a.classList.toggle("has", n > 0);
  };
  // The "Plans" link in the navbar follows who pays: signed-in individuals and licence holders get "My plan",
  // students placed by a school or tutor, and co-teachers, have no plan to manage so the link goes away.
  Site.adaptNav = () => {
    const a = document.querySelector('nav.main a[href$="pricing/"]');
    if (!a || !Site.me || a.classList.contains("on")) return;
    const m = Site.me, v = m.plan_view || (m.is_admin ? "admin" : m.is_school_teacher ? "licence" : m.is_teacher ? "none" : m.school ? "managed" : "individual");
    if (v === "managed" || v === "none") a.hidden = true;
    else if (v !== "admin") { a.textContent = "My plan"; a.href = base + "plan/"; }
  };
  async function startBell() { if (configured) { await Site.whoami(); Site.adaptNav(); Site.refreshBell(); } }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", startBell); else startBell();

  const start = () => { bindButtons(); bindRoleToggles(); guardHidden(); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
