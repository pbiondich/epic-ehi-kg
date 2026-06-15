# HSP_CLP_PROC_INFO

> Stores information about the procedure codes for a given claim print record.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the procedure associated with this claim. Multiple procedures can be associated with this claim. |
| 3 | `PROC_CODE` | VARCHAR |  | A procedure code on this claim. |
| 4 | `PROC_DATE` | DATETIME |  | The date for this procedure code. |
| 5 | `CODE_SET_C` | INTEGER |  | The procedure code's code set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

