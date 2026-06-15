# BILL_SCHED_PMT_STS_HX

> This table contains the payment schedule status history from the Billing Scheduled Payment (BSP) master file.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCHD_STS_HX_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when the schedule status was changed. |
| 4 | `SCHD_STS_HX_STS_C_NAME` | VARCHAR |  | Stores the status to which the schedule was changed. |
| 5 | `SCHD_STS_HX_USER_ID` | VARCHAR |  | This column stores the user who changed the schedule status. |
| 6 | `SCHD_STS_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `STS_HX_MYPT_ID` | VARCHAR |  | Stores the MyChart account that changed the status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

