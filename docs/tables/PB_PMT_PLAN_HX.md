# PB_PMT_PLAN_HX

> This table stores PB Payment Plan history items.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PLAN_START_DATE` | DATETIME |  | This item will store historical data of when payment plan started. |
| 4 | `PLAN_END_DATE` | DATETIME |  | This item will store historical data of when payment plan ended. |
| 5 | `MISSED_PMT_CNT` | INTEGER |  | This item will store the total number of missed payment plan payments. |
| 6 | `SCHEDULED_PMT_ID` | NUMERIC |  | This item will store historical data of scheduled payment record associated with the guarantor's payment plans. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

