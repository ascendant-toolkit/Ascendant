// Admin "Customers" tab: customers, orders, timeline and notes, all in Supabase (see supabase/crm_schema.sql).
(function () {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => (d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "");
  const money = (c, cur) => (c / 100).toLocaleString("en-US", { style: "currency", currency: cur || "USD" });
  const KINDS = ["student", "parent", "teacher", "school", "tutor", "other"];
  const STATUSES = ["lead", "active", "lapsed", "churned"];
  const SOURCES = ["manual", "waitlist", "contact", "checkout", "school", "referral", "import"];
  const ORDER_STATUS = ["paid", "pending", "refunded", "cancelled", "failed"];
  const PLANS = ["", "monthly", "annual", "seasonal", "school", "one-off"];
  const EVENT_TYPES = ["note", "email", "call", "contact", "signup", "grant", "revoke", "renewal", "cancel", "other"];
  const opts = (list, cur) => list.map((v) => `<option value="${esc(v)}" ${v === cur ? "selected" : ""}>${esc(v || "none")}</option>`).join("");

  window.AdminCRM = {
    async render(host, sb) {
      const $ = (s, r = host) => r.querySelector(s);
      const say = (el, t, ok) => { el.textContent = t; el.className = "msg " + (ok ? "ok" : "err"); el.hidden = !t; };
      let rows = [], products = [], filter = { q: "", status: "", kind: "" };

      async function load() {
        const [c, p] = await Promise.all([sb.from("customer_summary").select("*").order("created_at", { ascending: false }), sb.from("products").select("id,title").order("id")]);
        if (c.error) throw c.error;
        rows = c.data || []; products = p.data || [];
      }

      function shell() {
        const paid = rows.reduce((a, r) => a + (r.spent_cents || 0), 0);
        const stat = (n, l) => `<div class="card block" style="flex:1;min-width:120px"><b style="font-size:1.4rem">${n}</b><br><span class="hint">${l}</span></div>`;
        host.innerHTML = `
          <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:10px">${stat(rows.length, "customers")}${stat(rows.filter((r) => r.status === "active").length, "active")}
            ${stat(rows.filter((r) => r.status === "lead").length, "leads")}${stat(rows.reduce((a, r) => a + r.order_count, 0), "orders")}${stat(money(paid), "net revenue (USD-equivalent, unconverted)")}</div>
          <div class="row" style="margin-top:12px;gap:8px;flex-wrap:wrap"><input id="crm-q" placeholder="Search name, email, org, tag" style="flex:1;min-width:180px" value="${esc(filter.q)}">
            <select id="crm-st"><option value="">All statuses</option>${opts(STATUSES, filter.status)}</select>
            <select id="crm-kd"><option value="">All types</option>${opts(KINDS, filter.kind)}</select>
            <button class="mini" id="crm-add">New customer</button><button class="mini" id="crm-imp">Import from site</button><button class="mini" id="crm-csv">Export CSV</button></div>
          <p class="msg" id="crm-msg" hidden></p><div id="crm-list"></div>
          <dialog id="crm-dlg" class="wide"><div id="crm-body"></div></dialog>`;
        list();
        $("#crm-q").addEventListener("input", (e) => { filter.q = e.target.value; list(); });
        $("#crm-st").addEventListener("change", (e) => { filter.status = e.target.value; list(); });
        $("#crm-kd").addEventListener("change", (e) => { filter.kind = e.target.value; list(); });
        $("#crm-add").addEventListener("click", () => detail(null));
        $("#crm-imp").addEventListener("click", async () => {
          const { data, error } = await sb.rpc("admin_crm_import");
          if (error) return say($("#crm-msg"), error.message, false);
          await refresh(); say($("#crm-msg"), `Imported ${data} new customer${data === 1 ? "" : "s"}.`, true);
        });
        $("#crm-csv").addEventListener("click", () => {
          const cols = ["email", "name", "kind", "org", "country", "status", "source", "order_count", "spent_cents", "last_order_at", "created_at"];
          const q = (v) => `"${String(v ?? "").replace(/"/g, '""')}"`;
          const csv = [cols.join(","), ...visible().map((r) => cols.map((c) => q(r[c])).join(","))].join("\n");
          const a = document.createElement("a");
          a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" })); a.download = "customers.csv"; a.click();
        });
      }

      const visible = () => {
        const q = filter.q.trim().toLowerCase();
        return rows.filter((r) => (!filter.status || r.status === filter.status) && (!filter.kind || r.kind === filter.kind) &&
          (!q || [r.name, r.email, r.org, (r.tags || []).join(" ")].join(" ").toLowerCase().includes(q)));
      };

      function list() {
        const v = visible();
        $("#crm-list").innerHTML = v.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Customer</th><th>Type</th><th>Status</th><th>Orders</th><th>Spent</th><th>Last activity</th></tr></thead><tbody>
          ${v.map((r) => `<tr data-id="${r.id}" style="cursor:pointer"><td><b>${esc(r.name || "(no name)")}</b><br><span class="hint">${esc(r.email)}${r.org ? " · " + esc(r.org) : ""}</span></td>
            <td>${esc(r.kind)}</td><td>${esc(r.status)}</td><td>${r.order_count}</td><td>${r.spent_cents ? money(r.spent_cents) : ""}</td><td>${fmt(r.last_event_at || r.last_order_at || r.created_at)}</td></tr>`).join("")}</tbody></table></div>`
          : '<p class="hint">No customers match. Use Import from site to pull in students, the waitlist and contact senders.</p>';
        host.querySelectorAll("#crm-list tr[data-id]").forEach((tr) => tr.addEventListener("click", () => detail(+tr.dataset.id)));
      }

      async function refresh() { await load(); shell(); }

      async function detail(id) {
        const dlg = $("#crm-dlg"), body = $("#crm-body");
        const c = id ? rows.find((r) => r.id === id) : { kind: "student", status: "lead", source: "manual", marketing_ok: false, tags: [] };
        let orders = [], events = [], notes = [];
        if (id) {
          const [o, e, n] = await Promise.all([
            sb.from("customer_orders").select("role, orders(*, order_items(*))").eq("customer_id", id),
            sb.from("events").select("*").eq("customer_id", id).order("occurred_at", { ascending: false }).limit(100),
            sb.from("customer_notes").select("*").eq("customer_id", id).order("created_at", { ascending: false })]);
          orders = (o.data || []).filter((x) => x.orders).map((x) => ({ ...x.orders, role: x.role })).sort((a, b) => b.placed_at.localeCompare(a.placed_at));
          events = e.data || []; notes = n.data || [];
        }
        const field = (l, n, v, t = "text") => `<label>${l}<input type="${t}" name="${n}" value="${esc(v)}"></label>`;
        body.innerHTML = `<div class="row"><h3>${id ? esc(c.name || c.email) : "New customer"}</h3><button class="mini" data-close>Close</button></div>
          <form id="crm-f">${field("Name", "name", c.name)}${field("Email", "email", c.email, "email")}
            <div class="row" style="gap:8px;flex-wrap:wrap"><label>Type<select name="kind">${opts(KINDS, c.kind)}</select></label><label>Status<select name="status">${opts(STATUSES, c.status)}</select></label>
            <label>Source<select name="source">${opts(SOURCES, c.source)}</select></label></div>
            ${field("Organisation", "org", c.org)}${field("Country", "country", c.country)}${field("Phone", "phone", c.phone)}${field("Tags (comma separated)", "tags", (c.tags || []).join(", "))}
            <label><input type="checkbox" name="marketing_ok" ${c.marketing_ok ? "checked" : ""}> OK to send marketing email</label>
            <div class="row"><button class="btn" type="submit">${id ? "Save" : "Add customer"}</button>${id ? '<button class="mini danger" type="button" id="crm-del">Delete</button>' : ""}</div><p class="msg" hidden></p></form>
          ${id ? `<h4>Orders (${orders.length})</h4>
            ${orders.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Date</th><th>Items</th><th>Total</th><th>Status</th><th>Role</th></tr></thead><tbody>${orders.map((o) => `<tr>
              <td>${fmt(o.placed_at)}</td><td>${esc((o.order_items || []).map((i) => i.description || [i.product, i.tier].filter(Boolean).join(" ")).join(", "))}</td>
              <td>${money(o.total_cents, o.currency)}${o.refunded_cents ? `<br><span class="hint">refunded ${money(o.refunded_cents, o.currency)}</span>` : ""}</td><td>${esc(o.status)}</td><td>${esc(o.role)}</td></tr>`).join("")}</tbody></table></div>` : '<p class="hint">No orders.</p>'}
            <form id="crm-o" class="inline"><label>Product<select name="product"><option value="">(other)</option>${products.map((p) => `<option value="${esc(p.id)}">${esc(p.title)}</option>`).join("")}</select></label>
              <label>Tier<select name="tier">${opts(["", "basic", "full", "vip"], "")}</select></label><label>Amount<input name="amount" type="number" step="0.01" min="0" required style="width:90px"></label>
              <label>Plan<select name="plan">${opts(PLANS, "")}</select></label><label>Status<select name="ostatus">${opts(ORDER_STATUS, "paid")}</select></label>
              <button class="btn" type="submit">Record order</button><p class="msg" hidden></p></form>
            <h4>Notes</h4><form id="crm-n" class="inline"><label style="flex:1"><textarea name="body" rows="2" required></textarea></label><button class="btn" type="submit">Add note</button></form>
            <ul class="plain">${notes.map((n) => `<li><span class="hint">${fmt(n.created_at)}</span> ${esc(n.body)}</li>`).join("") || '<li class="hint">No notes.</li>'}</ul>
            <h4>Timeline</h4><form id="crm-e" class="inline"><label>Type<select name="type">${opts(EVENT_TYPES, "email")}</select></label><label style="flex:1">Summary<input name="summary" required maxlength="500"></label><button class="btn" type="submit">Log event</button></form>
            <ul class="plain">${events.map((e) => `<li><span class="hint">${fmt(e.occurred_at)} · ${esc(e.type)}</span> ${esc(e.summary)}</li>`).join("") || '<li class="hint">No events.</li>'}</ul>` : ""}`;
        dlg.showModal();
        body.querySelector("[data-close]").addEventListener("click", () => dlg.close());
        const reopen = async () => { await load(); list(); detail(id); };

        $("#crm-f", body).addEventListener("submit", async (e) => {
          e.preventDefault();
          const f = e.target, m = $(".msg", f);
          const v = { name: f.name.value.trim(), email: f.email.value.trim().toLowerCase(), kind: f.kind.value, status: f.status.value, source: f.source.value,
            org: f.org.value.trim() || null, country: f.country.value.trim() || null, phone: f.phone.value.trim() || null, marketing_ok: f.marketing_ok.checked,
            tags: f.tags.value.split(",").map((t) => t.trim()).filter(Boolean) };
          const { error } = id ? await sb.from("customers").update(v).eq("id", id) : await sb.from("customers").insert(v);
          if (error) return say(m, /duplicate/i.test(error.message) ? "That email is already a customer." : error.message, false);
          dlg.close(); refresh();
        });
        if (!id) return;
        $("#crm-del", body).addEventListener("click", async () => {
          if (!confirm(`Delete ${c.email} and their notes and timeline? Orders are kept.`)) return;
          const { error } = await sb.from("customers").delete().eq("id", id);
          if (error) return alert(error.message);
          dlg.close(); refresh();
        });
        $("#crm-o", body).addEventListener("submit", async (e) => {
          e.preventDefault();
          const f = e.target, m = $(".msg", f), cents = Math.round(parseFloat(f.amount.value) * 100);
          const prod = products.find((p) => p.id === f.product.value);
          const o = await sb.from("orders").insert({ status: f.ostatus.value, total_cents: cents, plan: f.plan.value || null, provider: "manual" }).select("id").single();
          if (o.error) return say(m, o.error.message, false);
          const oid = o.data.id, desc = prod ? prod.title : "Manual order";
          const steps = [
            sb.from("order_items").insert({ order_id: oid, product: prod ? prod.id : null, tier: f.tier.value || null, description: desc, unit_cents: cents }),
            sb.from("customer_orders").insert({ customer_id: id, order_id: oid, role: "buyer" }),
            sb.from("events").insert({ customer_id: id, order_id: oid, type: "order", summary: `${desc}, ${money(cents)} (${f.ostatus.value})` })];
          for (const s of steps) { const r = await s; if (r.error) return say(m, r.error.message, false); }
          if (c.status !== "active" && f.ostatus.value === "paid") await sb.from("customers").update({ status: "active" }).eq("id", id);
          reopen();
        });
        $("#crm-n", body).addEventListener("submit", async (e) => {
          e.preventDefault();
          const { error } = await sb.from("customer_notes").insert({ customer_id: id, body: e.target.body.value.trim() });
          if (error) return alert(error.message);
          reopen();
        });
        $("#crm-e", body).addEventListener("submit", async (e) => {
          e.preventDefault();
          const { error } = await sb.from("events").insert({ customer_id: id, type: e.target.type.value, summary: e.target.summary.value.trim() });
          if (error) return alert(error.message);
          reopen();
        });
      }

      try { await load(); shell(); }
      catch (e) { host.innerHTML = `<p class="msg err">Could not load customers: ${esc(e.message)}. Has supabase/crm_schema.sql been run?</p>`; }
    },
  };
})();
