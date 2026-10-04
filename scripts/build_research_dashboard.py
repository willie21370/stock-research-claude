#!/usr/bin/env python3
"""Rebuild the deep-research dashboard page from research/deep-research/results/*.json.

Each results file is written by one research run:
  {"ticker","name","price","currency","upside_36m_pct","overall_score","scorecard","likelihood","advice","report"}
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "research" / "deep-research"


def slug(ticker):
    return re.sub(r"[^A-Za-z0-9]+", "_", ticker).strip("_")


def main():
    queue = json.loads((ROOT / "queue.json").read_text())
    done = {}
    for f in (ROOT / "results").glob("*.json"):
        r = json.loads(f.read_text())
        done[r["ticker"]] = r
    rows = []
    for q in queue:
        r = done.get(q["ticker"])
        rows.append({
            "rank": q["rank"], "ticker": q["ticker"], "name": q["name"],
            "batch": (q["rank"] - 1) // 10 + 1,
            "done": r is not None and (ROOT / "reports" / f"{slug(q['ticker'])}.html").exists(),
            "upside": r and r.get("upside_36m_pct"), "overall": r and r.get("overall_score"),
            "scorecard": r and r.get("scorecard"), "likelihood": r and r.get("likelihood"),
            "advice": r and r.get("advice"), "href": f"reports/{slug(q['ticker'])}.html",
        })
    n_done = sum(r["done"] for r in rows)
    page = (ROOT / "dashboard_template.html").read_text()
    page = page.replace("__DATA__", json.dumps(rows)).replace("__DONE__", str(n_done)).replace("__TOTAL__", str(len(rows)))
    (ROOT / "index.html").write_text(page)
    print(f"dashboard: {n_done}/{len(rows)} reports")


if __name__ == "__main__":
    main()
