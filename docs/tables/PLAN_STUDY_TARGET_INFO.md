# PLAN_STUDY_TARGET_INFO

> This table contains the target version and instructions information associated with the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_TARGET_VERSION` | VARCHAR |  | The target study version when the study amendment banner is appearing above treatment plan. |
| 4 | `STUDY_TARGET_INSTRUCTIONS` | VARCHAR |  | The target study version information when the study amendment banner is appearing above the treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

