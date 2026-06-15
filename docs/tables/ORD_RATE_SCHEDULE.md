# ORD_RATE_SCHEDULE

> Schedule of rates for an order. Contains a table of rates and durations for those rates.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RATE_SCHED_RATE_AMT` | VARCHAR |  | The rate amount for a specific segment of a medication's rate schedule. |
| 4 | `RATE_SCHED_RATE_U_C_NAME` | VARCHAR | org | The med & dose unit category ID for a specific segment of a medication's rate schedule. |
| 5 | `RATE_SCHED_DUR_AMT` | VARCHAR |  | The time amount for a specific segment of a medication's rate schedule. |
| 6 | `RATE_SCHED_DUR_U_C_NAME` | VARCHAR |  | The time unit category ID for a specific segment of a medication's rate schedule. |
| 7 | `RATE_SCHED_PARAM_C_NAME` | VARCHAR |  | The dosing parameter type category ID which was used to generate a segment of the rate schedule for the order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

