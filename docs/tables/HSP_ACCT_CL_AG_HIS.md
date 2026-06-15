# HSP_ACCT_CL_AG_HIS

> This table contains collection agency history information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated collection agency information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each collection agency history will have its own line number. |
| 3 | `AGNCY_HST_DT_OF_CH` | DATETIME |  | Date hospital account was either assigned to or withdrawn from the collection agency. |
| 4 | `AGNC_HST_CHG_TP_C_NAME` | VARCHAR |  | Change in the collection agency status. 1-Assign to agency 2-Withdraw from agency |
| 5 | `AGNCY_HST_AGNCY_ID` | NUMERIC |  | ID of collection agency hospital account has been assigned to. |
| 6 | `AGNCY_HST_AGNCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 7 | `AGN_HST_COL_ACT_C_NAME` | VARCHAR |  | This column stores the type of collection action done on the hospital account: 1-Send Letter, 2-Pre-Collect, 3-Bad Debt, 4-Return to Self-Pay, 5-Write Off, 6-Create Billing Note, 7-Change Notification Date, 8-Add to Queue, 10- Outsource Account, 11- Return from Outsource, 12-Change Agency, 13-Set Billing Indicator, or 14-Send SmartText Letter. |
| 8 | `AGNCY_HST_ACCT_BAL` | NUMERIC |  | Account balance on the hospital account that was sent to collections. |
| 9 | `AGNCY_HST_CHG_RSN_C_NAME` | VARCHAR | org | This column contains the reason why the account was placed or withdrawn from the agency. Refer to the AGNC_HST_CHG_TP_C to know whether this was related to an assign or withdraw. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

