# ACCOUNT

> This table stores information about guarantor accounts (and should not be confused with hospital accounts). The guarantor is the entity ultimately responsible for payment of a balance. One guarantor can be used for many hospital accounts. Use this table to find current professional billing and hospital billing balances for a guarantor across all patients and encounters.

**Overflow family:** [ACCOUNT_2](ACCOUNT_2.md), [ACCOUNT_3](ACCOUNT_3.md)  
**Primary key:** `ACCOUNT_ID`  
**Columns:** 103  
**Org-specific columns:** 13  
**Joined by:** 47 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the guarantor record. This ID number may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `ACCOUNT_NAME` | VARCHAR |  | This column stores the name for the guarantor record. The name could be hidden if you have elected to use enterprise reporting’s security utility. |
| 3 | `CONTACT_PERSON` | VARCHAR |  | The name of the person to contact for questions regarding the guarantor. This item could be hidden. |
| 4 | `BIRTHDATE` | DATETIME |  | The guarantor's date of birth. |
| 5 | `SEX` | VARCHAR | org | The sex of the guarantor. This is extracted as the category abbreviation. |
| 6 | `IS_ACTIVE` | VARCHAR |  | This column indicates whether the guarantor was active at the time of the extract. |
| 7 | `CITY` | VARCHAR |  | The city in which the guarantor lives. |
| 8 | `STATE_C_NAME` | VARCHAR | org | The category value of the state in which the guarantor lives. |
| 9 | `ZIP` | VARCHAR |  | The ZIP Code area in which the guarantor lives. |
| 10 | `HOME_PHONE` | VARCHAR |  | The guarantor’s home phone number (may contain dashes). |
| 11 | `WORK_PHONE` | VARCHAR |  | The guarantor’s work phone number (may contain dashes). |
| 12 | `ACCOUNT_TYPE_C_NAME` | VARCHAR | org | Category value associated with the type of account, such as Personal/Family, Worker’s Comp, etc. |
| 13 | `REFERRING_PROV_ID` | VARCHAR | FK→ | This column stores the unique identifier for the referral source for this guarantor. |
| 14 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 15 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 16 | `FIN_CLASS_C_NAME` | VARCHAR | org | The category value of the primary financial class of the guarantor (i.e. commercial, Medicare, self-pay, etc.) |
| 17 | `TOTAL_BALANCE` | NUMERIC |  | The total professional billing outstanding balance on the account. This amount includes both balances with insurance and with the patients. |
| 18 | `INSURANCE_BALANCE` | NUMERIC |  | The amount of the professional billing insurance balance on the guarantor. |
| 19 | `PATIENT_BALANCE` | NUMERIC |  | The amount of the professional billing self-pay balance on the account. |
| 20 | `BILLING_CYCLE_C_NAME` | VARCHAR | org | The category value associated with the billing cycle to which the guarantor belongs. |
| 21 | `BILLING_STATUS_C_NAME` | VARCHAR |  | The category value for the billing status used for handling statements for this guarantor, such as Age and Hold Statements, Age and Send Statements, Don’t Age and Hold Statements, and so on. |
| 22 | `PMT_PLAN_AMOUNT` | NUMERIC |  | The dollar amount to be paid per period if a payment plan has been established for this account. |
| 23 | `PMT_PLAN_STRT_DATE` | DATETIME |  | This column stores the date when the payment plan becomes effective. This column will only be populated if the guarantor is on a payment plan. |
| 24 | `PMT_PLAN_DUE_DATE` | INTEGER |  | The day of the month when the payment plan amount is due if the account is on a payment plan. |
| 25 | `LAST_INS_PMT_DATE` | DATETIME |  | The date the most recent insurance payment was received for this account before the enterprise reporting extract. |
| 26 | `LAST_PAT_PMT_DATE` | DATETIME |  | The date the most recent patient payment was received for this account before the enterprise reporting extract. |
| 27 | `LAST_PAT_PMT_AMT` | NUMERIC |  | The amount of the most recent patient payment received for this account before the enterprise reporting extract. |
| 28 | `LAST_STMT_DATE` | DATETIME |  | The date the most recent patient statement was sent for the account. |
| 29 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 30 | `CONTRACT_EXP_DATE` | DATETIME |  | The date on which the contract attached to this guarantor expires. |
| 31 | `COLLECTOR_USER_ID` | VARCHAR |  | This column stores the unique identifier for the system user who is the collector assigned to this guarantor. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 32 | `COLLECTOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 33 | `EPIC_ACCT_ID` | NUMERIC |  | This column stores the unique identifier for the guarantor record. This field will be hidden in a public view of the ACCOUNT table. |
| 34 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 35 | `OCCUPATION` | VARCHAR |  | The occupation of the guarantor. |
| 36 | `UNDIST_PMT_YN` | VARCHAR |  | Indicates whether the account has any undistributed payments. Y indicates the account has some undistributed payments. A null value indicates the account has no undistributed payments. An N will not be populated for this column. |
| 37 | `CREDIT_BALANCE_YN` | VARCHAR |  | Indicates whether the guarantor has credit balance. Y indicates the guarantor has credit balance. A null value indicates the guarantor has no credit balance. An N will not be populated for this column. |
| 38 | `PP_AMOUNT_DUE` | NUMERIC |  | The Hospital Billing Payment Plan current amount due. |
| 39 | `PP_CUR_BALANCE` | NUMERIC |  | The Hospital Billing Payment Plan current balance. |
| 40 | `EB_LAST_ND_STMT_DT` | DATETIME |  | Last non-demand enterprise statement date. |
| 41 | `EB_LAST_D_STMT_DT` | DATETIME |  | Last demand enterprise statement date. |
| 42 | `HOM_CLARITY_FLG_YN` | VARCHAR |  | This column indicates whether the guarantor should be extracted. If the guarantor is homed it will be extracted, otherwise not: 1-extract, 0-do not extract. |
| 43 | `HB_BALANCE` | NUMERIC |  | This value is the Hospital Billing balance on the guarantor. |
| 44 | `HB_PREBILL_BALANCE` | NUMERIC |  | This value is the Hospital Billing prebilled balance on the account. |
| 45 | `HB_INSURANCE_BALAN` | NUMERIC |  | This value is the Hospital Billing insurance balance on the guarantor, but excludes hospital accounts in external AR or bad debt. |
| 46 | `HB_SELFPAY_BALANCE` | NUMERIC |  | This value is the Hospital Billing self-pay balance on the account, but excludes hospital accounts in external AR, bad debt or that have not yet been billed to self-pay. |
| 47 | `HB_BADDEBT_BALANCE` | NUMERIC |  | This value is the Hospital Billing bad debt balance on the guarantor. |
| 48 | `HB_UNDISTRIB_BAL` | NUMERIC |  | This value is the Hospital Billing undistributed balance on the account, but excludes hospital accounts in external AR or bad debt. |
| 49 | `HB_SP_AGING_DATE` | DATETIME |  | Oldest Self-pay aging date. |
| 50 | `HB_INS_AGING_DATE` | DATETIME |  | This column stores the hospital billing insurance aging date. |
| 51 | `HB_LAST_INS_PMT_DT` | DATETIME |  | This column stores the last hospital billing insurance payment date. |
| 52 | `HB_LAST_SP_PMT_DT` | DATETIME |  | This column stores the last hospital billing self-pay payment date. |
| 53 | `SBO_HSP_ACCOUNT_ID` | NUMERIC |  | This column stores the unique identifier for the default hospital account of the guarantor. The item is only used in single billing office mode. |
| 54 | `EB_LAST_INFO_ST_DT` | DATETIME |  | This column stores the date the last enterprise non-demand informational statement was generated. Informational statements are those with no self-pay balance for the guarantor. |
| 55 | `EB_LAST_D_INFO_DT` | DATETIME |  | This column stores the date the last enterprise demand informational statement was generated. Informational statements are those with no self-pay balance for the guarantor. |
| 56 | `GUAR_REHOMED_YN` | VARCHAR |  | Indicates whether a new guarantor was created as a result of running the rehoming report and performing the rehome account action. Y indicates a new guarantor was created as a result of running the rehoming report and performing the rehome account action. An N will not be populated for this column. This item will only be populated if the guarantor is rehomed. |
| 57 | `OLD_REHOMED_ID` | NUMERIC |  | Holds a pointer from the new guarantor to the old guarantor |
| 58 | `EMPR_ID_CMT` | VARCHAR |  | A free text comment that can be entered when the value that is considered to be "Other" is selected as the employer. This option is available only if your organization has chosen to link the account employer to the Employer (EEP) master file in the Facility Profile. |
| 59 | `PAT_REC_OF_GUAR_ID` | VARCHAR |  | If the guarantor is the same person as a patient, this item contains the patient ID. |
| 60 | `HOUSE_NUM` | VARCHAR |  | This column stores the house number for the guarantor's address. |
| 61 | `NXT_STM_DATE` | DATETIME |  | Specifies the next statement date on the client account |
| 62 | `CLNT_BILL_FRQNCY_C_NAME` | VARCHAR |  | Specifies the statement frequency for this guarantor. Available options are weekly, monthly, bi-weekly, or weekly and end-of-month. |
| 63 | `CLNT_BILL_DAY_C_NAME` | VARCHAR |  | Specifies the day of the week to generate the client bill on provided that CLNT_BILL_FRQNCY_C is set to weekly or biweekly. |
| 64 | `CLNT_BILL_DT_MNTH` | INTEGER |  | Specifies the day of the month to bill the client on provided that CLNT_BILL_FRQNCY_C is set to monthly. |
| 65 | `CLIENT_ACCOUNT_YN` | VARCHAR |  | Indicates whether or not this is a client guarantor. |
| 66 | `PMT_PLAN_DURATION` | INTEGER |  | The payment plan duration in months. |
| 67 | `PMT_PLAN_TOTAL_AMT` | NUMERIC |  | The payment plan total amount. |
| 68 | `PMT_PLAN_ON_TIME_YN` | VARCHAR |  | Whether payment plan is on time, "Y" for on time, "N" for not on time. |
| 69 | `PMT_PLAN_BAL_PD_YN` | VARCHAR |  | This column indicates whether the payment plan will be effective until the balance is paid off that is, the payment plan remains effective if new charges occur. This column will only be populated if there is a payment plan. |
| 70 | `PMT_PLAN_LNKSTMT_YN` | VARCHAR |  | Indicates whether the payment plan due day is linked to the statement day. Y indicates the payment plan due day is linked to the statement day. This column will only be populated if there is a payment plan. |
| 71 | `RQG_RELATIONSHIP_C_NAME` | VARCHAR | org | This column stores the unique identifier for the guarantor's relationship to the requisition grouper patient record. |
| 72 | `HB_BD_SELFPAY_BAL` | NUMERIC |  | Self-pay balance of accounts in bad debt that have been billed to self-pay. |
| 73 | `HB_BD_INSURANCE_BAL` | NUMERIC |  | This column stores the total of all insurance buckets for this guarantor's hospital accounts that are in bad debt when using account-based bad debt. |
| 74 | `HB_BD_UNDISTRIB_BAL` | NUMERIC |  | This column stores the total of all undistributed buckets for this guarantor's hospital accounts that are in bad debt when using account-based bad debt. |
| 75 | `COUNTY_C_NAME` | VARCHAR | org | The category number for the county of the guarantor's billing address. |
| 76 | `COUNTRY_C_NAME` | VARCHAR | org | The category number for the country of the guarantor's billing address. |
| 77 | `EMPY_STAT_C_NAME` | VARCHAR | org | The category number for the guarantor's employment status. |
| 78 | `GUAR_EMPR_CITY` | VARCHAR |  | The city of the guarantor's employer. |
| 79 | `GUAR_EMPR_STATE_C_NAME` | VARCHAR |  | The category number for the state of the guarantor's employer. |
| 80 | `GUAR_EMPR_ZIP` | VARCHAR |  | The ZIP code of the guarantor's employer. |
| 81 | `GUAR_EMP_CNTRY_C_NAME` | VARCHAR |  | The category number for the country of the guarantor's employer. |
| 82 | `INCOME_SOURCE_C_NAME` | VARCHAR | org | Income source. |
| 83 | `LANGUAGE_C_NAME` | VARCHAR | org | The category value for the preferred language of the guarantor. |
| 84 | `HB_LAST_STMT_DATE` | DATETIME |  | This column contains the date of the last statement sent to the guarantor. |
| 85 | `HB_NEXT_STMT_DATE` | DATETIME |  | This column contains the date of the next statement to be sent to the guarantor. |
| 86 | `HB_LAST_DEMAND_DATE` | DATETIME |  | This column contains the date of the last demand statement to be sent to the guarantor. |
| 87 | `HB_BILL_NOTE_EXP_DT` | DATETIME |  | This column contains the expiration date of the billing note on this guarantor. |
| 88 | `HB_PP_MONTHLY_DUE` | VARCHAR |  | This column contains the monthly payment due on a hospital account for a payment plan. |
| 89 | `HB_PP_CUR_HAR_DUE` | VARCHAR |  | Current amount due on a hospital account for a payment plan. |
| 90 | `HB_PP_INIT_HAR_BAL` | VARCHAR |  | The initial balance on the hospital account when the payment plan starts. |
| 91 | `GUAR_VERIF_STAT_C_NAME` | VARCHAR | org | The category number of the guarantor verification status. |
| 92 | `LAST_VERIF_DT` | DATETIME |  | This column contains the date of the last verification of the associated guarantor. |
| 93 | `NEXT_REVIEW_DT` | DATETIME |  | Next date this guarantor's verification should be reviewed. |
| 94 | `LAST_VERIF_USER_ID` | VARCHAR |  | This column stores the unique identifier of the last user to verify the guarantor. |
| 95 | `LAST_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 96 | `GUAR_EMP_HOUSE_NUM` | VARCHAR |  | The house number of the guarantor's employer. |
| 97 | `GUAR_EMPR_DISTR_C_NAME` | VARCHAR | org | The category number for the district of the guarantor's employer. |
| 98 | `GUAR_VERIF_ID` | NUMERIC |  | The verification record of the guarantor. |
| 99 | `CONF_NAM_OF_ASSC_PT` | VARCHAR |  | This item contains the confidential name of the associated patient, if it exists. This name is used to determine the confidential nature of the guarantor. |
| 100 | `EXT_BD_SP_BAL` | NUMERIC |  | This value is the Professional Billing external AR bad debt self-pay balance. |
| 101 | `EXT_BD_INS_BAL` | NUMERIC |  | This value is the Professional Billing external AR bad debt insurance balance. |
| 102 | `PB_EXT_SP_BAL` | NUMERIC |  | This value is the Professional Billing external AR self-pay balance for the account. |
| 103 | `PB_EXT_INS_BAL` | NUMERIC |  | This value is the Professional Billing external AR insurance balance for the account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRING_PROV_ID` | [REFERRAL_SOURCE](REFERRAL_SOURCE.md) | sole_pk | high |

## Joined in — referenced by (47)

| From | Column | Confidence |
|------|--------|------------|
| [ACCOUNT_CONTACT](ACCOUNT_CONTACT.md) | `ACCOUNT_ID` | high |
| [ACCOUNT_DISCON_CVG](ACCOUNT_DISCON_CVG.md) | `ACCOUNT_ID` | high |
| [ACCOUNT_FPL_INFO](ACCOUNT_FPL_INFO.md) | `ACCOUNT_ID` | high |
| [ACCOUNT_RQG_GROUPERS](ACCOUNT_RQG_GROUPERS.md) | `ACCOUNT_ID` | high |
| [ACCOUNT_STATUS](ACCOUNT_STATUS.md) | `ACCOUNT_ID` | high |
| [ACCT_ADDR](ACCT_ADDR.md) | `ACCOUNT_ID` | high |
| [ACCT_COLL_AGENCY_HX](ACCT_COLL_AGENCY_HX.md) | `ACCOUNT_ID` | high |
| [ACCT_COVERAGE](ACCT_COVERAGE.md) | `ACCOUNT_ID` | high |
| [ACCT_EB_STMT_HIST](ACCT_EB_STMT_HIST.md) | `ACCOUNT_ID` | high |
| [ACCT_GUAR_PAT_INFO](ACCT_GUAR_PAT_INFO.md) | `ACCOUNT_ID` | high |
| [ACCT_HOME_PHONE_HX](ACCT_HOME_PHONE_HX.md) | `ACCOUNT_ID` | high |
| [ACCT_TX](ACCT_TX.md) | `ACCOUNT_ID` | high |
| [ACCT_WORK_PHONE_HX](ACCT_WORK_PHONE_HX.md) | `ACCOUNT_ID` | high |
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `ACCOUNT_ID` | high |
| [ARPB_TX_ACTIONS](ARPB_TX_ACTIONS.md) | `ACCOUNT_ID` | high |
| [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | `ACCOUNT_ID` | high |
| [CASE_RATE](CASE_RATE.md) | `ACCOUNT_ID` | high |
| [CASE_RATE_ACCT](CASE_RATE_ACCT.md) | `ACCOUNT_ID` | high |
| [CLAIM_INFO](CLAIM_INFO.md) | `ACCOUNT_ID` | high |
| [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | `ACCOUNT_ID` | high |
| [DENTAL_TREAT_PLAN](DENTAL_TREAT_PLAN.md) | `ACCOUNT_ID` | high |
| [FIN_ASST_CASE](FIN_ASST_CASE.md) | `ACCOUNT_ID` | high |
| [GUAR_ACCT_STMT_HX](GUAR_ACCT_STMT_HX.md) | `ACCOUNT_ID` | high |
| [GUAR_ADDR_HX](GUAR_ADDR_HX.md) | `ACCOUNT_ID` | high |
| [GUAR_NOTIF_HX_REPL](GUAR_NOTIF_HX_REPL.md) | `ACCOUNT_ID` | high |
| [GUAR_PMT_SCORE_HB_HX](GUAR_PMT_SCORE_HB_HX.md) | `ACCOUNT_ID` | high |
| [GUAR_PMT_SCORE_HX](GUAR_PMT_SCORE_HX.md) | `ACCOUNT_ID` | high |
| [GUAR_PMT_SCORE_PB_HX](GUAR_PMT_SCORE_PB_HX.md) | `ACCOUNT_ID` | high |
| [GUAR_PMT_SCORE_REPL](GUAR_PMT_SCORE_REPL.md) | `ACCOUNT_ID` | high |
| [HSP_ACCT_LETTERS](HSP_ACCT_LETTERS.md) | `ACCOUNT_ID` | high |
| [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | `ACCOUNT_ID` | high |
| [INVOICE](INVOICE.md) | `ACCOUNT_ID` | high |
| [MYC_CONVO_ABT_ACCOUNTS](MYC_CONVO_ABT_ACCOUNTS.md) | `ACCOUNT_ID` | high |
| [NOTES_ACCT](NOTES_ACCT.md) | `ACCOUNT_ID` | high |
| [PAT_ACCT_CVG](PAT_ACCT_CVG.md) | `ACCOUNT_ID` | high |
| [PAT_ENC](PAT_ENC.md) | `ACCOUNT_ID` | high |
| [PB_ACCT_SAPBS](PB_ACCT_SAPBS.md) | `ACCOUNT_ID` | high |
| [PB_ACCT_TRK_IDS](PB_ACCT_TRK_IDS.md) | `ACCOUNT_ID` | high |
| [PB_PMT_PLAN_PMTS](PB_PMT_PLAN_PMTS.md) | `ACCOUNT_ID` | high |
| [PMT_EOB_INFO_I](PMT_EOB_INFO_I.md) | `ACCOUNT_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `ACCOUNT_ID` | high |
| [PRE_AR_SESSION](PRE_AR_SESSION.md) | `ACCOUNT_ID` | high |
| [PR_EST_INFO](PR_EST_INFO.md) | `ACCOUNT_ID` | high |
| [RQG_ACCOUNT](RQG_ACCOUNT.md) | `ACCOUNT_ID` | high |
| [SUSPENSE_ACCT](SUSPENSE_ACCT.md) | `ACCOUNT_ID` | high |
| [V_EHI_AUDIT_EAR](V_EHI_AUDIT_EAR.md) | `ACCOUNT_ID` | high |
| [V_EHI_AUDIT_HAR](V_EHI_AUDIT_HAR.md) | `ACCOUNT_ID` | high |

