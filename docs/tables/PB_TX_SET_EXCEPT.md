# PB_TX_SET_EXCEPT

> The PB_TX_SET_EXCEPT table lists exceptions entered for a premium billing payment transaction set.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | Line counter for the exception on the transaction set. |
| 3 | `EXCEPT_PB_TX_ID` | VARCHAR |  | The unique ID of the premium billing detailed transaction associated with the exception. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

