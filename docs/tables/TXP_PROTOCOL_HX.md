# TXP_PROTOCOL_HX

> History of changes to a patient's transplant protocols.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_PROTOCOL_HX_C_NAME` | VARCHAR | org | Store the history of the changes to transplant protocols |
| 4 | `TX_PROTOCOL_WHO_ID` | VARCHAR |  | User who changed the transplant protocol |
| 5 | `TX_PROTOCOL_WHO_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TX_PROTOCOL_HX_INST` | DATETIME (Local) |  | Instant of update for the transplant protocol. |
| 7 | `TX_PROTCOL_HX_ACT_C_NAME` | VARCHAR |  | Stores whether a protocol was added or removed from the episode. |
| 8 | `BMT_PROTOCOL_HX_C_NAME` | VARCHAR | org | Stores the history of the changes to blood and marrow transplant protocols. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

