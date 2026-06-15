# CASE_DX

> The CASE_DX table allows you to report on diagnoses associated with case records.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the diagnosis associated with this case record. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

