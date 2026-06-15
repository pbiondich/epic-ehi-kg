# HSP_ACCOUNT_5

> This table contains hospital account information from the Hospital Accounts Receivable (HAR) master file. This fifth hospital account table has the same basic structure as HSP_ACCOUNT, HSP_ACCOUNT_2, HSP_ACCOUNT_3, and HSP_ACCOUNT_4, but was created as a fifth table to prevent the other tables from getting any larger. It excludes Professional Billing accounts in classic PB self-pay service areas.

**Overflow of:** [HSP_ACCOUNT](HSP_ACCOUNT.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 22  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the hospital account record. |
| 2 | `AR_CLASSIFICATION_C_NAME` | VARCHAR |  | This column stores the A/R classification of this account. |
| 3 | `INITIAL_EXPECTED_ALLOWED_AMT` | NUMERIC |  | The sum of the expected allowed amounts for the primary claims initially sent. Doesn't include any expected reimbursement from interim claims. |
| 4 | `CURRENT_EXPECTED_ALLOWED_AMT` | NUMERIC |  | The sum of the expected allowed amounts for the primary claims last sent. Doesn't include any expected reimbursement from interim claims. |
| 5 | `CHANGE_IN_EXPECTED_ALLOWED_AMT` | NUMERIC |  | The difference between the sums of the expected allowed amounts of the primary claims initially sent and of the primary claims last sent. Doesn't include any expected reimbursement from interim claims. |
| 6 | `INITIAL_CLM_CLASS_C_NAME` | VARCHAR | org | The claim class used when sending the initial primary claims. Represented with a patient class category ID for the hospital account. |
| 7 | `INITIAL_CLM_BASE_CLASS_C_NAME` | VARCHAR |  | The claim base class used when sending the initial primary claims. Represented with an account base class category ID for the hospital account. |
| 8 | `CUR_CLM_CLASS_C_NAME` | VARCHAR |  | The claim class used for currently sent or closed primary claims. Represented with a patient class category ID for the hospital account. |
| 9 | `CUR_CLM_BASE_CLASS_C_NAME` | VARCHAR |  | The claim base class used for currently sent or closed primary claims. Represented with an account base class category ID for the hospital account. |
| 10 | `DAYS_FROM_INIT_TO_CUR_CLM_ACPT` | INTEGER |  | The maximum of the number of days between the accept dates for the first and last claim sent for each primary payer for this hospital account. |
| 11 | `PAYER_DOWNGRADE_TYPE_C_NAME` | VARCHAR |  | The payer downgrade request type category ID for the hospital account. This category is the type of downgrade requested when the primary payer tries to dispute the level of care of the HAR. NULL if no such attempt was made. |
| 12 | `PAYER_DOWNGRADE_OUTCOME_C_NAME` | VARCHAR |  | Whether the primary payer's attempt to lower the level of care of the account was appropriate and whether it was overturned or led to a downgrade. NULL if no such attempt was made by the Primary Payer. |
| 13 | `PAYER_DOWNGRADE_BDC_ID` | NUMERIC |  | The unique ID of the follow-up record that is the primary payer's attempt to lower the level of care of the account. NULL if no such attempt was made by the primary payer. This column is frequently used to link to the BDC_INFO table. |
| 14 | `LAST_SP_LEVEL_UPDATE_DATE` | DATETIME |  | Retrieves the last date when the self-pay follow-up cycle was updated. |
| 15 | `OVER_TIME_CODING_RECORD_ID` | NUMERIC |  | The COD record used for Coding Over Time on the account. |
| 16 | `PMT_DISCNT_PROMOTION_ID` | NUMERIC |  | Stores the active discount offer that a visit account qualifies for. |
| 17 | `PMT_DISCNT_PROMOTION_ID_PROMOTION_NAME` | VARCHAR |  | The promotion record name. |
| 18 | `PMT_DISCNT_OFFER_STS_C_NAME` | VARCHAR |  | The status of the payment-based discount offer |
| 19 | `PMT_DISCNT_INELIG_RSN_C_NAME` | VARCHAR |  | The reason this hospital account is ineligible for a discount offer. |
| 20 | `REV_SPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 21 | `REV_SUBSPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 22 | `CHANGE_EAR_FLAG_YN` | VARCHAR |  | Indicates whether the HAR’s coverage list originated from a source guarantor as a result of change guarantor. When set, retro processes will bypass the HAR. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [HSP_ACCOUNT](HSP_ACCOUNT.md).

