#!/usr/bin/env python3
"""Append one research round's picks to candidates.json.

Usage: python3 scripts/add_round.py <round_number> <picks.json>

Forward P/Es are recomputed as price / EPS (price and EPS must share a currency),
and tickers already in the database are skipped.
"""
import json
import sys
from pathlib import Path

CANDIDATES = Path(__file__).resolve().parent.parent / "research" / "inflation-top100" / "candidates.json"


def main():
    rnd, picks_path = int(sys.argv[1]), Path(sys.argv[2])
    db = json.loads(CANDIDATES.read_text())
    have = {s["ticker"] for s in db}
    added = []
    for s in json.loads(picks_path.read_text()):
        if s["ticker"] in have:
            print(f"skip {s['ticker']}: already in database")
            continue
        price = s.get("price")
        s["fwd_pe"] = [round(price / e, 1) if price and isinstance(e, (int, float)) and e > 0 else None
                       for e in s.get("eps") or []]
        s["round_added"] = rnd
        db.append(s)
        added.append(s["ticker"])
    CANDIDATES.write_text(json.dumps(db, indent=1, ensure_ascii=False))
    print(f"round {rnd}: added {len(added)} -> {', '.join(added)} (database now {len(db)})")


if __name__ == "__main__":
    main()
