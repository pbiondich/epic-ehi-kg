# REFLAB_VOID_REPOST

> This table contains transaction information for reference labs as related to the void and repost source transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RL_VID_REPST_ETR_ID` | NUMERIC |  | The unique ID of the reference lab void and repost source transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

