# STMT_EB_SCHED_AUTO_PAY

> This table stores the schedule payments that are scheduled to automatically charge the payment method on file for a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCHED_PMT_ID` | NUMERIC | FK→ | Stores the scheduled payment ID that is scheduled to automatically charge the payment method on file. |
| 4 | `SCHED_PMT_DATE` | DATETIME |  | Stores the date for which an automatic payment is scheduled. |
| 5 | `SCHED_PMT_AMT` | NUMERIC |  | Stores the amount for which an automatic payment is scheduled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

