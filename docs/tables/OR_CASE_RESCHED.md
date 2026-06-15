# OR_CASE_RESCHED

> The OR_CASE_RESCHED table contains OR management system case reschedule information.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the rescheduling information for the case. |
| 3 | `RESCHEDULE_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `RESCHEDULE_NEED_C_NAME` | VARCHAR | org | The category value indication the reason the reschedule is needed. |
| 5 | `RESCHEDULE_CMT` | VARCHAR |  | The rescheduling comment of the rescheduled case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

