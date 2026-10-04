# International Petroleum Corporation (TSX / Nasdaq Stockholm: IPCO) — research notes (2026-10-04)

Method note: WebSearch snippets only. Every WebFetch attempt was blocked by the egress proxy (inderes.se, thelundingroup.com PDF, boereport, mfn.se, international-petroleum.com, stockanalysis, google finance, theglobeandmail, finanzen.net, affarsvarlden, fintel, stockchase, iocharts, halo-technologies, marketscreener; curl to Yahoo/Stooq APIs rejected). The session-wide WebSearch budget (200 calls, shared with parallel runs) ran out after 19 IPCO searches. Many fields (Q1-26 detail, cash/gross debt split, RBL size, insider trades, short interest, ADV, compensation, hedge book, October price) could not be researched; they are listed under Gaps. Items from background knowledge are marked ASSUMED.

## Q1: Current price, share count, market value

### Takeaway
The last dated quote I could verify is CA$34.56 (4 Sep 2026). The screening file shows CA$28.99 (1 Oct 2026), but I could not confirm that figure, and a Stockholm market-cap snippet points to about CA$37. The share count is solid: 111,727,666 shares outstanding at 30 Sep 2026.

### Cited Findings
- IPCO CA$34.56 "as of September 4", down 1.12% (−0.39); 52-week high CA$39.47, low CA$20.74; 112.83M shares; no dividend — [halo-technologies snippet](https://www.halo-technologies.com/markets/shares/tse/ipco/)
- Simply Wall St snippets show CA$35.75, CA$33.14 and CA$29.49 at different (undated) points in 2026 — [Simply Wall St](https://simplywall.st/stock/tsx/ipco)
- Stockholm market cap 28,444 MSEK (date unclear) — [Affärsvärlden](https://www.affarsvarlden.se/aktie/international-petroleum-corp). At 111.73M shares that is about SEK 254.6/share, roughly CA$36–37 at an assumed SEK/CAD of 6.9 (DERIVED/ASSUMED)
- 111,727,666 common shares outstanding at 30 Sep 2026, after cancelling 431,638 repurchased shares — [via.ritzau / IPC updated share capital](https://via.ritzau.dk/files/90446/15197113/556438/en)
- 112,826,752 shares at 14 Aug 2026, of which 277,616 were held in treasury — [BNN Bloomberg NCIB release](https://www.bnnbloomberg.ca/press-releases/2026/08/17/international-petroleum-corporation-announces-results-of-normal-course-issuer-bid/)
- Screening file: CA$28.99 on 2026-10-01, market cap ~US$2.4bn — local `inflation-top100/candidates.json` (source not stated, unverified)

### Inferences
- The price is the single biggest uncertainty in this report. The anchor is CA$34.56 (the latest verified dated print). The two alternatives give PW upside of about +29% (at CA$28.99) or about −2% (at ~CA$36.8).
- Market cap ≈ 111.73M × CA$34.56 = CA$3.86bn ≈ US$2.78bn at an assumed USD/CAD of 1.39.

### Gaps
- No verified close for late Sep / early Oct 2026, because every quote host was blocked.

## Q2: Latest results (Q2 2026) and guidance

### Takeaway
Blackrod Phase 1 reached first oil in May 2026, ahead of schedule and on budget, and the plateau of 30,000 bopd is now expected in late 2027. Q2 itself was weak: net result was US$10M, EPS badly missed estimates, and FCF was only US$4M. Full-year OCF guidance was raised to US$230–330M on a higher oil deck.

### Cited Findings
- Q2-26 production ~42,200 boe/d (53% heavy crude, 13% light/medium, 34% gas), in line with guidance — [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/08/04/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report/), [Quartr](https://quartr.com/events/international-petroleum-corporation-ipco-q2-2026_3Yqm1Y5L)
- Q2-26 OCF US$67M, FCF US$4M, net debt US$509M at 30 Jun (about US$4M lower than at 31 Mar) — [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/08/04/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report/), [allmind](https://allmind.ai/earnings/event/2940979)
- Q2-26 net result US$10M; EPS $0.13 vs $0.37 estimated (currency probably CAD) — [allinvestview](https://www.allinvestview.com/earnings/IPCO.TO/q2-2026/), [MarketBeat](https://www.marketbeat.com/earnings/reports/2026-8-4-international-petroleum-co-ipcoto-stock/)
- Q2-26 revenue US$185.738M; gross profit US$38.094M; opex US$19.1/boe — [inderes.fi](https://www.inderes.fi/en/releases/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report)
- Q2 capital and decommissioning spend US$49M, in line; FY2026 capex guidance of US$163M maintained (up from the US$122M February budget, which was raised earlier for short-cycle investment) — [mfn/placera snippets](https://www.placera.se/pressmeddelanden/international-petroleum-corp-international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report-20260804)
- FY2026 guidance: production 44,000–47,000 boe/d (maintained); opex US$18–20/boe (maintained); OCF US$230–330M; FCF US$10–110M (was 0–120M); assumes Brent US$70–90 for the rest of 2026 — [mfn snippet](https://mfn.se/one/a/international-petroleum/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report-8298ef1d), [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/08/04/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report/)
- Blackrod Phase 1: first oil May 2026, ahead of schedule and on budget; 30,000 bopd plateau by late 2027, one quarter earlier than first guided — [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/08/04/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report/)
- Original 2026 budget (Feb 2026): capex US$122M, production 44–47k boe/d, OCF US$100–250M at Brent US$55–75 — [inderes.fi YE2025](https://www.inderes.fi/en/releases/international-petroleum-corporation-announces-2025-year-end-financial-and-operational-results-and-2026-budget-reserves-and-guidance)

### Inferences
- Q2 OCF/boe was only ~US$17.4 (67 / 3.84 MMboe) with Brent in the US$90s. The likely reasons are hedge losses, Blackrod start-up costs and low AECO gas prices. I could not confirm the split.
- FCF guidance (10–110) is ~US$57M below OCF guidance minus capex (230–330 − 163). The gap is probably interest, leases and other items. Unreconciled.

### Gaps
- Q1-26 production, OCF and net result; H1 totals; hedge book; realized prices; WCS differential.

## Q3: Reserves, balance sheet, debt

### Takeaway
IPC has long-life reserves: 2P of 521 MMboe, a 31-year RLI and 1.2bn boe of contingent resources. Its debt is a single US$450M 7.50% bond due around Oct 2030, plus bank lines.

### Cited Findings
- YE2025 2P reserves 521 MMboe; RLI 31 years; reserve replacement 277%; PDP 125 MMboe (+28%, driven by Blackrod); contingent resources (best, unrisked) 1,224 MMboe — [inderes.fi](https://www.inderes.fi/releases/international-petroleum-corporation-announces-2025-year-end-financial-and-operational-results-and-2026-budget-reserves-and-guidance)
- US$450M senior unsecured bonds, 5-year tenor, fixed 7.50% coupon; described as a refinancing completed in October, maturity Oct 2030 — [mfn snippet](https://mfn.se/one/a/international-petroleum/international-petroleum-corporation-completes-usd-450-million-bond-placement-142784eb), [allmind](https://allmind.ai/earnings/event/2940979)
- Net debt US$509M at 30 Jun 2026 — [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/08/04/international-petroleum-corporation-announces-second-quarter-2026-financial-and-operational-results-and-releases-sustainability-report/)

### Gaps
- Cash balance, drawn RBL/bank debt, facility sizes, covenants, NPV10 of reserves, book equity.

## Q4: Capital return and ownership

### Takeaway
The NCIB allows up to 6,468,077 shares (10% of public float) through 4 Dec 2026. Only 1,099,086 shares had been bought by 25 Sep 2026, so the programme is about 17% used. IPC pays no dividend.

### Cited Findings
- NCIB announced 3 Dec 2025; max 6,468,077 shares to 4 Dec 2026; repurchased shares are cancelled — [BNN Bloomberg](https://www.bnnbloomberg.ca/press-releases/2026/09/28/international-petroleum-corporation-announces-results-of-normal-course-issuer-bid/), [placera](https://www.placera.se/pressmeddelanden/international-petroleum-corp-international-petroleum-corporation-announces-results-of-normal-course-issuer-bid-20260810)
- 1,099,086 shares repurchased to 25 Sep 2026; 148,500 in the week of 21–25 Sep (100,000 in Stockholm via Pareto, 48,500 on TSX via ATB) — [BNN Bloomberg 28 Sep](https://www.bnnbloomberg.ca/press-releases/2026/09/28/international-petroleum-corporation-announces-results-of-normal-course-issuer-bid/), [boereport](https://boereport.com/2026/09/28/international-petroleum-corporation-announces-results-of-normal-course-issuer-bid-94/)
- Founded by Adolf H. Lundin (Lundin Group) on 13 Jan 2017, HQ Vancouver; assets in Canada, Malaysia and France — [halo-technologies snippet](https://www.halo-technologies.com/markets/shares/tse/ipco/)

### Inferences
- The TSX caps an NCIB at 10% of public float, so public float ≈ 64.7M shares. Shares outstanding were ~113M at the time, which implies ~42–43% held by insiders and control persons, mostly Lundin family trusts (DERIVED).
- CEO William Lundin (since 2024) and Chairman Lukas H. Lundin: background knowledge, ASSUMED.

### Gaps
- Insider transactions in the last 6 months; option/PSP overhang; short interest; ADV; institutional holders.

## Q5: Consensus and price targets

### Takeaway
Eight analysts cover the stock. The consensus target is CA$40.71 (raised from CA$38.44). The consensus EPS figures date from early 2026, before the war, and are internally inconsistent.

### Cited Findings
- Price target CA$40.71 (from CA$38.44); a narrative fair value of ~CA$42 after CA$2 and CA$4 target increases — [Simply Wall St valuation](https://www.simplywall.st/company/id/8dc5ca71-f6cc-4c10-b0bf-a86afb86b953/valuation)
- "Eight analysts expect 2026 revenue of US$702.6m and EPS up 44% to US$0.44" (dated, likely Feb 2026) — [Simply Wall St news](https://simplywall.st/stocks/ca/energy/tsx-ipco/international-petroleum-shares/news/international-petroleum-corporation-earnings-missed-analyst)
- Screening file consensus EPS (CAD, converted at 1.39): 2026 0.85, 2027 2.82, 2028 3.92 (≈ US$0.61 / 2.03 / 2.82); revenue (US$) 703 / 1,049 / 1,301 — local candidates.json, citing [Simply Wall St future](https://simplywall.st/stocks/se/energy/sto-ipco/international-petroleum-shares/future)

### Gaps
- High and low targets; broker names; estimate dates.

## Q6: Macro (oil)

### Cited Findings (from companion VIST notes, same session)
- Brent ~US$91.9 (Oct-2026 contract) around 2 Oct 2026; Brent peaked near US$110 in 2026 (Iran war / Strait of Hormuz) and fell to ~US$82 in late July — [sxcoal](https://en.sxcoal.com/news/detail/2095317254680023042), [TASS](https://tass.com/economy/2166539/amp)

### Gaps
- WCS differential, AECO gas price, USD/CAD and SEK/CAD on the as-of date.
