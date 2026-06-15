# OR_CASE_CPT_TXT

> The OR_CASE_CPT_TXT table contains the list of free-text CPT(R) codes entered for a case record.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CPT_CODE_TXT` | VARCHAR |  | The free-text Current Procedural Terminology (CPT(R)) codes associated with the procedures in this case request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

