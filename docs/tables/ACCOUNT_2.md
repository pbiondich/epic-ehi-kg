# ACCOUNT_2

> Accounts contain information about billing for services, while coverages contain information about insurance payors, benefits, subscribers, and members. This table contains one row for each account record in your system. This table is the continuation of the ACCOUNT table.

**Overflow of:** [ACCOUNT](ACCOUNT.md)  
**Primary key:** `ACCT_ID`  
**Columns:** 74  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `FOL_UP_LEVEL_CUR` | INTEGER |  | Current follow up level. |
| 3 | `EMPL_ID_NUM` | VARCHAR |  | Employee ID number of the guarantor. |
| 4 | `BILLING_NOTE_EXP_DT` | DATETIME |  | Billing note expiration date. |
| 5 | `ALT_BILL_ADDR_YN` | VARCHAR |  | Indicates whether the Alternate Billing Address is used. "Y" indicates that the Alternate Billing Address is used. "N" indicates that the Alternate Billing Address is not used. |
| 6 | `ALT_BILL_CITY` | VARCHAR |  | This is the city on the Alternate Billing Address. |
| 7 | `ALT_BILL_STATE_C_NAME` | VARCHAR | org | The category value of the state on the Alternate Billing Address. |
| 8 | `ALT_BILL_ZIP` | VARCHAR |  | This is the zip code on the Alternate Billing Address. |
| 9 | `RQG_ACCT_YN` | VARCHAR |  | Indicates whether this is a requisition grouper account. |
| 10 | `GUAR_SYNC_OWNER_ID` | NUMERIC |  | When using guarantor account syncing, this item is the record pointer to the owning guarantor account, if one exists. |
| 11 | `EAR_ISOLATED_YN` | VARCHAR |  | This flag is set if the guarantor is considered "isolated" for patient data restrictions. Isolated guarantors are guarantors created from isolated patients. |
| 12 | `CVG_LAST_VERIF_DT` | DATETIME |  | Contains the date that the corresponding coverage was last verified. |
| 13 | `USER_CVG_LST_VER_ID` | VARCHAR |  | Contains the date that the corresponding coverage was last verified. |
| 14 | `USER_CVG_LST_VER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `EMPLOYMENT_DATE` | DATETIME |  | The date the guarantor was employed. |
| 16 | `EMPLOYER_FAX` | VARCHAR |  | The guarantor's employer's fax number. |
| 17 | `FAX` | VARCHAR |  | The fax number associated with this guarantor account. |
| 18 | `LAST_BILLED_AMT` | NUMERIC |  | Last statement's billed amount |
| 19 | `LAST_INS_BAL` | NUMERIC |  | Last statement's insurance amount |
| 20 | `LAST_CLAIM_DATE` | DATETIME |  | Last date the claim was produced |
| 21 | `BILL_STATUS_EXP_DT` | DATETIME |  | Billing status expiration date |
| 22 | `PMT_PLAN_FREQ_C_NAME` | VARCHAR |  | Payment plan frequency |
| 23 | `ACCT_VIP_STAT_YN` | VARCHAR |  | Indicates whether there is VIP status for this account. Y indicates the account has VIP status. N indicates the account does not have VIP status. |
| 24 | `HBMYC_LST_ST_V_DTTM` | DATETIME (UTC) |  | The date and time when a Hospital Billing statement was last viewed in MyChart by this guarantor. This field will be updated when either a guarantor-level or hospital account-level statement is viewed in MyChart for this guarantor. The date and time for this column is stored in Universal Coordinated Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 25 | `HBMYC_LST_DB_V_DTTM` | DATETIME (UTC) |  | The date and time when a Hospital Billing detail bill was last viewed in MyChart by this guarantor. The date and time for this column is stored in Universal Coordinated Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 26 | `HBMYC_LST_LT_V_DTTM` | DATETIME (UTC) |  | The date and time when a Hospital Billing letter was last viewed in MyChart by this guarantor. This field will be updated when either a guarantor-level or hospital account-level letter is viewed in MyChart for this guarantor. The date and time for this column is stored in Universal Coordinated Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 27 | `CREDIT_SCORE` | INTEGER |  | The guarantor's credit score. |
| 28 | `PROPENSITY_TO_PAY_C_NAME` | VARCHAR | org | Category describing the likelihood for this guarantor to pay. |
| 29 | `FOL_UP_LAST_LET_DT` | DATETIME |  | Date the last follow-up letter was sent. |
| 30 | `UNDIST_CREDIT_BAL` | NUMERIC |  | Total account undistributed credit balance |
| 31 | `UNDIST_INS_CR_BAL` | NUMERIC |  | Account undistributed credit balance - insurance credits only. |
| 32 | `UNDIST_SP_CR_BAL` | NUMERIC |  | Account undistributed credit balance - self-pay credits only. |
| 33 | `DELIVERY_POINT` | VARCHAR |  | The billing delivery point is a two digit extension to the nine digit US zip code, with values from 00 to 99. |
| 34 | `MILITARY_RANK_C_NAME` | VARCHAR | org | This column stores the military rank to which the patient's guarantor belongs. |
| 35 | `BRANCH_OF_SERVICE_C_NAME` | VARCHAR | org | This column stores the military branch of service to which the guarantor belongs. |
| 36 | `MIL_COMPONENT_C_NAME` | VARCHAR | org | This column stores the guarantor's military component, which is used to distinguish between guarantors who are on regular active duty and those who are members of one of the augmenting support groups. |
| 37 | `MIL_PAY_GRADE_C_NAME` | VARCHAR | org | This column stores the military pay grade to which the patient's guarantor belongs. |
| 38 | `DIST_LATER_COUNT` | INTEGER |  | Number of undistributed credits that are marked as for later distribution in this account. |
| 39 | `GUAR_EMPR_COUNTY_C_NAME` | VARCHAR | org | The category value corresponding to the county in which the guarantor's employer is located. |
| 40 | `ALT_BILL_COUNTY_C_NAME` | VARCHAR |  | The category number for the alternate county of the guarantor's billing address. |
| 41 | `ALT_BILL_COUNTRY_C_NAME` | VARCHAR | org | The category number for the alternate country of the guarantor's billing address. |
| 42 | `ALT_BILL_HOUSE_NUM` | VARCHAR |  | The alternate billing house number for the guarantor. |
| 43 | `ALT_BILL_DISTRICT_C_NAME` | VARCHAR | org | The category number for the alternate district of the guarantor's billing address. |
| 44 | `STMT_HOLD_DT` | DATETIME |  | The most recent date on which the account was held from the Professional Billing (PB) statement processing. |
| 45 | `STMT_HOLD_REASON_C_NAME` | VARCHAR | org | The reason why the account was held in Professional Billing statement processing. |
| 46 | `MYPT_ID` | VARCHAR | shared | The unique ID of the MyChart account that is linked to this guarantor record. This is used when the guarantor is not a patient in the system but needs to have access to the billing information in MyChart. |
| 47 | `GUAR_SUBDIV_CODE_C_NAME` | VARCHAR | org | Capture the guarantor's country subdivision code. |
| 48 | `MOBILE_PHONE` | VARCHAR |  | Mobile phone for guarantor accounts. |
| 49 | `FOL_UP_LAST_LEVEL` | INTEGER |  | This retains the value of the current follow up level (I EAR 3007) when a letter was last generated. |
| 50 | `PMT_PLAN_DLQ_AMT` | NUMERIC |  | This is the sum of delinquent payment plan payments. |
| 51 | `PMT_PLAN_DUE_AMT` | NUMERIC |  | This includes both the delinquent amount and the amount due for the current month. |
| 52 | `PMT_PLAN_PAID_AMT` | NUMERIC |  | This is the total amount of the payment plan payments. |
| 53 | `PMT_PLAN_REMAIN_AMT` | NUMERIC |  | This is the remaining amount of the payment plan. |
| 54 | `HB_EXT_AR_SELF_PAY_BAL` | NUMERIC |  | This item stores the Hospital Billing (HB) external Accounts Receivable (AR) self-pay balance for the account. |
| 55 | `HB_EXT_AR_INS_BAL` | NUMERIC |  | This item stores the Hospital Billing (HB) external Accounts Receivable (AR) insurance balance for the account. |
| 56 | `HB_EXT_AR_UNDIST_BAL` | NUMERIC |  | This item stores the Hospital Billing (HB) external Accounts Receivable (AR) undistributed balance for the account. |
| 57 | `HB_LAST_AUTOPAY_DATE` | DATETIME |  | The most recent Auto Pay date for guarantor set up with a payment plan on Auto Pay. |
| 58 | `EMAIL_ADDRESS` | VARCHAR |  | Email address documented on the guarantor. Any clarity report looking for the guarantor's email address must search in the following sequence, and use the first found one: - The primary email address from the associated patient of the guarantor. - The email address from the MyChart account associated with the guarantor. - The email address returned by this clarity column. |
| 59 | `ADDR_CHG_USER_ID` | VARCHAR |  | The user who initiated the linked address changes. |
| 60 | `ADDR_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 61 | `ADDR_CHG_INSTANT_DTTM` | DATETIME (Local) |  | The instant that the linked address change was initiated. |
| 62 | `ADDR_CHG_SOURCE` | VARCHAR |  | The source record that initiated the linked address changes. |
| 63 | `PREFERENCE_ID` | NUMERIC |  | The ID number of the communication preferences record for the guarantor. |
| 64 | `PMT_PLAN_CURRENT_MISS_CNT` | INTEGER |  | This item will store the number of payments that are currently late on the payment plan |
| 65 | `PMT_PLAN_TOTAL_MISS_CNT` | INTEGER |  | This item will store the total number of missed payments on the account's payment plan. |
| 66 | `PMT_PLAN_AUTOPAY_CARD_ID` | NUMERIC |  | Credit card associated with the payment plan. This credit card will be charged automatically when an installment is due for the payment plan. This column will be deprecated in the future release as the payment plan is being transitioned to use the scheduled payment framework. Once the transition is complete, reference the scheduled payment record for the current credit card. |
| 67 | `PB_PP_AUTOPAY_SCHED_PMT_ID` | NUMERIC |  | The scheduled payment record (BSP) associated with the guarantor's payment plan. Scheduled payment record is used to define the auto pay payment plan terms, including the payment method, day to trigger payment, and monthly amount. |
| 68 | `PMT_PLAN_CURR_AMT` | NUMERIC |  | If Guarantor is on autopayment plan using Scheduled Payment architecture, this item stores the monthly amount to be used for this payment plan cycle if the value is different than the updated payment plan monthly amount in payment plan amount. |
| 69 | `KI_GUAR_ACCT_VERIF_DATE` | DATETIME |  | This item indicates the most recent date the patient verified the self-guarantor billing information is correct in Welcome. |
| 70 | `KI_GUAR_ACCT_VERIF_STS_C_NAME` | VARCHAR |  | This item indicates the most recent patient-selected status of whether the self-guarantor billing information is correct in Welcome. |
| 71 | `LAST_PB_BAL_NOTIF_DATE` | DATETIME |  | The date on which the last balance notification was sent to the guarantor for their Professional Billing (PB) balances. |
| 72 | `LAST_HB_BAL_NOTIF_DATE` | DATETIME |  | The date on which the last balance notification was sent to the guarantor for their Hospital Billing (HB) / Single Billing Office (SBO) balances. |
| 73 | `PB_SELF_PAY_BAL_UPDATE_DATE` | DATETIME |  | This is updated based on changes to patient balance. |
| 74 | `HB_SELF_PAY_BAL_UPDATE_DATE` | DATETIME |  | This is updated based on changes to Hospital Billing (HB) self-pay balance (I EAR 20003). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ACCOUNT](ACCOUNT.md).

