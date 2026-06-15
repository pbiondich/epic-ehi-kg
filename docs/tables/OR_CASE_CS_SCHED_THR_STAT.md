# OR_CASE_CS_SCHED_THR_STAT

> The OR_CASE_CS_SCHED_THR_STAT table contains details about whether the C-section should be scheduled before or after a certain gestational threshold.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CS_SCHED_THRESHOLD_STATUS_C_NAME` | VARCHAR | org | This item stores whether the C-section should be scheduled before or after a certain gestational threshold. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

