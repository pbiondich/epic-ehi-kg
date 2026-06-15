# DENT_TR_RESCIND_CMT_HX_RM

> This table extracts the related multiple response Dental: Treatment Approval Rescinded Comment Hx (I TPL 94134) item that contains comments entered when dental treatment plan approval is rescinded.

**Primary key:** `TREATMENT_PLAN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the treatment plan record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the treatment record. Together with TREATMENT_PLAN_ID, this forms the foreign key to the TR_RESCIND_CMT_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number for one of the multiple rescind comments associated with the treatment and the historical instant from the TR_RESCIND_CMT_HX table |
| 4 | `DENTTR_RSCND_CMT_HX` | VARCHAR |  | The revision history for the comments entered when a user rescinds dental treatment plan approval. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

