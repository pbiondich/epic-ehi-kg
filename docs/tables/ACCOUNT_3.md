# ACCOUNT_3

> Accounts contain information about billing for services, while coverages contain information about insurance payors, benefits, subscribers, and members. This table contains one row for each account record in your system.

**Overflow of:** [ACCOUNT](ACCOUNT.md)  
**Primary key:** `ACCOUNT_ID`  
**Columns:** 37  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the account record. |
| 2 | `PNB_TYPE_C_NAME` | VARCHAR |  | The Posted Not Billed rule type category ID for the guarantor account. |
| 3 | `ALWAYS_SELF_PAY_YN` | VARCHAR |  | Indicates whether this account should always be self-pay. |
| 4 | `REFERRAL_SOURCE_COMMENT` | VARCHAR |  | The comment associated with the referral source in ACCOUNT.REFERRAL_SOURCE. |
| 5 | `BILLING_TITLE_C_NAME` | VARCHAR | org | The category ID of the title used to address the person associated with the guarantor account. |
| 6 | `HB_NEXT_BAL_NOTIF_DT` | DATETIME |  | The date on which the next balance notification will be sent to the guarantor for their HB/SBO balances. |
| 7 | `HB_NEXT_AUTOPAY_DT` | DATETIME |  | The next Auto Pay date for guarantor set up with a payment plan on Auto Pay. |
| 8 | `PB_NEXT_BAL_NOTIF_DT` | DATETIME |  | Stores the date on which the next balance notification will be sent to the guarantor for their PB balances. |
| 9 | `FAMILY_INCOME` | NUMERIC |  | The annual family income for this account. |
| 10 | `CLEAR_FOLLOWUP_FLAG` | INTEGER |  | Stores whether the account should be considered for a new follow-up cycle by nightly processing. |
| 11 | `FOL_UP_LETTER` | VARCHAR |  | The follow-up letter associated with the account. |
| 12 | `FOL_UP_TEMPLATE` | VARCHAR |  | The comma-delimited string of SmartText records associated with the account. |
| 13 | `FAMILY_SIZE` | INTEGER |  | The number of family members associated with the account. |
| 14 | `OUTSTANDING_ACCT_C_NAME` | VARCHAR |  | This column specifies if the account is outstanding or not. |
| 15 | `PMT_PLAN_SECOND_DUE_DT` | INTEGER |  | Contains the day of the month that the second bi-monthly payment is due. |
| 16 | `PMT_PLAN_EXP_AMT` | NUMERIC |  | The expected paid amount of the payment plan. This amount is updated by nightly processing. The amount is incremented by the monthly amount when the closed batch date equals the current due date. |
| 17 | `PMT_PLAN_NEXT_DUE_DT` | DATETIME |  | Next due date of the payment plan. The date is updated by nightly processing when the closed batch date is the current due date. |
| 18 | `PMT_PLAN_AUTOPAY_DUE_DT` | DATETIME |  | The date when the card will be charged for the auto-pay payment plan. |
| 19 | `PMT_PLAN_AUTOPAY_DAY` | INTEGER |  | The day of the month when card will be automatically charged. |
| 20 | `STMT_HOLD_REASON_TEXT` | VARCHAR |  | The free text information related to the reason why the account was held in PB statement processing. |
| 21 | `HB_IN_PROG_SP_BAL` | NUMERIC |  | This item stores the HB self-pay balance of in progress accounts for the guarantor, excluding hospital accounts in external AR or bad debt. In progress accounts are those that have not yet been billed to self-pay. |
| 22 | `HB_IN_PROG_BAD_DEBT_SP_BAL` | NUMERIC |  | This item stores the HB self-pay balance of in progress bad debt accounts for the guarantor. In progress accounts are those that have not yet been billed to self-pay. |
| 23 | `HB_IN_PROG_EXTERNAL_AR_SP_BAL` | NUMERIC |  | This item stores the HB self-pay balance of in progress external AR accounts for the guarantor. In progress accounts are those that have not yet been billed to self-pay. |
| 24 | `HB_CONTEST_SP_BAL` | NUMERIC |  | This item stores the HB self-pay balance of contested accounts for the guarantor, excluding hospital accounts in external AR or bad debt. |
| 25 | `HB_CONTEST_BAD_DEBT_SP_BAL` | NUMERIC |  | This item stores the HB bad debt self-pay balance of contested accounts for the guarantor. |
| 26 | `HB_CONTEST_EXTERNAL_AR_SP_BAL` | NUMERIC |  | This item stores the HB External AR self-pay balance of contested accounts for the guarantor. |
| 27 | `DECLINED_FA_UTC_DTTM` | DATETIME (UTC) |  | The most recent time a guarantor declined financial assistance. |
| 28 | `PB_CONTEST_SP_BAL` | NUMERIC |  | The total contested PB HAR balance for the guarantor |
| 29 | `PB_CONTEST_EXTERNAL_AR_SP_BAL` | NUMERIC |  | The total contested external A/R PB HAR balance for the guarantor |
| 30 | `EB_PMT_PLAN_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the HB/SBO payment plan agreement record for this guarantor. |
| 31 | `PB_PMT_PLAN_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the PB payment plan agreement record for this guarantor. Only used in service areas that use PB Visit-Based Self-Pay Follow-up. |
| 32 | `PB_PMT_HX_SCORE` | INTEGER |  | The guarantor's PB Payment History Score. |
| 33 | `HB_PMT_HX_SCORE` | INTEGER |  | The guarantor's HB Payment History Score. |
| 34 | `EB_PMT_HX_SCORE` | INTEGER |  | The guarantor's EB Payment History Score. |
| 35 | `SCORE_LAST_CALC_UTC_DTTM` | DATETIME (UTC) |  | The last instant the guarantor's payment history score was calculated. (UTC) |
| 36 | `SCORE_LAST_CALC_LOCAL_DTTM` | DATETIME (Local) |  | The last instant the guarantor's payment history score was calculated. (Local) |
| 37 | `EPISODE_ID` | NUMERIC | FK→ | The associated workers' compensation episode (HSB) record for workers' compensation guarantors. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

## Joined in

Inbound joins are tracked on the logical base [ACCOUNT](ACCOUNT.md).

