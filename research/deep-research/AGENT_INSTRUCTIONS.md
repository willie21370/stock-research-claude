# Instructions for each per-stock deep-research run

Today is 2026-10-04. You produce ONE institutional equity research report for ONE stock.

## Steps
1. **First, read** `/root/.claude/skills/synced/73bf25d2-874a-40f4-9a98-5b8c08f1053f_d6096cf9-0d0a-4bad-9571-185fc9c04303/deep-research/references/researcher.md` and follow its research method.
2. Read the user's prompt: `/home/user/stock-research-claude/research/deep-research/stock_prompt.md`. Treat `[STOCK NAME / TICKER]` as the stock you were given. For the mandate placeholders use the prompt's own examples: return hurdle **100% total return within 36 months**, holding period **36 months**, risk budget **1.0%**.
3. Research with WebSearch (mode "standard"; "extended" only when standard results are thin). Direct website fetching is mostly blocked by the network, so search snippets are your main source — WebFetch may work for a few hosts; try once, don't waste time. Budget: about 60 searches. Prioritise: current share price (late Sep / early Oct 2026, with date), latest results (H1/Q2 2026), guidance, consensus estimates (with analyst counts), balance sheet/debt, share count, insider transactions, buybacks, analyst price targets, mine life / reserves / offtakes (miners), peers.
4. Save your raw research notes (facts + source URLs) to `/home/user/stock-research-claude/research/deep-research/notes/{SLUG}.md`.
5. Write the full report as a standalone HTML page to `/home/user/stock-research-claude/research/deep-research/reports/{SLUG}.html`.
   - Start from the structure in `/home/user/stock-research-claude/research/deep-research/reports/_TEMPLATE.html` (read it): keep its `<head>` exactly (fonts + `report.css`), the back link, and the class names. Do NOT add other stylesheets, scripts or external images.
   - Order: **Beginning summary** (every item in the prompt's "Beginning summary" list, as `.kpis` tiles + `.stats` rows) → Section 0 → Executive summary → Sections 1–7 → Closing audit. Separate sections with `<hr>`.
   - Formatting rules from the prompt: yellow marker = `<span class="hl">`, green = `.pos`, red = `.neg`, amber = `.flag`; confidence tags `.tag verified|derived|assumed`; `NOT RELIABLY AVAILABLE` as `<span class="na">`. Every table inside `<div class="table-wrap">`, numeric cells `<td class="num">`. Every score shown as X/10 or X/100. Scenario tables show the Probability column before the price columns.
   - Escape `&` as `&amp;` in text. Close every tag.
   - Be honest: flag gaps as NOT RELIABLY AVAILABLE rather than inventing figures. Label estimates with < 5 analysts as noise. Use the prompt's anti-bloat priority if you must truncate, and say what you truncated in the Closing audit.
6. Write a results file `/home/user/stock-research-claude/research/deep-research/results/{SLUG}.json` with exactly these keys (numbers, not strings):
   `{"ticker":"…","name":"…","price":0.0,"currency":"…","price_date":"YYYY-MM-DD","upside_36m_pct":0.0,"overall_score":0,"scorecard":0,"likelihood":0,"advice":"Strong Buy|Buy|Hold|Sell|Strong Sell","pw_target_36m":0.0,"report":"reports/{SLUG}.html"}`
   - `upside_36m_pct` = probability-weighted 36-month target vs current price, in %.
   - `overall_score` = the Overall Investment Stock Score (0–100) from the beginning summary.
   - `scorecard` = the Institutional Scorecard weighted composite (0–100).
   - `likelihood` = the base-case execution likelihood (0–100).
   These numbers must match what the report shows.
7. Your final reply must be ONE line only: `DONE {TICKER} | upside {x}% | overall {x} | scorecard {x} | likelihood {x}% | {advice}` (or `FAILED {TICKER} | reason`).

## Context from the screening stage (verify — do not trust blindly)
The stock came from an inflation-beneficiary screen (`/home/user/stock-research-claude/research/inflation-top100/candidates.json` has its screening entry: consensus EPS, P/Es, thesis, sources). Prices there may be stale; re-verify.
