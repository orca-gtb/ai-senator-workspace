#!/usr/bin/env python3
"""senator: CLI Senator Media Works (F0). Hanya stdlib.

  senator validate            cek registry (termasuk aturan BUILD TO PRODUCE untuk modul)
  senator status              slate: proyek per tahap, gerbang yang menunggu Nanda
  senator metrics             waktu riset-ke-publikasi, biaya per konten, kelulusan gerbang, ROI
  senator finance             jembatan target surplus: biaya langganan -> pendapatan kotor -> views
  senator new <id> <property> "<judul>"   daftarkan proyek baru (mulai di S0, QG0 pending)
"""
import argparse, json, sys, time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = ROOT / "registry"
STAGES = [f"S{i}" for i in range(10)]
GATES = [f"QG{i}" for i in range(7)]
GATE_STATUS = {"pass", "fail", "pending"}
PROJECT_KEYS = {"id", "property", "title", "stage", "gates", "dates", "credits_used", "revenue_idr", "cost_idr", "notes"}
MODULE_KEYS = ("need", "evidence", "kpi")
# gerbang yang wajib lolos sebelum tahap tertentu dimasuki (urutan pipeline)
GATE_BEFORE_STAGE = {"S1": "QG0", "S7": "QG4", "S8": "QG5"}


def load(p, reg=None):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def registry(reg=REG):
    reg = Path(reg)
    return {
        "properties": load(reg / "properties.json")["properties"],
        "budget": load(reg / "budget.json"),
        "revenue": load(reg / "revenue.json")["entries"],
        "modules": load(reg / "modules.json")["modules"],
        "projects": [load(f) for f in sorted((reg / "projects").glob("*.json"))],
        "studios": {f.stem: load(f) for f in (reg / "studios").glob("*.json")},
    }


def validate(R):
    """Kembalikan daftar error (kosong = valid)."""
    E = []
    pids = {p["id"] for p in R["properties"]}
    for pr in R["properties"]:
        if pr["id"] not in R["studios"]:
            E.append(f"property {pr['id']}: registry/studios/{pr['id']}.json tidak ada")
    seen = set()
    for p in R["projects"]:
        pid = p.get("id", "?")
        miss = PROJECT_KEYS - set(p)
        if miss:
            E.append(f"project {pid}: field kurang {sorted(miss)}")
            continue
        if pid in seen:
            E.append(f"project {pid}: id ganda")
        seen.add(pid)
        if p["property"] not in pids:
            E.append(f"project {pid}: property '{p['property']}' tidak terdaftar")
        if p["stage"] not in STAGES:
            E.append(f"project {pid}: stage '{p['stage']}' tidak valid")
            continue
        for g, st in p["gates"].items():
            if g not in GATES:
                E.append(f"project {pid}: gerbang '{g}' tidak dikenal")
            if st not in GATE_STATUS:
                E.append(f"project {pid}: status gerbang {g}='{st}' tidak valid")
        si = STAGES.index(p["stage"])
        for stage, gate in GATE_BEFORE_STAGE.items():
            if si >= STAGES.index(stage) and p["gates"].get(gate) != "pass":
                E.append(f"project {pid}: di {p['stage']} tetapi {gate} belum pass")
        if p["dates"].get("published") and p["gates"].get("QG5") != "pass":
            E.append(f"project {pid}: sudah publish tanpa QG5 pass")
        if p.get("revenue_idr") not in (None, 0) and not p["dates"].get("published"):
            E.append(f"project {pid}: ada pendapatan tetapi belum ditandai publish")
    # BUILD TO PRODUCE: modul wajib terikat kebutuhan produksi nyata
    for m in R["modules"]:
        for k in MODULE_KEYS:
            if not str(m.get(k, "")).strip():
                E.append(f"module {m.get('id', '?')}: field '{k}' kosong (aturan BUILD TO PRODUCE)")
    b = R["budget"]
    if b["allocation"].get("wh", 0) + b["allocation"].get("sk", 0) > 1.0001:
        E.append("budget: alokasi kredit lebih dari 100%")
    return E


def days(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


def project_metrics(R):
    rows = []
    for p in R["projects"]:
        d = p["dates"]
        lead = days(d["research_start"], d["published"]) if d.get("research_start") and d.get("published") else None
        gs = [v for v in p["gates"].values() if v != "pending"]
        rows.append({
            "id": p["id"], "lead_days": lead, "credits": p.get("credits_used"),
            "gate_pass": (sum(v == "pass" for v in gs), len(gs)),
            "cost_idr": p.get("cost_idr"), "revenue_idr": p.get("revenue_idr") or 0,
        })
    return rows


def credit_cost_idr(R):
    b = R["budget"]; pl = b["plan"]
    if not pl.get("credits_month"):
        return None
    return pl["usd_month"] * b["fx_idr_per_usd"] / pl["credits_month"]


def finance(R):
    b = R["budget"]; sub = b["plan"]["usd_month"] * b["fx_idr_per_usd"]
    need = sub + b["target_surplus_idr_month"]
    out = {"sub_idr": sub, "target_surplus": b["target_surplus_idr_month"], "gross_needed_idr": need, "scenarios": []}
    for rpm in b["rpm_scenarios_usd"]:
        usd = need / b["fx_idr_per_usd"]
        out["scenarios"].append({"rpm_usd": rpm, "monetized_views": usd / rpm * 1000})
    return out


def rp(n):
    return "n/a" if n is None else "Rp{:,.0f}".format(n).replace(",", ".")


def cmd_validate(a):
    R = registry(); E = validate(R)
    for e in E:
        print("GAGAL ", e)
    n = len(R["projects"]); m = len(R["modules"])
    print(("OK" if not E else f"{len(E)} error") + f" | {len(R['properties'])} property, {n} proyek, {m} modul")
    return 1 if E else 0


def cmd_status(a):
    R = registry(); b = R["budget"]["credits_now"]
    left = b["limit"] - b["used"]
    print(f"Kredit suara: {left:,} / {b['limit']:,} (per {b['date']}), reset {time.strftime('%d %b %Y', time.gmtime(b['reset_unix']))}".replace(",", "."))
    print("Gerbang: ✓ lolos  · menunggu  ✗ gagal")
    print(f"{'PROYEK':18} {'TAHAP':6} {'GERBANG':34} CATATAN")
    waiting = []
    for p in R["projects"]:
        g = " ".join(f"{k}{ {'pass': '✓', 'fail': '✗', 'pending': '·'}[v]}" for k, v in p["gates"].items())
        print(f"{p['id']:18} {p['stage']:6} {g:34} {p['notes'][:60]}")
        for k in ("QG0", "QG5"):
            if p["gates"].get(k) == "pending" and (k == "QG0" or p["stage"] in ("S7", "S8")):
                waiting.append(f"{p['id']} menunggu {k} (Nanda)")
    print("Menunggu keputusan Nanda:" if waiting else "Tidak ada gerbang manusia yang menunggu.")
    for w in waiting:
        print("  -", w)
    return 0


def cmd_metrics(a):
    R = registry(); rows = project_metrics(R); cc = credit_cost_idr(R)
    print(f"{'PROYEK':16} {'RISET→PUBLISH':14} {'KREDIT':8} {'GERBANG':10} {'BIAYA KREDIT':14} {'PENDAPATAN':12}")
    tot_rev = 0; tot_cost = 0; known = True
    for r in rows:
        cost = r["credits"] * cc if (cc is not None and r["credits"] is not None) else None
        tot_rev += r["revenue_idr"]
        if cost is None: known = False
        else: tot_cost += cost
        gp = f"{r['gate_pass'][0]}/{r['gate_pass'][1]}" if r["gate_pass"][1] else "n/a"
        lead = "n/a" if r["lead_days"] is None else f"{r['lead_days']} hari"
        print(f"{r['id']:16} {lead:14} {str(r['credits'] if r['credits'] is not None else 'n/a'):8} {gp:10} {rp(cost):14} {rp(r['revenue_idr']):12}")
    sub = R["budget"]["plan"]["usd_month"] * R["budget"]["fx_idr_per_usd"]
    ledger = sum(e["amount_idr"] for e in R["revenue"])
    print(f"\nPendapatan tercatat (ledger): {rp(ledger)} | langganan/bulan: {rp(sub)} | surplus bulan ini: {rp(ledger - sub)}")
    if cc is None:
        print("Catatan: biaya per kredit n/a sampai budget.json plan.credits_month diisi (saat membeli paket).")
    if not known:
        print("Catatan: n/a = belum tercatat. Tidak diisi dengan tebakan.")
    return 0


def cmd_finance(a):
    R = registry(); f = finance(R); b = R["budget"]
    print(f"Langganan {b['plan']['name']}: ${b['plan']['usd_month']}/bln × Rp{b['fx_idr_per_usd']:,}/USD = {rp(f['sub_idr'])}  ({b['fx_note']})".replace(",", "."))
    print(f"Target surplus setelah langganan:        {rp(f['target_surplus'])}")
    print(f"Pendapatan kotor yang dibutuhkan/bulan:  {rp(f['gross_needed_idr'])}")
    print("Views berpendapatan iklan yang dibutuhkan/bulan (ASUMSI RPM, ganti dengan data Studio):")
    for s in f["scenarios"]:
        print(f"  RPM ${s['rpm_usd']}: {s['monetized_views']:,.0f} views".replace(",", "."))
    print("Catatan:", b["rpm_note"])
    print("Iklan YouTube baru ada setelah YPP aktif. Sebelum itu pendapatan = 0 kecuali affiliate/sponsor/produk.")
    return 0


def cmd_new(a):
    R = registry()
    if a.property not in {p["id"] for p in R["properties"]}:
        print("property tidak dikenal:", a.property); return 1
    f = REG / "projects" / f"{a.id}.json"
    if f.exists():
        print("sudah ada:", a.id); return 1
    p = {"id": a.id, "property": a.property, "title": a.title, "stage": "S0", "gates": {"QG0": "pending"},
         "dates": {"research_start": None, "published": None}, "credits_used": 0, "revenue_idr": 0, "cost_idr": None, "notes": "baru; menunggu QG0 (Nanda)"}
    f.write_text(json.dumps(p, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("terdaftar:", f.relative_to(ROOT)); return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="senator"); sp = ap.add_subparsers(dest="cmd", required=True)
    for n, fn in (("validate", cmd_validate), ("status", cmd_status), ("metrics", cmd_metrics), ("finance", cmd_finance)):
        sp.add_parser(n).set_defaults(fn=fn)
    n = sp.add_parser("new"); n.add_argument("id"); n.add_argument("property"); n.add_argument("title"); n.set_defaults(fn=cmd_new)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
