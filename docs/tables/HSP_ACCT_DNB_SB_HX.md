# HSP_ACCT_DNB_SB_HX

> This table holds the history items of adding and removing discharged-not-billed (DNBs), Stop Bills, and Validation Checks to Hospital Accounts. This includes the user that initiated the action, when the action was initiated, and what rule was used to initiate the action.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID with related stop bill/DNB/validation check information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each piece of stop bill/DNB/validation check history will have its own line number. |
| 3 | `HX_DNBSB_ADD_USR_ID` | VARCHAR |  | This column stores the unique identifier for the user who placed the stop bill/DNB/validation check on the hospital account. |
| 4 | `HX_DNBSB_ADD_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `HX_DNBSB_RMV_USR_ID` | VARCHAR |  | This column stores the unique identifier for the user who removed the stop bill/DNB/validation check from the hospital account. |
| 6 | `HX_DNBSB_RMV_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HX_BILLING_INDC_C_NAME` | VARCHAR | org | This is the billing indicator category that was added or removed from the account. |
| 8 | `HX_FILTER_CER_RULE_ID` | VARCHAR |  | This column stores the unique identifier for the edit check's CER filter rule. |
| 9 | `HX_FILTER_CER_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 10 | `HX_FILTER_BWR_RULE_ID` | NUMERIC |  | This column stores the unique identifier for the edit check's BWR filter rule. |
| 11 | `HX_FILTER_BWR_RULE_ID_RULE_NAME` | VARCHAR |  | This column stores the name of the hospital billing workqueue rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

