# BILL_SCHED_PMT_PP_HAR_EST

> This table contains pre-service estimates directly linked to hospital accounts that are attached to a payment plan.

**Primary key:** `SCHED_PMT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ESTIMATE_ID` | NUMERIC | shared | The unique ID of the estimate record associated with a hospital account on a payment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

