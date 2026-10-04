#!/usr/bin/env python3
"""Rank the inflation-beneficiary stock list and regenerate the Top-100 report.

Data lives in research/inflation-top100/candidates.json (one object per stock).
Run:  python3 scripts/rank_inflation.py            -> rewrites TOP100.md
      python3 scripts/rank_inflation.py --check    -> prints data sanity warnings only

Composite score (0-100):
  35%  inflation benefit   (analyst judgment 1-10)
  25%  valuation           (FY2 forward P/E: 5x -> full marks, 25x+ -> zero)
  20%  EPS growth          (3-yr EPS CAGR, capped at 40%)
  10%  revenue growth      (3-yr revenue CAGR, capped at 25%)
   5%  under-the-radar     (fewer covering analysts = higher)
   5%  data confidence     (high / medium / low)
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "research" / "inflation-top100"
CANDIDATES = DATA_DIR / "candidates.json"
REPORT = DATA_DIR / "TOP100.md"

WEIGHTS = {"inflation": 35, "value": 25, "eps_growth": 20, "rev_growth": 10, "radar": 5, "confidence": 5}


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def num(x):
    return x if isinstance(x, (int, float)) else None


def cagr(start, end, years):
    if start is None or end is None or start <= 0 or end <= 0 or years <= 0:
        return None
    return ((end / start) ** (1 / years) - 1) * 100


def derived(s):
    """Recompute growth rates from raw estimates where possible; fall back to supplied values."""
    eps = s.get("eps") or [None, None, None]
    rev = s.get("rev") or [None, None, None]
    eps0, rev0 = num(s.get("eps_fy0")), num(s.get("rev_fy0"))

    rev_cagr = cagr(rev0, num(rev[2]), 3) if len(rev) > 2 else None
    if rev_cagr is None:
        rev_cagr = num(s.get("rev_cagr_3y_pct"))

    eps_cagr, basis = None, s.get("eps_cagr_basis", "FY0-FY3")
    if len(eps) > 2 and eps0 is not None and eps0 > 0 and num(eps[2]) and eps[2] / eps0 > 0:
        # FY0 must be meaningful (>15% of FY3) or the CAGR explodes from a near-zero base
        if eps0 >= 0.15 * eps[2]:
            eps_cagr, basis = cagr(eps0, eps[2], 3), "FY0-FY3"
    if eps_cagr is None and len(eps) > 2 and num(eps[0]) and num(eps[2]):
        eps_cagr, basis = cagr(eps[0], eps[2], 2), "FY1-FY3"
    if eps_cagr is None:
        eps_cagr = num(s.get("eps_cagr_3y_pct"))

    pe = s.get("fwd_pe") or [None, None, None]
    return {"rev_cagr": rev_cagr, "eps_cagr": eps_cagr, "eps_basis": basis, "pe": [num(p) for p in pe]}


def score(s, d):
    infl = clamp((num(s.get("inflation_score")) or 0) / 10)
    pe2 = d["pe"][1] if len(d["pe"]) > 1 else None
    value = clamp((25 - pe2) / 20) if pe2 and pe2 > 0 else 0.0
    eps_g = clamp((d["eps_cagr"] or 0) / 40)
    rev_g = clamp((d["rev_cagr"] or 0) / 25)
    n = num(s.get("n_analysts"))
    radar = 0.5 if n is None else 1.0 if n <= 3 else 0.7 if n <= 6 else 0.4 if n <= 10 else 0.1
    conf = {"high": 1.0, "medium": 0.6, "low": 0.2}.get(s.get("confidence", "low"), 0.2)
    parts = {"inflation": infl, "value": value, "eps_growth": eps_g, "rev_growth": rev_g, "radar": radar, "confidence": conf}
    return round(sum(WEIGHTS[k] * v for k, v in parts.items()), 1)


def sanity(s):
    """Flag forward P/Es that don't match price / EPS (often a currency mismatch)."""
    warns = []
    price, eps, pe = num(s.get("price")), s.get("eps") or [], s.get("fwd_pe") or []
    for i, (e, p) in enumerate(zip(eps, pe)):
        if price and num(e) and e > 0 and num(p):
            implied = price / e
            if abs(implied - p) / p > 0.15:
                warns.append(f"{s['ticker']}: FY{i+1} P/E {p} vs price/EPS {implied:.1f} (currency mismatch?)")
    return warns


def fmt(x, suffix="", nd=1):
    return "n/a" if x is None else f"{x:.{nd}f}{suffix}"


def main():
    stocks = json.loads(CANDIDATES.read_text())
    warns = [w for s in stocks for w in sanity(s)]
    if "--check" in sys.argv:
        print("\n".join(warns) or "no warnings")
        return

    rows = []
    for s in stocks:
        d = derived(s)
        rows.append((score(s, d), s, d))
    rows.sort(key=lambda r: r[0], reverse=True)
    rows = rows[:100]

    rounds = max(s.get("round_added", 1) for s in stocks)
    out = [
        "# Top-100 Inflation Beneficiaries — Cheap & Fast-Growing",
        "",
        f"_Last updated: {date.today().isoformat()} · research round {rounds} · {len(stocks)} stocks in database_",
        "",
        "> Research output, not investment advice. Estimates are analyst consensus gathered from public",
        "> search results and may be stale or incomplete; check every number before acting on it.",
        "",
        "**Score (0-100)** = 35% inflation benefit · 25% valuation (FY2 P/E) · 20% 3-yr EPS CAGR ·",
        "10% 3-yr revenue CAGR · 5% under-the-radar (few analysts) · 5% data confidence.",
        "",
        "| # | Ticker | Company | Country | Theme | Score | Infl. | Rev CAGR 3y | EPS CAGR 3y | P/E FY1 | P/E FY2 | P/E FY3 | Analysts | Added |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, (sc, s, d) in enumerate(rows, 1):
        pe = d["pe"] + [None] * (3 - len(d["pe"]))
        eps_c = fmt(d["eps_cagr"], "%") + (" ¹" if d["eps_basis"] != "FY0-FY3" else "")
        out.append(
            f"| {i} | {s['ticker']} ({s.get('exchange','')}) | {s['name']} | {s.get('country','')} | {s.get('theme','')} "
            f"| **{sc}** | {s.get('inflation_score','')}/10 | {fmt(d['rev_cagr'], '%')} | {eps_c} "
            f"| {fmt(pe[0], 'x')} | {fmt(pe[1], 'x')} | {fmt(pe[2], 'x')} | {s.get('n_analysts') or 'n/a'} | R{s.get('round_added', 1)} |"
        )
    out += ["", "¹ EPS CAGR measured FY1→FY3 (2 years) because the base-year EPS was negative or near zero.", ""]

    out += ["## Why each stock benefits from US inflation", ""]
    for i, (sc, s, d) in enumerate(rows, 1):
        fy = s.get("fy_years") or ["FY1", "FY2", "FY3"]
        eps = s.get("eps") or []
        eps_str = ", ".join(f"{y}: {fmt(num(e), '', 2)}" for y, e in zip(fy, eps))
        out += [
            f"### {i}. {s['name']} — {s['ticker']} ({s.get('exchange','')}, {s.get('country','')}) · score {sc}",
            "",
            f"- **Why inflation helps:** {s.get('inflation_thesis','')}",
            f"- **Key risks:** {s.get('key_risks','')}",
            f"- **Price:** {s.get('price')} {s.get('currency','')} ({s.get('price_date','')}) · "
            f"mkt cap ~${fmt(num(s.get('market_cap_usd_bn')), 'bn')} · consensus EPS {eps_str}",
            f"- **Data confidence:** {s.get('confidence','')}" + (f" · {s['notes']}" if s.get("notes") else ""),
            "- **Sources:** " + ", ".join(f"[{j+1}]({u})" for j, u in enumerate(s.get("sources", [])[:4])),
            "",
        ]
    REPORT.write_text("\n".join(out))
    print(f"wrote {REPORT.relative_to(ROOT)} with {len(rows)} stocks")
    if warns:
        print("sanity warnings:\n  " + "\n  ".join(warns))


if __name__ == "__main__":
    main()
