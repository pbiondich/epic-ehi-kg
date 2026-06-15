# TPL_STUDY_ENROLMTS

> This table stores a list of the patient's research study enrollments that are associated with a given treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENROLLMENT_ID` | NUMERIC |  | This item stores a list of the patient's research study enrollments (LAR records) that are linked to this treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

