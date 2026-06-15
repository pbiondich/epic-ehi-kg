# BILL_SCHED_PMT_PP_HAR

> This table contains information about the hospital accounts on a payment plan record.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the hospital account that is associated with this payment plan. |
| 4 | `HAR_INITIAL_BAL` | NUMERIC |  | The initial balance the hospital account contributes to the payment plan. |
| 5 | `HAR_REMAINING_BAL` | NUMERIC |  | The remaining balance the hospital account contributes to the payment plan. |
| 6 | `HAR_PLAN_STATUS_C_NAME` | VARCHAR |  | The category ID of the status for this hospital account on the payment plan. |
| 7 | `HAR_PLAN_STATUS_UPDATE_DATE` | DATETIME |  | The date the hospital account's status was updated for the payment plan. |
| 8 | `IS_HAR_BAL_PRORATED_YN` | VARCHAR |  | This column indicates that this hospital account was set up as a prorated payment plan balance. 'Y' indicates that the hospital account was added to this payment plan with custom amounts or amounts from estimate or partial self-pay balances. 'N' or NULL indicates that the hospital account's full self-pay balance was added to the payment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

