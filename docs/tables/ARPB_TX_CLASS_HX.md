# ARPB_TX_CLASS_HX

> Classification history for Professional Billing Transactions. Indicates when the transaction has moved between Active AR, External AR, and Bad Debt.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLASS_HX_INST` | DATETIME (Local) |  | The instant when the transaction's classification changed. |
| 4 | `CLASS_HX_CHANGE_C_NAME` | VARCHAR |  | The classification change category number of the transaction. |
| 5 | `CLASS_HX_AMOUNT` | NUMERIC |  | The amount of the transaction that is associated with the classification change of the transaction in dollars. |
| 6 | `CLASS_HX_USER_ID` | VARCHAR |  | The unique ID associated with the user who made the classification change. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `CLASS_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CLASS_HX_LN` | INTEGER |  | The line associated with the matching transactions group that this classification change corresponds to. Used to easily link the classification change to the distribution/undistribution history of the transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

