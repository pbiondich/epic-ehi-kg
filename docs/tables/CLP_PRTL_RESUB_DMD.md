# CLP_PRTL_RESUB_DMD

> This table stores claim partial resubmit/demand information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `UB_TCN` | VARCHAR |  | Stores uniform billing line control number. |
| 4 | `ORIG_UB_LN` | INTEGER |  | Stores original line number for partial uniform billing line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

