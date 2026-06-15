# GUAR_PMT_SCORE_REPL

> This table contains information for the HB and PB Guarantor Payment Score Items.

**Primary key:** `ACCOUNT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the guarantor record. |
| 2 | `HB_SCORE` | INTEGER |  | The guarantor's hospital billing payment history score. |
| 3 | `HB_SCORE_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the guarantor was most recently scored. |
| 4 | `PB_SCORE` | INTEGER |  | The guarantor's professional billing payment history score. |
| 5 | `PB_SCORE_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the guarantor was most recently scored. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

