# TXP_NEXT_REV_HX

> Next review date history for transplant episodes.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_NEXT_REV_DT` | DATETIME |  | Stores the history of next review dates for the transplant episode. |
| 4 | `HX_NEXT_REV_USER_ID` | VARCHAR |  | The user who changed the next review date for the transplant episode. |
| 5 | `HX_NEXT_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_NEXT_REV_INST` | DATETIME (Local) |  | Stores the instant on which the next review date for the transplant episode was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

