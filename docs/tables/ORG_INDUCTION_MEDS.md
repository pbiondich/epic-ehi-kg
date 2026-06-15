# ORG_INDUCTION_MEDS

> This table lists organ induction medications used.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INDUCTION_MEDS_C_NAME` | VARCHAR | org | List of induction medications used |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

