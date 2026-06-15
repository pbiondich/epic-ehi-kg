# LOADED_EXT_CVG_HX_VALS

> Clarity table for storing historical external coverage values.

**Primary key:** `EXTERNAL_CVG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_CVG_EFF_HX_DT` | DATETIME |  | The historical values from LCI 82 |
| 4 | `EXT_CVG_TERM_HX_DT` | DATETIME |  | Historical date values from I LCI 83 |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

