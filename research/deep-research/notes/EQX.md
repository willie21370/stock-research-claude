# Equinox Gold (TSX / NYSE American: EQX) — research notes (as of 2026-10-04)

Research method: WebSearch snippets only. Direct fetches of sec.gov, equinoxgold.com, globenewswire, stockanalysis, marketbeat, yahoo, miningweekly, pulse2, wtop, stocktitan and edgex were all blocked by the egress proxy. The session-wide web-search budget ran out after 20 queries, so many microstructure items are gaps. Every figure below carries its source, and gaps are listed explicitly.

## Q1. Price, share count, market cap

### Takeaway
EQX closed at US$11.11 on NYSE American on 2 Oct 2026 (TSX C$15.83). There were 1,135.1M basic shares after the Orla merger closed on 31 Jul 2026, and the in-the-money 4.75% converts (27.4M shares) are being forced into conversion by 19–20 Oct 2026.

### Cited Findings
- EQX closed at US$11.11 on 2 Oct 2026, +$0.29 (+2.68%). TSX C$15.83 (+2.86%). 52-week range $8.48–$18.96. TSX market cap C$18.481B. The move followed a late-September sector selloff. — [Yahoo Finance / CNBC / TradingView quote aggregation via search](https://finance.yahoo.com/quote/EQX/)
- US$12.45 on 18 Sep 2026; 52-week high of $18.96 set on 25 Feb 2026; weeks ending 4 Sep and 11 Sep were −1.4% and −3.2% — [chartrow weekly returns](https://chartrow.com/quote/eqx/weekly-returns), [Weiss Ratings](https://weissratings.com/en/instant-news-alerts/equinox-gold-corp-eqx-down-4-6-is-it-time-to-ditch-this-stock)
- One snippet says "in July 2026 the stock was trading at $8.76" (unconfirmed; consistent with the $8.48 52-week low) — [digrin price history](https://www.digrin.com/stocks/detail/EQX/price)
- 1,135.1M shares issued and outstanding after the merger. Up to 421,770,377 shares issued to Orla holders at 1.00 EQX per Orla share plus US$0.0001 cash. Ownership split ~67% EQX / ~33% Orla on a fully diluted in-the-money basis — [EQX Fact Sheet Aug 2026](https://www.equinoxgold.com/wp-content/uploads/2026/07/EQX-Fact-Sheet-Aug-2026.pdf), [Placera / shareholder approval release](https://www.placera.se/pressmeddelanden/equinox-gold-equinox-gold-shareholders-approve-business-combination-with-orla-mining-20260722)
- Screening file (stale): US$11.82 on 15 Sep 2026, market cap US$9.33bn. That cap is on the PRE-merger share count, so it is wrong post-merger — `research/inflation-top100/candidates.json`

### Inferences
- Pre-merger shares ≈ 1,135.1 − 421.8 = 713.3M (DERIVED).
- Diluted after convert conversion ≈ 1,135.1 + 27.4 = 1,162.5M (DERIVED). Diluted market cap ≈ US$12.9bn.
- Cross-check: TSX cap C$18.481B ÷ C$15.83 = 1,167M shares implied (DERIVED), consistent with ~1,162–1,167M.
- Implied USD/CAD = 15.83 / 11.11 = 1.425.

### Gaps
- ADV, short interest, days to cover, borrow fee, institutional ownership and 13F direction: not found (search budget exhausted).
- Option and RSU count after the merger: not found.

## Q2. Latest results (Q2 2026) and guidance

### Takeaway
Q2 2026 operations were solid but earnings missed: adjusted EPS of $0.16 against a $0.27 consensus (−40.7%). AISC was $2,175/oz. 2026 guidance was raised to 870–920koz (including 5 months of Orla) at AISC of $1,900–2,000.

### Cited Findings
- Q2 2026: production 176,836 oz; sold 177,959 oz at a realized $4,256/oz; revenue $769.8M; adjusted EBITDA $358.3M; net income $230.6M; Canadian production +11% q/q — [Quartr](https://quartr.com/events/equinox-gold-corp-eqx-q2-2026_3PhAxtMQ), [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/07/10/equinox-gold-reports-176836-ounces-of-gold-production-in-q2-2026-canadian-gold-production-increased-11-quarter-over-quarter/)
- Q2 adjusted net income $123.3M ($0.16/sh) vs $0.27 estimate (−40.7% surprise) — [Quiver Quant / Zacks-style snapshot](https://www.quiverquant.com/news/Equinox+Gold+Corp.+%28EQX%29+Releases+Q2%202026%20Earnings%3A%20Revenue%20and%20Profit%20Surge)
- Q2 cash costs $1,816/oz; AISC $2,175/oz; mine-site FCF before WC $223.7M — [Q2 call highlights](https://www.thecerbatgem.com/?p=10344092)
- Updated 2026 guidance: 870–920koz (12 months legacy + 5 months Musselwhite and Camino Rojo; closing 31 Jul); pro forma ~1.1Moz; cash costs $1,600–1,700; AISC $1,900–2,000 — [Barchart/Orla](https://www.barchart.com/story/news/3200309/orla-mining-reports-strong-second-quarter-operating-results), [IRW-Press release copy](https://irw-press.com/en/equinox-gold-delivers-strong-second-quarter-results-increases-2026-production-guidance-following-successful-completion-of-the-orla-mining-merger-quarterly-dividend-increased-by-50-2/)
- 2026 growth capex guidance $600–650M, including South Railroad $70–80M, Los Filos $35–40M and Valentine Phase 2 $50–60M; $105–120M for studies, engineering and procurement — [SEC 6-K Q2 MD&A (snippet)](https://www.sec.gov/Archives/edgar/data/0001756607/000175660726000004/eqx-20260630mda.htm)
- Original (Feb 2026) legacy guidance: 700–800koz, cash cost $1,425–1,525, AISC $1,775–1,875. By mine: Greenstone 250–300koz (AISC $1,750–1,850); Valentine 150–200koz (AISC $1,200–1,300); Nicaragua 200–250koz (AISC $2,100–2,200); Mesquite 70–80koz (AISC $2,300–2,400) — [SEC 6-K (snippet)](https://www.sec.gov/Archives/edgar/data/1756607/000117184326000248/exh_991.htm)
- Quarterly dividend raised 50% to $0.09/sh. Inaugural dividend announced with FY2025 results — [Mining Weekly](https://www.miningweekly.com/article/equinox-approves-50-quarterly-dividend-increase-after-orla-merger-2026-08-06), [Barchart FY2025](https://www.barchart.com/story/news/292229/equinox-gold-delivers-transformational-year-with-strategic-merger-record-production-and-revenue-portfolio-optimization-more-than-us1-1-billion-in-debt-reduction-and-announces-inaugural-dividend)
- CEO succession: Darren Hall retires in Oct 2026 and Jason Simpson (ex-Orla CEO) becomes CEO — [Quartr](https://quartr.com/events/equinox-gold-corp-eqx-q2-2026_3PhAxtMQ)

### Inferences
- Q2 EBITDA-to-adjusted-NI conversion was only 34%, which implies heavy D&A of about $850–950/oz (Greenstone, plus purchase-price step-ups). House D&A is $850/oz in 2026 and $800/oz from 2027 (ASSUMED).
- H2-26 cash cost implied by the full-year midpoint ≈ $1,557/oz (DERIVED: (1,650×895 − 1,800×342)/553).

### Gaps
- Q1 2026 adjusted EPS and the per-mine split of updated guidance (Musselwhite, Camino Rojo): not retrieved.
- Last 8 quarters of guidance beat/miss: only Q2-26 (EPS −40.7%) was found.

## Q3. Balance sheet and debt

### Takeaway
Net debt fell sharply after the Brazil sale. At 30 Jun 2026, legacy net debt was $265.2M including converts. Pro forma liquidity is about $1.21bn, and the converts are being forced into equity.

### Cited Findings
- 30 Jun 2026: cash (unrestricted) $317.8M; total debt $583.0M (current $29.1M, non-current $553.9M); net debt $265.2M. Available liquidity ≈ $1,214M = combined cash $729M (30 Jun) + $485M undrawn RCF (31 Jul) — [Q2 MD&A / news release (snippet)](https://www.sec.gov/Archives/edgar/data/1756607/000175660726000004/eqx-20260630mda.htm)
- Q1 2026: net debt $77M excluding converts at 30 Apr; cash $363M at 31 Mar; drawn debt $440M; undrawn RCF $560M; liquidity $923M; repaid $990M of debt in Q1 after the Brazil sale closed (Jan 2026); RCF refinanced on improved terms — [Q1 deck via MarketScreener](https://www.marketscreener.com/news/equinox-gold-webcast-deck-20260507-eqx-q1-conference-call-deck-final-ce7f58d2d080f72c), [Brazil sale complete](https://www.equinoxgold.com/wp-content/uploads/2026/01/20260123-EQX-Brazil-Operations-Sale-Complete-News-Release-Final.pdf)
- FY2025: more than US$1.1bn of debt reduction — [Barchart](https://www.barchart.com/story/news/292229/)
- 4.75% convertible senior notes due 15 Oct 2028: $172.5M called for redemption on 20 Oct 2026 (conversion deadline 19 Oct, 5pm NY); 158.7302 shares per $1,000 (conversion price ≈ $6.30); redemption price ≈ $1,000.66 per $1,000 — [BNN Bloomberg 21 Sep 2026](https://www.bnnbloomberg.ca/press-releases/2026/09/21/equinox-gold-announces-redemption-of-its-outstanding-475-convertible-senior-notes-due-october-2028/), [Finviz](https://finviz.com/news/393707/)

### Inferences
- RCF size ≈ $1.0bn (DERIVED: 440 + 560 at 30 Apr). Drawn ≈ $515M at 31 Jul if the size is unchanged (DERIVED: 1,000 − 485).
- Converts: 172.5 × 158.73 = 27.38M new shares. They are deep in the money ($11.11 vs $6.30), so near-full conversion is expected.
- Pro forma gross debt ex-converts ≈ $560M (ASSUMED: ~$515M RCF + ~$45M equipment loans) vs cash $729M, giving net cash ≈ $170M (DERIVED/ASSUMED).

### Gaps
- RCF maturity date, covenants and pricing; Orla debt repaid at closing; hedge book; streams/royalties.

## Q4. Merger, assets, reserves, growth

### Cited Findings
- At-market merger with Orla announced in May 2026, implied combined market cap ~$18.5bn (currency not stated; consistent with CAD); closed 31 Jul 2026 — [Pulse 2.0](https://pulse2.com/equinox-gold-and-orla-mining-18-5-billion-combination-creates-new-north-american-senior-gold-producer/), [Skillings](https://skillings.net/equinox-gold-and-orla-mining-close-18-5b-merger-create-1-1moz-senior-gold-producer)
- Combined: ~1.1Moz pro forma annual production; 6 North American mines; ~23Moz P&P reserves; three long-life Canadian mines (Greenstone, Musselwhite, Valentine); internally funded path to >1.9Moz/yr via Valentine Phase 2, South Railroad (Nevada; moving toward FID), Castle Mountain (California), Los Filos and Camino Rojo underground (Mexico) — [Pulse 2.0](https://pulse2.com/equinox-gold-and-orla-mining-18-5-billion-combination-creates-new-north-american-senior-gold-producer/)
- Valentine Phase 2 approved 5 Aug 2026: initial capital $436M (20% contingency), throughput from 2.5 to 5.0 Mtpa, production +~25% to ~223koz/yr average, 24-month build, completion late 2028 — [Northern Miner](https://www.northernminer.com/news/equinox-approves-436m-valentine-expansion/1003893761/), [Pulse 2.0](https://pulse2.com/equinox-gold-valentine-expansion-targets-223000-ounces-annually-as-orla-merger-creates-1-1-million-ounce-producer/)
- Orla produced 88,265oz in Q2 2026 — [CP24](https://www.cp24.com/news/money/2026/07/09/orla-produced-88265-ounces-of-gold-in-q2-on-track-to-achieve-guidance/)

### Inferences
- Reserve life ≈ 23 / 1.1 ≈ 21 years at the pro forma rate, or ≈ 14 years at the house 2031 rate of 1.6Moz (DERIVED).
- House base production by mine is ASSUMED (no per-mine guidance for Orla assets was retrieved).

### Gaps
- South Railroad FID date and capex; Castle Mountain Phase 2 permit (ROD) timing; Los Filos restart timing and community agreements; Nicaragua sanctions status in 2026 (not searched; budget exhausted).

## Q5. Gold price

### Cited Findings
- Spot gold settled at $4,158.70 on 30 Sep 2026 (−0.6%); Dec futures $4,186.70; gold −6.5% in September; ~−8.5% for Q3; driven by rising real yields (10-yr TIPS +0.44pp in September) — [Investing.com / texmetals / Yahoo via search](https://texmetals.com/all-news/precious-metals-market-update-9-30-2026)
- ATH ~$5,597 on 29 Jan 2026, followed by a ~$1,200 two-day crash; late-June low ~$3,995 (from KNT notes) — [Fortune](https://fortune.com/article/current-price-of-gold-09-29-2026/)
- Forecasts: Goldman $4,900 (Dec 2026); JPM $6,300 (end 2026); Reuters poll median 2026 $4,746.50 — [Metalsmine](https://www.metalsmine.com/news/1382062-jpmorgan-forecasts-gold-to-hit-6300-in-2026/amp)

## Q6. Analysts and consensus

### Cited Findings
- 9 analysts, average rating "Strong Buy", average 12-month target $13.0 ("+33.2% from latest price"; snapshot date unclear) — [stockscan.io](https://stockscan.io/stocks/EQX/forecast)
- Screening consensus EPS: 2026 $1.29 / 2027 $2.00 / 2028 $1.55 (7 analysts; 2028 revenue rests on one analyst); revenue $4,000 / $3,724 / $4,126M; Scotiabank FY27 EPS $1.75 — [vcpscanner](https://www.vcpscanner.com/valuation/eqx/estimates), [tickflow](https://tickflow.io/stock/EQX/forecast), [Simply Wall St](https://simplywall.st/stocks/de/materials/fra-1lrc/equinox-gold-shares/future)

### Inferences
- The consensus EPS share basis is unclear (pre- vs post-merger), and it predates September's 6.5% gold drop. Treat it as low-reliability.

### Gaps
- High and low price targets; median; estimate dates.

## Q7. Peers (screening file, not re-verified)
- EGO US$43.0 (1 Sep), cap US$8.7bn, fwd P/E 9.2/8.1/8.5, 12 analysts
- TXG US$39.10 (1 Oct), US$3.84bn, 7.6/6.7/4.9, 11 analysts; house report pw 36m +20.6%, stress −56%
- WDO US$24.22, US$3.6bn, 9.2/7.9/8.0, 12 analysts
- KNT US$16.84, US$4.1bn, 11.2/7.1/5.6, 10 analysts; house pw +32.1%, stress −72.6%
- AUGO US$76.02, US$6.35bn, 10.7/6.7/6.0, 7 analysts; house pw +23.1%, stress −60%
- Precious-metals screen median fwd P/E FY26 9.2x / FY27 7.0x (DERIVED, 23 names)

## Gaps (overall)
- Insider ownership %, insider transactions (SEDI), compensation, short interest, ADV, institutional ownership, buyback/NCIB (none found), beta and realised volatility, streams and royalties, hedges, RCF maturity, Nicaragua sanctions status, Los Filos status, Q1-26 EPS, guidance accuracy history. All are NOT RELIABLY AVAILABLE.
