# ORGAN_CROSSMATCH

> Organ crossmatch types and results.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CROSSMATCH_TYPE_C_NAME` | VARCHAR | org | Cross match test type |
| 4 | `CROSSMATCH_RESULT_C_NAME` | VARCHAR | org | Crossmatch test result |
| 5 | `CROSSMATCH_FLOW` | NUMERIC |  | Crossmatch flow number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

