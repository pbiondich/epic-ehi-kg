# HSP_ACCT_ABS_CHK

> This table stores the abstract validation checks information.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABS_CHK_RULE_ID` | VARCHAR |  | This column stores the abstracting validation rules the account failed. |
| 4 | `ABS_CHK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 5 | `ABS_CHK_CER_RULE_ID` | VARCHAR |  | This column stores the unique identifier for the CER filter rule used in the abstracting validation check. |
| 6 | `ABS_CHK_CER_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 7 | `ABS_CHK_BWR_RULE_ID` | NUMERIC |  | This column stores the unique identifier for the BWR filter rule used in the abstracting validation check. |
| 8 | `ABS_CHK_BWR_RULE_ID_RULE_NAME` | VARCHAR |  | This column stores the name of the hospital billing workqueue rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

