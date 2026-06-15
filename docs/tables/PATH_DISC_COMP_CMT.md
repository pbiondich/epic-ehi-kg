# PATH_DISC_COMP_CMT

> PATHWAY_DISC_CMT table contains comments for discontinuing and completing a patient pathway.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique ID of the patient pathway record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DISC_COMPL_COMMENT` | VARCHAR |  | Comments for discontinuing or completing the pathway |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

