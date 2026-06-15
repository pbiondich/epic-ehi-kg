# BILL_SCHED_PMT_PAT_CSN

> This table contains the patient contacts on the scheduled payment from the Billing Scheduled Payment (BSP) master file.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column stores the patient contact serial number (CSN) associated with the scheduled payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

