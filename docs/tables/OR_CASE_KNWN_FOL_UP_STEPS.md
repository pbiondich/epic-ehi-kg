# OR_CASE_KNWN_FOL_UP_STEPS

> This table is used for the Known Follow-Up Steps (I ORC 7902) item.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `KNWN_FOL_UP_STEPS_C_NAME` | VARCHAR | org | Question to let the performing endoscopist know what the patient's expectations are concerning the follow-up. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

