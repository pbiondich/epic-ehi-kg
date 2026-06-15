# HEART_RANKING_STATUS_HX

> This table condenses heart status history to a start date and expiration date, and a pointer to the line in TXP_HEART_STATUS_HX where the details can be found.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_DT` | DATETIME |  | The date when the heart status in this row became active. |
| 4 | `END_DT` | DATETIME |  | The date when the heart status in this row expired. |
| 5 | `SOURCE_LINE` | INTEGER |  | The line in heart status history (HSB 30417) for this heart status. This corresponds to the LINE column in TXP_HEART_STATUS_HX. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

