# Samsung Galaxy — Sales & 5G Dashboard

E-commerce/Sales course project. Cleans a Kaggle sales dataset, answers 8 business
questions, and builds an interactive Excel dashboard with filters (slicers), KPIs, and charts.

## Files

| File | Description |
|---|---|
| `Expanded_Dataset.csv` | Raw dataset (Kaggle: Samsung Global Product Sales Dataset) |
| `Expanded_Dataset_cleaned.csv` | Cleaned dataset (see [Cleaning](#cleaning)) |
| `data_overview.md` | Full data profile — columns, dtypes, missing values, duplicates, unique values |
| `samsung_dashboard.xlsx` | Final deliverable — Dashboard, Business Questions, Data, Calc, Lists sheets |
| `pandas_cleaning.py` | Cleaning script (pandas) |
| `findings_recommendations.md` | Business recommendations tied to each finding |
| `screenshots/power_bi_dashboard.png` | Power BI dashboard preview |
| `screenshots/screenshot_1_overview_charts.png` | Dashboard — filters, KPIs, revenue & region charts |
| `screenshots/screenshot_2_models_table.png` | Dashboard — top models, 5G split, model table |

## Dataset

- **Source:** [Samsung Global Product Sales Dataset](https://www.kaggle.com/datasets/ashyou09/samsung-global-product-sales-dataset) (Kaggle)
- **Scope:** 15 Galaxy models, 5 regions, 2019–2024, quarterly
- **Columns:** Year, Quarter, Product Model, 5G Capability, Units Sold, Revenue ($),
  Market Share (%), Regional 5G Coverage (%), 5G Subscribers (millions),
  Avg 5G Speed (Mbps), Preference for 5G (%), Region

Full profile (dtypes, missing values, duplicates, unique-value counts,
data-quality issues) is in `data_overview.md`.

## Cleaning

Raw file: 1,000 rows → Cleaned file: 360 rows.

| Issue | Fix | Rows affected |
|---|---|---|
| Exact duplicate rows | Dropped | 640 |
| Negative `Market Share (%)` | Clamped to 0 | 17 |
| Negative `5G Subscribers (millions)` | Clamped to 0 | 3 |
| `Regional 5G Coverage (%)` > 100 | Capped at 100 | 12 |

Also added a `Period` column (`Year-Quarter`, e.g. `2019-Q1`) for time-series analysis.

## Business Questions

| # | Question | Result |
|---|---|---|
| 1 | Top model by total revenue? | Galaxy A14 5G ($913M), then S23 5G ($895M) |
| 2 | Top region by units sold? | North America (2.70M units) |
| 3 | Revenue trend 2019–2024? | Peak 2020 ($1.96B) → trough 2023 ($1.53B) → rebound 2024 ($1.92B) |
| 4 | 5G vs non-5G unit sales? | 5G averages ~34% more units per row (35,667 vs 26,605) |
| 5 | Region with highest 5G preference? | Latin America (68.7%) |
| 6 | Does 5G coverage drive sales? | Weak correlation (r = 0.106) |
| 7 | Best-performing quarter? | Q3 highest units, Q1 highest revenue (lower avg price in Q3) |
| 8 | Highest average price per unit? | Galaxy S22 5G ($1,237/unit) |

Full methodology (GROUP BY logic, sample sizes) is in the **Business Questions** sheet
of `samsung_dashboard.xlsx`.

## Key Findings & Recommendations

Each finding above is turned into an actionable recommendation in
`findings_recommendations.md` — e.g. the 5G-vs-non-5G finding becomes a
recommendation to phase out non-5G models, and the Latin America preference
finding becomes a recommendation to expand there. See that file for all 8.

## Dashboard

Built in Excel (`samsung_dashboard.xlsx`, **Dashboard** sheet):

- **Filters** (Year, Region, 5G Capability, Model) — dropdown cells that drive every
  KPI, chart, and table live via `SUMPRODUCT` formulas (no macros)
- **KPIs:** Total Revenue, Total Units Sold, Avg 5G Preference, Avg Market Share
- **Charts:** Revenue by Year (line), Units Sold by Region (bar), Top Models by
  Revenue (bar), 5G vs Non-5G Units (pie)
- **Model summary table** — updates with the active filters

![Filters, KPIs, revenue trend, units by region](screenshots/screenshot_1_overview_charts.png)

This view shows the current filter state (all set to "All") plus the four
headline KPIs, the revenue trend line, and the units-by-region bar chart. Key
takeaway: revenue dipped from 2020 to 2023 before recovering in 2024, and
North America clearly leads all regions in units sold.

![Top models by revenue, 5G vs non-5G split, model summary table](screenshots/screenshot_2_models_table.png)

This view shows which models drive the most revenue, the overall 5G vs
non-5G split, and the full per-model breakdown. Key takeaway: the A14 5G and
S23 5G top the revenue chart, and roughly three-quarters of units sold are
5G-capable — reinforcing that 5G is now the dominant part of the lineup.

## Power BI Dashboard

![Power BI report: revenue by period, revenue by model, units by 5G capability, units by region](screenshots/power_bi_dashboard.png)

Same headline numbers as the Excel version — $10.77bn total revenue, 12M
units sold, 3.73% average market share — confirming both dashboards read the
same cleaned data. The revenue-by-model and units-by-region breakdowns match
the Excel findings exactly (A14 5G / S23 5G on top, North America leading
all regions).

**Known issue:** the "Sum of Revenue by Period" line chart's x-axis is not in
chronological order (Power BI sorts `Period` as plain text instead of by
date), which makes the trend look like a steady decline instead of the actual
2020-peak → 2023-dip → 2024-rebound pattern. Fix: add a numeric sort column
(`Year*10 + Quarter number`) in Power BI, then right-click the `Period`
column → **Sort by Column** → pick that column.

## Reproducing the cleaning

Run `python pandas_cleaning.py` — reproduces the same 1000 → 360 row cleaning.


