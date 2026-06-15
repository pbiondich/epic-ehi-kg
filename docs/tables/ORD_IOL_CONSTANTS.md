# ORD_IOL_CONSTANTS

> List of constants and their associated values in lens calculations.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CALC_IOL_CONSTANTS` | VARCHAR |  | Constants for a calculated IOL |
| 4 | `CALC_IOL_CONSTVALS` | VARCHAR |  | Values associated with constants for a calculated IOL |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

