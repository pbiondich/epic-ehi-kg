# EXPECTD_GOAL_ALERT

> It contains the information about the user and the instant for the goal alert for the care plan.

**Primary key:** `CARE_INTG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CARE_INTG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the careplan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GOAL_ALERT_INS_DTTM` | DATETIME (Local) |  | The date and time of the expected goal alert. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |

