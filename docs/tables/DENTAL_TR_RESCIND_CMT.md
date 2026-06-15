# DENTAL_TR_RESCIND_CMT

> This table contains the comments entered when a user rescinds dental treatment plan approval.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the treatment plan record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_TR_RSCND_CMT` | VARCHAR |  | The comments entered when a user rescinds dental treatment plan approval. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

