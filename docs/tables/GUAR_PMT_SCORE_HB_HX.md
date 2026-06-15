# GUAR_PMT_SCORE_HB_HX

> This table contains HB Guarantor Payment Score history items.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCORE_DATE` | DATETIME |  | This item will store the date of the score. |
| 4 | `SCORE` | INTEGER |  | This history item will store the self-pay score. |
| 5 | `AVG_SP_LEVEL_C_NAME` | VARCHAR |  | This history item will store the average self-pay level for the score. |
| 6 | `UNCOLL_BALANCE_YN` | VARCHAR |  | This history item will store if there has been any uncollectable balance. |
| 7 | `ONLINE_PMT_YN` | VARCHAR |  | This history item will store if a payment through MyChart or another electronic portal was used for scoring. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

