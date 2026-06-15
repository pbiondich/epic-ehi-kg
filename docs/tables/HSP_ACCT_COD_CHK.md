# HSP_ACCT_COD_CHK

> This table stores the information about the coding validation checks.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the coding validation check. Multiple coding validation checks can occur on one hospital account, so each check has a unique line number. |
| 3 | `COD_CHK_TEXT` | VARCHAR |  | Coding Validation text |
| 4 | `COD_VAL_ALT_ITEM_YN` | VARCHAR |  | This item stores the fact that the validation check has been run on the alternate code set items on the diagnosis and procedure tabs on the Coding screen. |
| 5 | `COD_CHK_RULE_ID` | VARCHAR |  | This item tracks which coding validation rules the account failed. |
| 6 | `COD_CHK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 7 | `COD_CHK_CER_RULE_ID` | VARCHAR |  | Stores the coding validation check's general filter rule ID. |
| 8 | `COD_CHK_CER_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 9 | `COD_CHK_BWR_RULE_ID` | NUMERIC |  | Stores the coding validation check's billing filter rule ID. |
| 10 | `COD_CHK_BWR_RULE_ID_RULE_NAME` | VARCHAR |  | This column stores the name of the hospital billing workqueue rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

