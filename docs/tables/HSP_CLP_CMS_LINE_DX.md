# HSP_CLP_CMS_LINE_DX

> This table contains linkages between service lines and diagnoses for Hospital Billing claims.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `LINE_DX_SVC_LINE` | INTEGER |  | The claim line number for a service line - diagnosis relationship. |
| 4 | `LINE_DX_PIECE` | INTEGER |  | The piece number for a service line - diagnosis relationship. |
| 5 | `LINE_DX_POINTER` | INTEGER |  | The diagnosis pointer from a single piece of a service line - diagnosis relationship. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

