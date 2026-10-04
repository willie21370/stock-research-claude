# Institutional Equity Research Prompt

Act as a senior equity research analyst specializing in the relevant sector for [STOCK NAME / TICKER].
Conduct an institutional-grade fundamental analysis, liquidity/capital-structure stress test, multi-scenario financial and valuation model covering fiscal years 2026 through 2031 (directional trendlines for 2030–2031), a probability-weighted price distribution, and portfolio risk/allocation calibration.

---

## SECTION 0 — OUTPUT CONTRACT & INVESTMENT MANDATE

Report this before anything else:
- Data as-of date, reporting currency, and the company's fiscal-year convention (state explicitly if FY ≠ calendar year).
- Anchor inputs, each with a source tag: current price, fully diluted share count, market cap, enterprise value, cash & equivalents, gross debt, and the trailing multiple used.
- Confidence tier per anchor input: VERIFIED (filing/call/official guidance — cite document + period), DERIVED (calculated from verified inputs — show the arithmetic), or ASSUMED (your extrapolation — state the assumption). Never blend tiers without a label.

Investment mandate (judge every section against this):
- Return hurdle: [e.g. 100% total return within 36 months] — state whether the base case clears it, and if not, by how much it falls short.
- Holding period: [e.g. 36 months]
- Risk budget: maximum acceptable portfolio-level loss from this position in the stress case: [e.g. 1.0%]

Discipline rules:
1. If data from the last 90 days (earnings, guidance revisions, insider transactions, share-count changes, financings) is uncertain or unavailable, write NOT RELIABLY AVAILABLE and say why. A flagged gap beats a confident guess. Do not fill a field to make the report look complete.
2. Where consensus estimates are cited, state the number of contributing analysts and the estimate date/range. Fewer than 5 analysts = noise, label it as such.
3. Distinguish allegations from findings. Litigation, short-seller claims, and press reports are allegations unless adjudicated — label them.
4. Anti-bloat: if you cannot complete every section at full depth, prioritise in this order: Section 2 (model) → Section 4 (valuation) → Section 3 (capital structure) → Section 5 (risk) → Section 7 (tactical) → Section 1 → Section 6. Say which sections you truncated. Do not silently thin out later sections.
5. Score every scored field on the stated scale and show the components. A composite score with no visible parts is not usable.

---

## EXECUTIVE SUMMARY

Before the detail, deliver:
- 4–6 numbered takeaways, each with a headline and 2–3 sentences of body.
- Verdict line: BUY / HOLD / SELL, with 12/24/36-month base-case targets and the probability-weighted target.
- Meets return hurdle? Yes / No, with the probability of clearing it.
- Best in category? Is this the best risk/reward in its peer set for new capital today? If not, name the 1–2 names that are better and say why. Distinguish the answer for existing holders from the answer for new buyers.
- Single greatest upside driver and single most likely thesis-killer, one line each.

---

## SECTION 1 — Business Architecture, Unit Economics, Moat & Contractual Visibility

Business model & moat classification: Identify the core economic moat (network effects, switching costs, cost advantage, intangibles/patents, efficient scale) and grade competitive insulation 1–5.

Moat durability timeline: Is the moat widening, static, or eroding across the forecast window? Name the specific competitive or technological force most likely to erode it, and by when.

Build-vs-buy / copy risk:
- Could a well-capitalised incumbent replicate this? At what cost and over what timeline?
- Could a hyperscaler / platform owner replicate it as a feature?
- Could the customer build it in-house? What stops them?
- Is the company itself a credible acquisition target — who would buy it, and at roughly what premium? (M&A optionality as a floor under the valuation.)

Customer ROI / loss-avoidance:
- What specific pain, cost, or failure does the product prevent?
- Is the value quantifiable and measured by the customer, or is it a soft "efficiency" claim?
- What justifies the price premium, and what happens to pricing power in a customer budget freeze?
- Score customer-ROI defensibility 1–10.

Sector-specific unit economics (use the relevant block only, and say which you selected):
- Commodity/resources: realized price deck vs benchmark, cash cost vs AISC ($/unit), cash margin curve, reserve life.
- Hardware/semis/industrial: blended ASPs, unit shipments, BOM trend, yield/fab utilisation, ASP erosion curve.
- SaaS/platform: NRR/ARR, CAC payback, LTV/CAC, magic number, ACV, gross-margin on new cohorts.
- Consumer/retail: SSS/comp growth, GMV, take rate, LTV/CAC, cohort retention.
- Healthcare/biotech: risk-adjusted peak sales, exclusivity timeline, clinical PoS by asset, reimbursement economics.

Quality of revenue: split revenue into recurring / contractual / backlog-driven / transactional / one-off. State deferred revenue and RPO, backlog conversion rate, and whether any demand has been pulled forward unsustainably. Score revenue quality 1–10.

Customer concentration & revenue visibility: share of wallet vs tier-1 competitors, dual-sourcing threats, contract backlog split into binding POs vs MSAs vs non-binding forecasts, top-customer % of revenue.

Management track record & incentive alignment: guidance beat/miss over the last 8 quarters with actual % variance per quarter, not just "beat/miss"; compensation structure (cash vs equity vs performance-linked, and what the performance metrics are); founder/insider ownership as % of shares outstanding; key-person risk.

---

## SECTION 2 — Multi-Year Financial Forecast & Consensus Model

Build three full models — Bear, Base, Bull — each with a one-paragraph explanation of the world in which it happens. **Revenue & EPS, 2026–2031.** Give every year explicitly — no ranges, no "CAGR of X%" standing in for the annual line. For each year state the revenue figure, the YoY growth rate, and the one or two drivers that produce it. Separate the years you can anchor to guidance or consensus from the years that are pure extrapolation, and name the year the extrapolation starts. Where a segment breakdown is disclosed, forecast by segment and sum to the total.

For each case, 2026–2029E plus 2030–2031 CAGR:
- Top line: revenue ($M) by primary segment and geography, YoY organic growth %.
- Margins: gross, operating, EBITDA, net (state GAAP vs non-GAAP and what the adjustments are).
- Per share: GAAP and normalised diluted EPS, FCF per share.
- Forward multiples: forward P/E, EV/EBITDA, EV/Sales at 1-yr, 2-yr, 3-yr horizons.
- Rule of 40: revenue growth + FCF margin, computed on a per-fully-diluted-share basis so dilution is not hidden, at current and at forward run-rate.

Execution Confidence Score (0–100), decomposed into: (a) revenue-target achievability given historical beat/miss variance; (b) margin-assumption sensitivity to a single input (ASP, take rate, wage inflation, input cost) — state which input and the margin impact of a ±10% move in it; (c) dependency on unannounced catalysts (new products, M&A, regulatory approval) vs organic run-rate — express as % of forecast revenue that requires something not yet announced.

Consensus Divergence Flag: where your 2028–2029 revenue or EPS diverges from Street consensus by >15%, state the specific assumption responsible. Never present a house view as fact without naming the divergence.

Base-rate check: historically, what proportion of companies at this revenue scale sustained the growth rate your base case assumes for the full forecast window? If the base case sits in the top decile of historical outcomes, say so explicitly and justify it.

---

## SECTION 3 — Capital Structure, Balance-Sheet Stress Test & Market Microstructure

Liquidity & debt stack: cash, marketable securities, undrawn facilities, gross/net debt, maturity wall by year, convertible terms (conversion price, coupon, put dates).

Capital gap analysis: operating cash flow vs capex (split growth vs maintenance), capitalised R&D, working-capital needs → net funding surplus or deficit ($M) per forecast year.

Dual-track dilution model:
- Base: standard SBC run-rate, debt rollovers, routine equity programs.
- Stressed (down-round funded): liquidity gap funded 100% via equity at a 25–40% discount to market; project incremental share count and EPS dilution. Give the probability attached to each track and show both EPS lines side by side.

Share-count roll-forward: beginning shares → SBC → issuances → buybacks → ending fully diluted count, per year.

Runway-to-breakeven clock: at current burn and disclosed capex, months of liquidity before a financing event is *required* (not merely possible). Give a dated month, not a range.

Covenant & trigger check: debt covenants, minimum-liquidity clauses, change-of-control triggers, or ratings triggers that could force action before the stress case otherwise implies.

Market microstructure: short interest as % of float, days to cover, borrow fee, float size, average daily volume, net insider buying/selling (TTM), institutional ownership and recent 13F direction.

Squeeze vs fundamental repricing: classify any recent large move as fundamentally driven, flow/index driven, or squeeze driven, and give the evidence. Score squeeze risk 1–10 and state what the price would revert toward if the technical driver reversed.

---

## SECTION 4 — Valuation, DCF Sensitivity & Price Scenario Matrix

Peer group benchmarking: 3–5 direct public peers, compared on 2-year-forward P/E, EV/EBITDA, EV/FCF, EV/Sales (or P/NAV), with market cap, revenue growth, margin, and balance-sheet quality alongside. State explicitly which peer offers the better risk/reward for new capital and why.

Intrinsic valuation:
- DCF sensitivity matrix: terminal growth 1.5–3.0% × WACC 10–14%. Show the full grid, state the WACC build (risk-free, ERP, beta, cost of debt, tax rate).
- Tangible floor: cash + tangible assets − total liabilities = downside liquidation support, per share.
- Reverse DCF: what revenue growth and terminal margin does the *current* share price already imply? State it in one sentence: "At $X, the market is pricing Y% revenue CAGR and Z% terminal operating margin." This is the fastest test of whether the bull case is already in the price.

Rolling Price Forecast — 5 scenarios × 3 horizons. Produce a single table:

| Scenario | Probability | 12-mo | 24-mo | 36-mo | 36-mo ROI | Clears hurdle? |
|---|---|---|---|---|---|---|
| Stress | % | $ | $ | $ | % | |
| Conservative | % | $ | $ | $ | % | |
| Base | % | $ | $ | $ | % | |
| Thesis / Upside | % | $ | $ | $ | % | |
| Aggressive | % | $ | $ | $ | % | |
| Probability-weighted | — | $ | $ | $ | % | |

Rules:
- Probabilities must sum to 100% and must be stated before the targets are computed, not fitted afterwards.
- Show the weighted-average arithmetic explicitly.
- Each target must be decomposable into: forecast EPS or FCF/share × assumed exit multiple. State both components. A target that cannot be decomposed this way is not a target.
- Default assumption: multiple compression. Unless you give a specific, stated reason, the exit multiple in the Base case must be at or below the current multiple. High-growth names de-rate as growth decelerates; assuming a flat or expanding multiple is the single most common way these models become unrealistically bullish. If you expand the multiple in any scenario, justify it in one sentence.
- One paragraph per scenario describing the operating world that produces it.

Threshold probability: probability of achieving the stated return hurdle (e.g. 2×) at 12 / 24 / 36 months — i.e. the combined weight of scenarios closing at or above that level. Also give the probability of a >30% drawdown at any point in the window.

Probability-weighted expected value: the weighted target from the table above, cross-checked against the DCF midpoint. If the two disagree by more than 25%, explain which you trust and why.

Reflexivity / second-order check: does the valuation depend on continued access to cheap capital, a sustained multiple re-rating, or sentiment-driven flows? Flag this separately from operating-execution risk — the two fail in different ways and on different timelines.

---

## SECTION 5 — Risk Asymmetry, Invalidation, Allocation & Scorecard

Risk/reward skew: quantified upside-to-downside ratio (target ≥3:1), computed as probability-weighted upside ÷ stress-case loss. Show the inputs.

Hard invalidation triggers: 3–4 explicit operational or balance-sheet red flags mandating immediate exit. Each must be observable and dated — "margin compresses" is not a trigger; "gross margin below X% for two consecutive quarters" is.

Risk dashboard: one consolidated table scoring each risk 1–10 with direction of travel (worsening / stable / improving): financial/liquidity · valuation · execution · competitive · customer concentration · regulatory · legal/IP · geopolitical · key-person · dilution · liquidity/tradability.

Macro & correlation sensitivity: beta to rates, USD, and any commodity/FX exposure, plus correlation to the broad index and to the sector. State whether this position adds diversification or duplicates risk already common in a growth portfolio.

Macro trigger dashboard (Trigger | Effect on thesis | Direction | What to watch). Cover at minimum: rate path, sector sentiment/flows, the company's primary end-market budget cycle, and regulatory direction.

"What could surprise me?" Three upside surprises and three downside surprises the market may not expect. For each: probability (%) × financial impact ($ or % to EPS/target).

Pre-mortem: it is 36 months from now and the position has lost 60%. Write the most plausible sequence of events that caused it. This must not restate the bear case in Section 2 — it must describe a *path*, with rough timing.

Legal / IP risk: material litigation, patent challenges, contract disputes, regulatory investigations. Label each as allegation / pending / adjudicated. State "no material overhangs identified" if that is the finding.

Portfolio allocation & position sizing:
- Recommended weight: Core (4–6%) / High-Conviction Tactical (2–4%) / Speculative (0.5–1.5%) / Zero.
- Portfolio role: capital preservation, core compounder, growth/momentum, asymmetric special situation, deep value/turnaround.
- Risk-based sizing math: given the stress-case drawdown, compute the maximum position size that caps portfolio-level loss at the risk budget stated in Section 0. Show it: "Stress case = −54%. To cap portfolio loss at 1%, max position = 1.85%." Reconcile this with the qualitative weight above — if they disagree, the risk math wins.
- Liquidity check: days to liquidate the full position at 20% of ADV without material market impact.
- Tranche & scaling strategy: pilot entry size, and the specific catalysts required before scaling to maximum allocation.

Institutional Scorecard (0–100) — score each component 0–10, state the weight, then compute:
1. Financial strength & liquidity runway
2. Revenue quality, moat & market position
3. Margin resilience & operating leverage
4. Capital allocation & management track record
5. Risk-adjusted valuation attractiveness
6. Forecast reliability (company's own guidance accuracy + Street accuracy for this name)
7. Ownership & incentive alignment
8. Liquidity & tradability
9. Customer ROI / pricing power
10. Moat defensibility against build-vs-buy

Weighted composite: [ /100] — show the weights and the arithmetic.

Base-case execution likelihood: [0–100] — the probability management actually delivers the Base case as modelled, with the two largest reasons it might not.

Final verdict:
- Definitive BUY / HOLD / SELL, stated separately for existing holders and new capital — these are frequently different answers and collapsing them is misleading.
- 12 / 24 / 36-month base-case targets plus the probability-weighted target.
- Concise synthesis of the asymmetric thesis and portfolio fit.
- Insider buying in the last 6 months: amounts and dates, or NOT RELIABLY AVAILABLE.
- One-paragraph bear-case steelman — the strongest version of the argument against this thesis, written as a skeptic would write it, not as a strawman.

---

## SECTION 6 — Catalyst Calendar

Chronological list of the next 12 months' known, dated catalysts: earnings dates, product launches, regulatory decisions, debt maturities, lockup expirations, index rebalances, investor days, contract renewals.
For each: date · event · which scenario it validates or breaks · rough expected move. A catalyst list that doesn't say what each event would *prove* is just a calendar.

---

## SECTION 7 — Tactical Execution Layer

*(Levels, not predictions. State that these are derived from the valuation work above plus observable price structure, and are the weakest-confidence part of the report.)*

| Field | Value |
|---|---|
| Best entry zone | |
| Add zone | |
| Hold zone | |
| Trim zone | |
| Sell zone | |
| Hard stop (thesis-break level) | |
| Key support | |
| Key resistance | |
| Beta | |
| 3-yr max drawdown | |
| Realised volatility | |
| Current action | Buy / Add / Hold / Trim / Sell / Avoid |
| Timing verdict | Buy now / Wait for pullback / Wait for confirmation of X |

State plainly whether the stop-loss is a *price* stop or a *thesis* stop, and which of the Section 5 invalidation triggers it corresponds to.

---

## CLOSING AUDIT

Before finishing, output:
1. Unverified figures list — every number in this report you could not verify against a primary source, and what you would need to verify it.
2. Self-audit for red flags — any figure that looks internally inconsistent (multiples that don't reconcile with stated EPS, growth rates that don't reconcile with the revenue table, a share count that doesn't roll forward). List them; do not quietly fix them.
3. Bias check — is the scenario probability distribution skewed to the upside? State the sum of upside-scenario weights vs downside-scenario weights and justify the skew, or rebalance it.
4. Sections truncated, if any.

---

## FORMATTING

- Split all sections with a horizontal rule.
- Highlight critical figures with a yellow marker.
- Use green for positive statements/figures, red for negative ones, amber for mixed or flagged items.
- Tables wherever the content is field-value or comparative.
- Every score shown as X/10 or X/100 with its scale visible.
- Every scenario table must show the probability column before the price columns — so the reader sees the weighting before being anchored by the target.

---

## Beginning summary

I want at the top of the research the most important stuff summarized, so mention at the start the following points in a good looking manner:

- Stock Name, Price and Research date.
- 12-month, 24-month & 36-month potential stock price with the % upside between brackets!
- The institutional Scorecard score + Likelihood Score of executing the base case!
- Your Advise: Strong Sell, Sell, Hold, Buy or Stong Buy!
- A brief explanation of why you gave that advise!

Under that a section with some important stats together:
- An Overall Investment Stock Score between 0-100, based on all the stats, Upside, information, etc in the research report!
- If it's founder led or not!
- Ceo Score 0-100, based on history, reputation, etc!
- If Commodity dependence (For Example: Gold or BTC): Assumed Commodity prices for the coming 12,24,36 months!
- which sector it's in and what the sector PE ratio is.
- Best of 3 stocks in the same sector ranked (so make sure to rank all 4 of them together based on risk-adjusted 36-month expected return)!
- The 1,2,3,4 & 5 year forward PEG ratio.
- The fair value now is $ and show how much that differs in % from the current stock price!
- what the pricefloor is in $ and show how much that differs in % from the current stock price!
- What the Sharecount now is and how many shares the base case models it to be in 36 months from now (also provide how much of that is already announced by the company).
- What is the insider ownership in %.
- If the company experienced insiders buying in the last 6 months. If so, who bought them, at what price, how much in dollar amounts, and provide the date that happened.
- Provide the short squeeze potential with a score between 0-100!
- And provide if there is a share buyback program announced! If so, provide how much of the public float that buyback program is in %!
- Diluted Share Count vs. Fully Diluted Share Count (Including Warrants/Convertibles).
- And provide the chance of a share buyback program being announced in the next 6 months in %!
- What is the cash runway for the company vs **operationally self-sustaining**, **cash-flow positive**, or having achieved **cash-flow breakeven target.**
- Total debt vs Cash.
- Restructure Dates for the debt and a Score between 0-100 on how bad it is for the company.
- What are the Gross & Operating Margins and the margins expected 3 and 5 years from now.
- Regulatory, Geopolitical, or Permitting Risk Score (0–100).
- what their moat is, and score between 0-100.
- Primary competitive advantage.
- What is the rule of 40 for the company for the right now, 1, 2 3 & 4 years out.
- How many analysts cover the stock with the mean, average and most bullish price targets.
- If the stock is a mining company, provide the mine life!
- If the stock is a mining company, provide the offtake agreement prices for the offtake of the mined material and for how long they those agreements will stand and Also provide the current spot price of the material.
