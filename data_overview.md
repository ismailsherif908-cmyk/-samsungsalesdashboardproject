# Data Overview

## Business context

The data tracks quarterly sales performance of Samsung Galaxy phone models
across 5 regions from 2019 to 2024, alongside 5G adoption metrics (network
coverage, subscriber counts, customer preference). Each row is one
model-region-quarter combination — not an individual transaction or order,
so there's no customer- or order-level data here, only aggregated sales and
5G-adoption figures per model per region per quarter.

## Shape

- **Raw file (`Expanded_Dataset.csv`):** 1,000 rows × 12 columns
- **Cleaned file (`Expanded_Dataset_cleaned.csv`):** 360 rows × 13 columns
  (see [Cleaning](README.md#cleaning) for what changed and why)

## Columns

| Column | Type | Meaning |
|---|---|---|
| `Year` | int | Calendar year, 2019–2024 |
| `Quarter` | text | Q1–Q4 |
| `Product Model` | text | One of 15 Galaxy models (S/Note/A/Z series) |
| `5G Capability` | text | `Yes`/`No` — whether the model supports 5G |
| `Units Sold` | int | Units sold that quarter, in that region |
| `Revenue ($)` | float | Revenue for that row |
| `Market Share (%)` | float | Model's market share that quarter/region |
| `Regional 5G Coverage (%)` | float | % of the region covered by 5G networks |
| `5G Subscribers (millions)` | float | 5G subscribers in that region, millions |
| `Avg 5G Speed (Mbps)` | float | Average 5G network speed in that region |
| `Preference for 5G (%)` | float | % of customers preferring 5G in that region |
| `Region` | text | One of 5 regions |
| `Period` *(added)* | text | `Year-Quarter`, e.g. `2019-Q1` — added during cleaning for time-series charts |

## Time period

2019–2024, quarterly (24 quarters total).

## Unique values

| Column | Count | Values |
|---|---|---|
| Year | 6 | 2019–2024 |
| Quarter | 4 | Q1, Q2, Q3, Q4 |
| Product Model | 15 | Galaxy S10 → Galaxy Z Flip5 5G (full list in the Data sheet) |
| 5G Capability | 2 | Yes, No |
| Region | 5 | Asia-Pacific, Europe, Latin America, Middle East & Africa, North America |

No customer or order counts exist in this dataset — it's pre-aggregated by
model/region/quarter, not transactional.

## Missing values

None. All 12 columns are fully populated in all 1,000 raw rows.

## Duplicates

640 fully duplicate rows out of 1,000 (every column identical) — removed
during cleaning, leaving 360 unique rows.

## Other data-quality issues found

| Column | Issue | Valid range | Found |
|---|---|---|---|
| `Market Share (%)` | Negative values | should be ≥ 0 | min −0.49 |
| `5G Subscribers (millions)` | Negative values | should be ≥ 0 | min −0.89 |
| `Regional 5G Coverage (%)` | Values over 100% | should be ≤ 100 | max 103.92 |

All three are fixed in `pandas_cleaning.py` (see [Cleaning](README.md#cleaning)).

## Notable observations

- The dataset is already aggregated (no raw transactions), which is why
  business questions here are phrased as "which region/model/quarter" rather
  than customer-level questions.
- 5G-capable models (10 of the 15) vastly outnumber non-5G models (5:
  S10, Note10, S20, Note20, S21) — the lineup has already shifted mostly to 5G.
- The 640 exact duplicates suggest the raw file was likely produced by
  appending the same generation process more than once rather than a natural
  data-collection artifact.
