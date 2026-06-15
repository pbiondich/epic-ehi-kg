# BILL_SCHED_PMT_PP_EST

> This table contains information about estimates on a payment plan.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESTIMATE_ID` | NUMERIC | shared | The unique ID of the pre-service estimate record for the payment plan. |
| 4 | `ESTIMATE_INITIAL_BALANCE` | NUMERIC |  | The initial responsibility the pre-service estimate contributes to the payment plan. |
| 5 | `ESTIMATE_REMAINING_BALANCE` | NUMERIC |  | The remaining responsibility the pre-service estimate contributes to the payment plan. |
| 6 | `ESTIMATE_STATUS_C_NAME` | VARCHAR |  | The category ID of the pre-service estimate's status on the payment plan. |
| 7 | `ESTIMATE_STATUS_UPDATE_DATE` | DATETIME |  | The most recent date the pre-service estimate's status on the payment plan was updated. |
| 8 | `ESTIMATE_COVERED_BY_EST_AMT` | NUMERIC |  | The portion of the pre-service estimate's initial balance that is still estimate responsibility. This amount is reduced by charges moving to Self-Pay on hospital accounts linked to the estimate. |
| 9 | `ESTIMATE_COVERED_BY_HAR_AMT` | NUMERIC |  | The portion of the pre-service estimate's initial balance that is applied to hospital accounts linked to the estimate. This amount plus the estimate responsibility remaining always equals the initial balance of the estimate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

