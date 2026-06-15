# HSP_ACCT_STMT_HX

> This table contains hospital account statement history information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple statements and detail bills can be sent for one hospital account, each statement or detail bill will have a unique line number. Note: This table includes information on demand statements and detail bills. Detail bills are sent at the hospital account level. Statements can be sent at the guarantor or hospital account level. When statements are sent at the guarantor level, a statement entry is made for each hospital account for which the guarantor is responsible. |
| 3 | `STMT_HX_DATE` | DATETIME |  | The date on which a statement or detail bill was sent. |
| 4 | `TOTAL_PAYMENTS` | NUMERIC |  | The total payments that appeared on a statement or detail bill. |
| 5 | `NEW_PAYMENTS` | NUMERIC |  | The total new payments that appeared on a statement. This column does not apply to detail bills. |
| 6 | `TOTAL_ADJUSTMENTS` | NUMERIC |  | The total adjustments that appeared on a statement or detail bill. |
| 7 | `TOTAL_DUE` | NUMERIC |  | The total due that appeared on a statement or detail bill. |
| 8 | `ACCT_SLFPYST_HA_C_NAME` | VARCHAR |  | The self pay status of the hospital account. |
| 9 | `TOTAL_BALANCE` | NUMERIC |  | The total hospital account balance that appeared on this statement or detail bill. |
| 10 | `PREV_INS_BAL` | NUMERIC |  | This item stores the previous insurance balance for this hospital account shown on a statement. |
| 11 | `CUR_INS_BAL` | NUMERIC |  | This item holds the current insurance balance for this hospital account shown on a statement. |
| 12 | `PB_PREV_BAL` | NUMERIC |  | This column stores the previous professional patient balance that appeared on a statement. This column only applies if single billing office is enabled. This column does not apply to detail bills. |
| 13 | `PB_TOTAL_CHARGES` | NUMERIC |  | This column stores the total professional charges that appeared on a statement or detail bill. This column only applies if single billing office is enabled. |
| 14 | `PB_NEW_CHARGES` | NUMERIC |  | This column stores the total new professional charges that appeared on a statement. This column only applies if single billing office is enabled. This column does not apply to detail bills. |
| 15 | `PB_TOTAL_PAYMENTS` | NUMERIC |  | This column stores the total professional payments that appeared on a statement or detail bill. This column only applies if single billing office is enabled. |
| 16 | `PB_NEW_PAYMENTS` | NUMERIC |  | This column stores the total new professional payments that appeared on a statement. This column only applies if single billing office is enabled. This column does not apply to detail bills. |
| 17 | `PB_TOTAL_ADJSTMNTS` | NUMERIC |  | This column stores the total professional adjustments that appeared on a statement or detail bill. This column only applies if single billing office is enabled. |
| 18 | `PB_NEW_ADJUSTMENTS` | NUMERIC |  | This column stores the total new professional adjustments that appeared on a statement. This column only applies if single billing office is enabled. This column does not apply to detail bills. |
| 19 | `PB_TOTAL_DUE` | NUMERIC |  | This column stores the total professional amount due that appeared on a statement or detail bill. This column only applies if single billing office is enabled. |
| 20 | `PB_TOTAL_BALANCE` | NUMERIC |  | This column stores the total professional patient balance that appeared on a statement or detail bill. This column only applies if single billing office is enabled. |
| 21 | `PB_PREV_INS_BAL` | NUMERIC |  | This item stores the previous professional insurance balance for this hospital account shown on a statement. This column only applies if single billing office is enabled. |
| 22 | `PB_CUR_INS_BAL` | NUMERIC |  | This item stores the current professional insurance balance for this hospital account shown on a statement. This column only applies if single billing office is enabled. |
| 23 | `STMT_DET_BILL_FLG_C_NAME` | VARCHAR | org | Denotes whether a document sent was a statement or a detail bill. |
| 24 | `STMT_COLL_STS_C_NAME` | VARCHAR |  | Stores the collection status of the hospital account on a particular statement. |
| 25 | `STMT_COLL_AGENCY_ID` | NUMERIC |  | Stores the collection agency of the hospital account on a particular statement. |
| 26 | `STMT_COLL_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 27 | `STMT_DVRY_MTD_C_NAME` | VARCHAR |  | Stores how the statement/detail bill was delivered. |
| 28 | `STMT_HX_CNTST_BAL` | NUMERIC |  | Stores the contested balance on the statement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

