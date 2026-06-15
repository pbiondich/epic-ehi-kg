# BILL_SCHED_PMT_REC_STS_HX

> This table contains the record status history from the Billing Scheduled Payment (BSP) master file.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_INSTANT_DTTM` | DATETIME (Attached) |  | Stores the instant that the record status was changed |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | Stores the user who changed the record status |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | Stores the action that was applied to the record status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

