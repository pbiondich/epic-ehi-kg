# OB_HSB_DEL_CMPLCTN

> This table contains information about the complications encountered during the delivery for this pregnancy.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OB_DEL_COMPLIC_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

