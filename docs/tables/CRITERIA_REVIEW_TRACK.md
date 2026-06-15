# CRITERIA_REVIEW_TRACK

> This table contains information for reviews in the Manual Review activity.

**Primary key:** `CRITERIA_REVIEW_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the criteria review record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OPEN_UTC_DTTM` | DATETIME (UTC) |  | The date and time the manual criteria review was opened. |
| 4 | `CLOSE_UTC_DTTM` | DATETIME (UTC) |  | The date and time the manual criteria review was accepted. |
| 5 | `STB_DELETES` | INTEGER |  | The number of characters deleted from the SmartText Box. |
| 6 | `STB_ADDS` | INTEGER |  | The number of characters added to the SmartText Box. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CRITERIA_REVIEW_ID` | [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | sole_pk | high |

