# Inflation Top-100 — research plan

Each round (every ~30 min) adds 10 new stocks to `candidates.json`; `scripts/rank_inflation.py`
re-ranks everything and rewrites `TOP100.md`. Rounds dig progressively deeper into
smaller, less-covered and non-US names.

| Round | Focus |
|---|---|
| 1 | Broad sweep: energy, precious metals, base/critical metals, agri & shipping, real assets & pricing power |
| 2 | Under-covered gold/silver/copper producers on TSX/TSXV/ASX/AIM; North Sea & Canadian oil small caps |
| 3 | Shipping deep dive (Oslo, Athens, US-listed Greek owners) + LatAm commodity exporters with USD revenue |
| 4 | Asia/Japan: trading houses, Asian miners & energy names selling in USD |
| 5 | Land, royalty & water owners (Permian minerals, timber, farmland), oil & gas royalty trusts |
| 6 | Coal (met & thermal: US, Australia, Indonesia) + potash/phosphate juniors in production |
| 7 | Oilfield services & offshore drillers (international, under-covered) |
| 8 | Financials that earn more with higher rates (P&C insurers with float, brokers, exchanges) |
| 9 | Uranium/nuclear fuel cycle, silver pure-plays, PGMs (South Africa) |
| 10 | Wildcard sweep: lowest PEG names across every theme not yet covered |

Tickers already in the database must not be re-added; later rounds may refresh data for existing names.

## Bench
`bench.json` holds names that were researched but did not make the cut (or had incomplete data).
Later rounds may refresh and promote them. Round-1 leads still to research: Yara, 3tentos (TTEN3),
SLC Agricola, LSB Industries, Torex Gold, Equinox Gold, West African Resources, G Mining Ventures,
Commercial Metals, Atalaya Mining, Adecoagro, JBS, Okeanis Eco Tankers.
