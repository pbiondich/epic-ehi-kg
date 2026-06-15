# PMT_EOB_INFO_II

> The PMT_EOB_INFO_II table contains the Explanation of Benefits information given a transaction ID. This table contains multiple response items pertaining to PMT_EOB_INFO_I table.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The transaction ID. |
| 2 | `LINE` | INTEGER | PK | The line number of one EOB code which is different from EOB line number in PMT_EOB_INFO_I. |
| 3 | `AMOUNT` | NUMERIC |  | The Explanation of Benefits amount for a transaction. |
| 4 | `EOB_CODES` | VARCHAR |  | The EOB Code for this transaction. |
| 5 | `ADJ_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 6 | `ACTIONS` | VARCHAR |  | The action category ID for the payment Explanation of Benefits (EOB) action in this table. This column is frequently used to link to the ZC_TX_ACTION_TYPE table. |
| 7 | `SYSTEM_COMMENT` | VARCHAR |  | The comment put into the systems for this transaction. |
| 8 | `WINNINGRMC_ID` | VARCHAR |  | The winning remittance code ID from the remittance code. |
| 9 | `WINNINGRMC_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 10 | `TX_MATCH_DATE` | DATETIME |  | The date when the charge was matched to the payment. |
| 11 | `PEOB_EOB_RMC_IDS` | VARCHAR |  | The remittance code specified by the payer in its Explanation of Benefits (EOB). If this contains a comma delimited list, we will only show the first remittance code. |
| 12 | `PEOB_EOB_AMOUNT` | NUMERIC |  | The not allowed amount associated with the Remittance Codes that the payor specifies in its Explanation of Benefit (EOB). |
| 13 | `PEOB_EOB_GRPCODE_C_NAME` | VARCHAR | org | The Explanation Of Benefits group code category ID for the transaction from insurance payment posting. |
| 14 | `PEOB_DUP_DENIAL_C_NAME` | VARCHAR |  | This item contains the duplicate denial reason calculated at the time the payment is distributed to the invoice. It is populated only when a duplicate denial (Remittance code external ID=18) is present. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

