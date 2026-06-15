# ARPB_TX_ACTIONS

> This table contains information about actions performed on professional billing transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 46

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given transaction. |
| 2 | `LINE` | INTEGER | PK | This column contains the line count for the information in this table. Each action associated with this transaction is stored on a separate line, one line for each entry. |
| 3 | `ACTION_TYPE_C_NAME` | VARCHAR |  | The action type category ID taken on the transaction. |
| 4 | `ACTION_DATE` | DATETIME |  | The date in which this action is performed. |
| 5 | `ACTION_AMOUNT` | NUMERIC |  | The amount associated with this action. |
| 6 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `DENIAL_CODE` | VARCHAR |  | The denial code associated with this action. |
| 8 | `DENIAL_CODE_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 9 | `POST_DATE` | DATETIME |  | The date this transaction was posted in calendar format. |
| 10 | `STMT_DATE` | DATETIME |  | The statement date of this transaction. |
| 11 | `OUT_AMOUNT_BEFORE` | NUMERIC |  | Outstanding amount of associated transaction before the action is performed. |
| 12 | `OUT_AMOUNT_AFTER` | NUMERIC |  | Outstanding amount of the associated transaction after the action is performed. |
| 13 | `INS_AMOUNT_BEFORE` | NUMERIC |  | Insurance amount of the associated transaction before the action is performed. |
| 14 | `INS_AMOUNT_AFTER` | NUMERIC |  | Insurance amount of the associated transaction after the action is performed. |
| 15 | `BEFORE_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 16 | `AFTER_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 17 | `BEFORE_CVG_ID` | NUMERIC |  | The coverage of the associated transaction before the action is performed. |
| 18 | `AFTER_CVG_ID` | NUMERIC |  | The coverage of the associated transaction after the action is performed. |
| 19 | `ACTION_USER_ID` | VARCHAR |  | The unique ID of the user who performed this action. |
| 20 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `ADJ_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 22 | `RMC_ID` | VARCHAR |  | The first reason code ID associated with this action. |
| 23 | `RMC_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 24 | `RMC_TWO_ID` | VARCHAR |  | The second reason code ID associated with this action. |
| 25 | `RMC_TWO_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 26 | `RMC_THREE_ID` | VARCHAR |  | The third reason code ID associated with this action. |
| 27 | `RMC_THREE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 28 | `RMC_FOUR_ID` | VARCHAR |  | The fourth reason code ID associated with this action. |
| 29 | `RMC_FOUR_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 30 | `PMT_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 31 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 32 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 33 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 34 | `LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 35 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `ACCOUNT_ID` | NUMERIC | FK→ | The internal ID of the record that maintains the patient's transactions. A patient may use more than one account and an account may contain more than one patient. |
| 37 | `PRIMARY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 38 | `MODIFIER_ONE` | VARCHAR |  | The first procedure modifier of the associated transaction. This is the external modifier, as it would be printed on the claim. |
| 39 | `MODIFIER_TWO` | VARCHAR |  | The second procedure modifier of the associated transaction. This is the external modifier, as it would be printed on the claim. |
| 40 | `MODIFIER_THREE` | VARCHAR |  | The third modifier of the associated transaction. This is the external modifier, as it would be printed on the claim. |
| 41 | `MODIFIER_FOUR` | VARCHAR |  | The fourth modifier of the associated transaction. This is the external modifier, as it would be printed on the claim. |
| 42 | `ASSIGNMENT_BEF_YN` | VARCHAR |  | This item is a Yes/No flag to determine if the transaction was assigned to insurance before the action on this line for this transaction. |
| 43 | `ASSIGNMENT_AFTER_YN` | VARCHAR |  | This item is a Yes/No flag to determine if the transaction was assigned to insurance after the action on this line for this transaction. |
| 44 | `ACTION_REMIT_CODES` | VARCHAR |  | This field stores a comma delimited list of external remittance codes for this transaction. |
| 45 | `ACTION_COMMENT` | VARCHAR |  | This is the system generated comment for this transaction. |
| 46 | `ACTION_DATETIME` | DATETIME (UTC) |  | The UTC date and time the action was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

