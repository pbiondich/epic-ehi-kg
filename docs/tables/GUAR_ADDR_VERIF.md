# GUAR_ADDR_VERIF

> This table contains information for guarantor address verification.

**Primary key:** `GUAR_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GUAR_ID` | NUMERIC | PK | Address verification - guarantor ID |
| 2 | `LINE` | INTEGER | PK | Address verification - line count for guarantors |
| 3 | `G_ADDR_INST_SENT` | DATETIME (Local) |  | The instant address verification message was sent. |
| 4 | `G_ADDR_INST_RECV` | DATETIME (Local) |  | The instant the address verification message was received. |
| 5 | `G_ADDR_ID_SENT` | VARCHAR |  | The ID of the address verification message that was sent. |
| 6 | `G_ADDR_ID_RECV` | VARCHAR |  | The ID of the address verification message that was received. |
| 7 | `G_ADDR_ACTN_C_NAME` | VARCHAR |  | Stores whether the sent or received address was kept for the guarantor. |
| 8 | `G_ADDR_TYP_SRCH` | VARCHAR |  | The type of search conducted for address verification. |
| 9 | `G_ADDR_REC_CR_ID` | VARCHAR |  | This points to the note record that contains the guarantor's address verification response with the credit information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

