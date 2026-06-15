# HSP_ACCOUNT_4

> This table contains hospital account information from the Hospital Accounts Receivable (HAR) master file. This fourth hospital account table has the same basic structure as HSP_ACCOUNT, HSP_ACCOUNT_2 and HSP_ACCOUNT_3, but was created as a fourth table to prevent the other tables from getting any larger. This table will exclude professional billing accounts in classic PB self-pay service areas.

**Overflow of:** [HSP_ACCOUNT](HSP_ACCOUNT.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 47  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the hospital account. |
| 2 | `EPISODE_ID` | NUMERIC | FK→ | This column stores the unique identifier for the bundled episode record for this row. This column will only be populated for hospital accounts that have been linked to a bundled episode and is frequently used to link to the BND_EPSD_INFO table. This column is being transitioned to the HSP_ACCT_BND_EPSD_INFO__BND_EPSD_EPISODE_ID column. This column will continue to work in the following manner: 1. Data in Bundled Episode (I HAR 10001) will continue to be extracted by this column. |
| 3 | `SRCHG_POSTED` | NUMERIC |  | Stores the surcharge amount posted on the hospital account. |
| 4 | `SRCHG_PAID` | NUMERIC |  | Stores the surcharge amount paid on the hospital account. |
| 5 | `SRCHG_PAID_SELFPAY` | NUMERIC |  | Stores the surcharge amount paid by patient on the hospital account. |
| 6 | `SRCHG_PAID_INS` | NUMERIC |  | Stores the surcharge amount paid by insurance on the hospital account. |
| 7 | `TRAUMA_ADMISSION_C_NAME` | VARCHAR | org | Whether the admission is a trauma case. |
| 8 | `PSYCH_ADMISSION_C_NAME` | VARCHAR | org | The nature of psychiatric admission. |
| 9 | `REHAB_ADMISSION_C_NAME` | VARCHAR | org | The code for rehabilitation admission class from the Guide for the Uniform Data Set for Medical Rehabilitation. |
| 10 | `REHAB_IMPAIRMENT_C_NAME` | VARCHAR | org | The group code for rehabilitation impairment from the Guide for the Uniform Data Set for Medical Rehabilitation. |
| 11 | `RANCHO_LEVEL_C_NAME` | VARCHAR | org | This column stores the Rancho level used to determine diagnosis-related groups (DRG) for rehabilitation services. |
| 12 | `SVC_SUCCESS_C_NAME` | VARCHAR |  | Holds whether the account was successfully marked "Coding Complete" by Simple Visit Coding. |
| 13 | `HH_COVCHG_DT` | DATETIME |  | The home health coverage change date for the hospital account. |
| 14 | `HH_COVCHG_DC_DISP_C_NAME` | VARCHAR | org | This is the discharge disposition value that should be used in the case of a home health coverage change. |
| 15 | `HAR_EXTRACT_TRIGGER_DATE` | DATETIME |  | Stores the date that hospital account information was changed that will cause the extraction of a closed hospital account. |
| 16 | `IRF_PAI_REGISTRY_DATA_ID` | NUMERIC |  | This column stores the unique identifier for the Inpatient Rehabilitation Facility Patient Assessment Instrument (IRF-PAI) record associated with the hospital account. The IRF-PAI record stores the assessment data collected for rehabilitation services. |
| 17 | `PB_SPLIT_REF_DATE` | DATETIME |  | This column stores the beginning service date of the date range used to split professional billing hospital accounts. Calculated based on the inpatient stay's admission date. |
| 18 | `BILLING_LENGTH_OF_STAY` | INTEGER |  | This column stores the billing length of stay (LOS) for the inpatient portion of the hospital account. The billing LOS is calculated as the number of days between admission and discharge. |
| 19 | `INST_INJURY_UTC_DTTM` | DATETIME (UTC) |  | This column stores the Coordinated Universal Time (UTC) instant when the injury happened. Used along with the Injury Codes in Denmark. |
| 20 | `TOT_INS_PMT` | NUMERIC |  | The total amount of insurance payments posted to this account, not including refunds. |
| 21 | `TOT_INS_RFND` | NUMERIC |  | The total amount of insurance refunds posted to this account. Includes refunds posted as either payments or adjustments. |
| 22 | `TOT_INS_ADJ` | NUMERIC |  | The total amount of insurance adjustments posted to this account, not including refunds. |
| 23 | `TOT_SP_PMT` | NUMERIC |  | The total amount of self-pay payments posted to this account, not including refunds. |
| 24 | `TOT_AR_INS_PMT` | NUMERIC |  | The total amount of active AR insurance payments posted to this account, not including refunds. When a hospital account is in bad debt or external AR, any insurance payments made will not update this amount. |
| 25 | `TOT_AR_INS_RFND` | NUMERIC |  | The total amount of active AR insurance refunds posted to this account. Includes refunds posted as either payments or adjustments. |
| 26 | `TOT_AR_INS_ALLOWANCES` | NUMERIC |  | The total amount of active AR insurance allowance adjustments posted to this account. |
| 27 | `TOT_AR_SP_PMT` | NUMERIC |  | The total amount of active AR self-pay payments posted to this account, not including refunds. When a hospital account is in bad debt or external AR, any self-pay payments made will not update this amount. |
| 28 | `TOT_AR_SP_RFND` | NUMERIC |  | The total amount of active AR self-pay refunds posted to this account. Includes refunds posted as either payments or adjustments. |
| 29 | `TOT_AR_SP_ALLOWANCES` | NUMERIC |  | The total amount of active AR self-pay allowance adjustments posted to this account. |
| 30 | `HH_IS_REV_REC_YN_NAME` | VARCHAR |  | Indicates whether the hospital account was evaluated by Revenue Recognition based on the Revenue Recognition active dates and the admission date of the hospital account. |
| 31 | `ESTIMATE_ID` | NUMERIC | shared | Stores the estimate created directly from this account for advance billing. Estimates provided prior to service are only linked to encounters and are not stored here. |
| 32 | `QUALIFIED_CDI_REVIEW_YN` | VARCHAR |  | This item indicates whether the account qualified for clinical documentation improvement (CDI) review, regardless of whether a review actually occurred. |
| 33 | `TOT_INS_PMTS_AND_RFNDS` | NUMERIC |  | The total insurance payment amount posted to the account, less any refunded amount. |
| 34 | `TOT_SP_PMTS_AND_RFNDS` | NUMERIC |  | The total self-pay payment amount posted to the account, less any refunded amount. |
| 35 | `TOT_PMTS_AND_RFNDS` | NUMERIC |  | The total payment amount posted to the account, less any refunded amount. |
| 36 | `TOT_ADJ_EXCL_RFNDS` | NUMERIC |  | The total adjustment amount posted to the account, not including refund adjustments. |
| 37 | `ANCHOR_HSP_ACCOUNT_ID` | NUMERIC |  | For an encounter series of accounts, if the system automatically splits a cycle such that it has multiple accounts to span the cycle, one account is maintained to be the anchor for that cycle. The anchor account is intended to always exist for the cycle, so if the split is no longer needed, the other accounts in the cycle will be combined in to the anchor. |
| 38 | `ANCHOR_START_DATE` | DATETIME |  | When establishing an anchor account, this is the start date that encapsulates all the accounts in the anchor group. If it's just the anchor account, then it should be that account's start date. If there are multiple accounts anchored to the same account, then it's the earlier date of the group. |
| 39 | `ANCHOR_END_DATE` | DATETIME |  | When establishing an anchor account, this is the end date that encapsulates all the accounts in the anchor group. If it's just the anchor account, then it should be that account's end date. If there are multiple accounts anchored to the same account, then it's the latest date of the group. |
| 40 | `COCM_EPISODE_ID` | NUMERIC |  | This column stores the unique identifier for the coordinated care management service episode linked to the hospital account. |
| 41 | `MECH_VENT_HOURS` | NUMERIC |  | The number of hours used by the mechanical ventilator. |
| 42 | `SP_RESP_AFTER_INS` | NUMERIC |  | The balance transferred to self-pay after insurance is taken into account. This does not include any self-pay discount, financial assistance, or pre-payments. |
| 43 | `SP_RESP_LESS_DISCOUNT` | NUMERIC |  | The self-pay responsibility after any self-pay or financial assistance discounts are posted on the self-pay bucket. |
| 44 | `TOT_PRESERVICE_PMT` | NUMERIC |  | This column stores the total pre-service payments made by the guarantor for the hospital account. |
| 45 | `BAL_IN_FULL_SELF_PAY_YN` | VARCHAR |  | This column indicates whether the balances for this hospital account are entirely in self-pay. 'Y' indicates that all balances are in self-pay. 'N' or NULL indicates that there are some balances not in self-pay or the account has not been billed. |
| 46 | `FIRST_TX_POST_DATE` | DATETIME |  | This column is the original post date for the very first transaction that filed to this hospital account, even if that transaction has been reposted, transferred, or reversed. |
| 47 | `SELF_PAY_EXEMPT_RSN_C_NAME` | VARCHAR | org | The self-pay charge exemption reason category ID for why self-pay only charges on the hospital account should be billed to insurance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

## Joined in

Inbound joins are tracked on the logical base [HSP_ACCOUNT](HSP_ACCOUNT.md).

