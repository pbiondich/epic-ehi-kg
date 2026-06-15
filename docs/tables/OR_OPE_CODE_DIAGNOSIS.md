# OR_OPE_CODE_DIAGNOSIS

> This table contains the diagnoses associated with procedure codes.

**Primary key:** `OPE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OPE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the orders performed record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the procedure code. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of the diagnosis associated with the procedure code. |
| 4 | `PROC_CODE_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

