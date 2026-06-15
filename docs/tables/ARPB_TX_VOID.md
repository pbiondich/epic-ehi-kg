# ARPB_TX_VOID

> This table contains information on transactions that were either: * Transferred * Voided * Reversed * Retroadjudicated.

**Primary key:** `TX_ID`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `OLD_ETR_ID` | NUMERIC |  | This item holds a pointer for a transaction that was reposted retroactively to the original transaction. |
| 3 | `REPOSTED_ETR_ID` | NUMERIC |  | This item stores a pointer to the old transaction in the case of charge correction or repost. |
| 4 | `REPOST_TYPE_C_NAME` | VARCHAR |  | This indicates the type of repost on the source transaction. This is either set to repost or correction. |
| 5 | `IS_RETRO_TX` | VARCHAR |  | This item serves as a flag to determine if this transaction was voided as a result of retroadjudication. |
| 6 | `TRANS_TX_ID` | NUMERIC |  | This item stores a pointer to the transaction ID that this transaction was transferred from. This item is only populated if a transaction was transferred from another transaction. |
| 7 | `TRANS_FROM_C_NAME` | VARCHAR |  | This item stores the void status of the transferred from transaction for this transaction. This item is only populated if this transaction was transferred from a different account. |
| 8 | `RETRO_CHARGE_ID` | NUMERIC |  | This item stores the transaction ID for the reposted transaction caused by the retroadjudication of this transaction. |
| 9 | `DEL_REVERSE_DATE` | DATETIME |  | This is the date that the transaction was voided or reversed. |
| 10 | `DEL_CHARGE_USER_ID` | VARCHAR |  | This item stores the user who voided this transaction. |
| 11 | `DEL_CHARGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `DEL_CHARGE_INSTANT` | DATETIME (Local) |  | This item stores the instant that a transaction was voided. |
| 13 | `IS_REVERSED_C_NAME` | VARCHAR |  | This flag determines if a transaction has been reversed. |
| 14 | `VOIDED_BY_MSG_YN` | VARCHAR |  | This flag is set if the charge was voided as a result of a Charge Router message. |
| 15 | `VOID_REASON_C_NAME` | VARCHAR | org | The reason for voiding/reversing category ID for the transaction |
| 16 | `VOIDED_BY_CGR_C_NAME` | VARCHAR |  | Indicates that a charge is voided by charge router. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

