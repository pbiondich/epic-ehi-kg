# OR_CASE_GI_TRIAGE_ASSESS

> This table is used for the GI Triage Assessment (I ORC 7909) item.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GI_TRIAGE_ASSESS_C_NAME` | VARCHAR | org | This field stores the assessment by the Gastrointestinal (GI) endoscopist doing triage to determine what the next steps for this patient are. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

