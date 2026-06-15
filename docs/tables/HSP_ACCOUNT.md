# HSP_ACCOUNT

> This table contains hospital account information from the Hospital Account (HAR) and Claim (CLM) master files. It will exclude professional billing accounts in classic PB self-pay service areas.

**Overflow family:** [HSP_ACCOUNT_2](HSP_ACCOUNT_2.md), [HSP_ACCOUNT_3](HSP_ACCOUNT_3.md), [HSP_ACCOUNT_4](HSP_ACCOUNT_4.md), [HSP_ACCOUNT_5](HSP_ACCOUNT_5.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 137  
**Org-specific columns:** 17  
**Joined by:** 126 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the hospital account. |
| 2 | `HSP_ACCOUNT_NAME` | VARCHAR |  | The name of the patient associated with the hospital account. |
| 3 | `ACCT_CLASS_HA_C_NAME` | VARCHAR | org | The hospital account's account class. |
| 4 | `ACCT_FIN_CLASS_C_NAME` | VARCHAR | org | The hospital account's financial class. |
| 5 | `ACCT_SLFPYST_HA_C_NAME` | VARCHAR |  | The hospital account's self-pay status. |
| 6 | `ACCT_BILLSTS_HA_C_NAME` | VARCHAR |  | This column stores the status of the hospital account. If this is a professional billing default hospital account, this column always returns 4 (Billed). |
| 7 | `ACCT_ZERO_BAL_DT` | DATETIME |  | This column stores the date the hospital account went to a zero balance. This may be empty for older accounts, as Zero Balance Date (I HAR 244) had not always been available. |
| 8 | `ADM_DATE_TIME` | DATETIME (Local) |  | This column stores the admission date and time associated with the hospital account. The admission date and time (I HAR 400/405) are first pulled from the coding information on the hospital account. If that data is not stored on the hospital account yet, then this will use the primary encounter to determine the admission date and time. The exact items used varies based on the encounter type. |
| 9 | `ADM_DEPARMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `ADM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `ADM_PRIORITY` | VARCHAR |  | The admission priority stored in the hospital account. |
| 12 | `ADM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `ATTENDING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `AUTOPSY_DONE_YN` | VARCHAR |  | Denotes whether an autopsy was performed. |
| 15 | `BAD_DEBT_AGENCY_ID` | NUMERIC |  | This column stores the unique identifier for the collection agency that was selected when the hospital account was sent to bad debt, sent to external agency A/R, outsourced, or pre-collected. This is cleared when the account returns from bad debt, returns from external agency A/R, or is no longer outsourced. |
| 16 | `BAD_DEBT_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 17 | `BAD_DEBT_BUCKET_ID` | NUMERIC |  | This column stores the unique identifier for the bad debt bucket that was created when the hospital account was sent to bad debt. |
| 18 | `CODE_BLUE_YNU` | VARCHAR |  | Denotes whether the patient associated with the hospital account was code blue. |
| 19 | `COMBINE_ACCT_ID` | NUMERIC |  | This column stores the unique identifier for the target hospital account into which this hospital account was combined. |
| 20 | `COMBINE_DATE_TIME` | DATETIME (Local) |  | The date and time that this hospital account was combined with another one. |
| 21 | `COMBINE_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who combined this hospital account with another one. |
| 22 | `COMBINE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `COMPLETION_DT_TM` | DATETIME (Local) |  | The date and time when abstracting was completed for the hospital account. |
| 24 | `CVG_LIST_SELECT_YN` | VARCHAR |  | Denotes whether coverages have been put on the hospital account. |
| 25 | `DISCH_DATE_TIME` | DATETIME (Local) |  | This column stores the discharge date and time associated with the hospital account. The discharge date and time (I HAR 425/430) are first pulled from the coding information on the hospital account. If that data is not stored on the hospital account yet, then this will use the primary encounter to determine the discharge date and time. The exact items used varies based on the encounter type. |
| 26 | `DISCH_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 27 | `DISCH_DESTIN_HA_C_NAME` | VARCHAR | org | This column stores the discharge destination stored in the hospital account. This item is copied from the patient's ADT event record. |
| 28 | `DISCH_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 29 | `DISCH_TO` | VARCHAR |  | A discharge destination stored in the hospital account for coding and/or abstracting purposes. This is manually entered into the hospital account. |
| 30 | `DRG_EXPECTED_REIMB` | NUMERIC |  | This column stores the diagnosis-related group (DRG)-based expected reimbursement amount stored in the hospital account. |
| 31 | `ER_ADMIT_DATE_TIME` | DATETIME |  | The emergency room admission date and time stored in the hospital account. |
| 32 | `ER_DSCHG_DATE_TIME` | DATETIME |  | The emergency room discharge date and time stored in the hospital account. |
| 33 | `ER_PAT_STS_HA_C_NAME` | VARCHAR | org | The emergency room patient status stored in the hospital account. |
| 34 | `EXPIRATION_UNIT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 35 | `FINAL_DRG_ID` | VARCHAR |  | The final coded DRG stored in the hospital account. |
| 36 | `FINAL_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 37 | `FRST_DMND_STMT_DT` | DATETIME |  | The date that the first demand statement was sent for the hospital account. |
| 38 | `FRST_STMT_DATE` | DATETIME |  | The date that the first statement (non-demand) was sent for the hospital account. If you are sending informational or prorated statements this date will store the date the first informational, prorated, or full statement was sent. |
| 39 | `GUAR_ADDR_1` | VARCHAR |  | The first line of the street address of the guarantor for the hospital account at time of discharge. |
| 40 | `GUAR_ADDR_2` | VARCHAR |  | The second line of the street address of the guarantor for the hospital account at time of discharge. |
| 41 | `GUAR_NAME` | VARCHAR |  | The name of the guarantor for the hospital account at time of discharge. |
| 42 | `GUAR_WK_PHONE` | VARCHAR |  | The work phone number of the guarantor for the hospital account at time of discharge. |
| 43 | `GUAR_ZIP` | VARCHAR |  | The ZIP Code of the guarantor for the hospital account at time of discharge. |
| 44 | `IS_CALLED_911_YNU` | VARCHAR |  | Denotes whether 911 was called. |
| 45 | `IS_INSTI_YN` | VARCHAR |  | Denotes whether the hospital account is designated as an institutional account. A hospital account is considered institutional if its guarantor is of a type designated as institutional in the system definition profile. |
| 46 | `LAST_DMND_STMT_DT` | DATETIME |  | The last date that a demand statement was sent for the hospital account. |
| 47 | `LAST_INTRM_BILL_DT` | DATETIME |  | The last date that interim billing was performed for the hospital account. |
| 48 | `MEANS_OF_ARRV_C_NAME` | VARCHAR | org | The patient's means of arrival stored in the hospital account. |
| 49 | `NUM_OF_DET_BILLS` | INTEGER |  | The number of detail bills that have been sent for the hospital account. |
| 50 | `NUM_OF_DMND_STMTS` | INTEGER |  | The number of demand statements that have been sent for the hospital account. |
| 51 | `NUM_OF_STMTS_SENT` | INTEGER |  | The number of statements (non-demand) that have been sent for the hospital account. |
| 52 | `PAT_CITY` | VARCHAR |  | The city portion of the address of the patient for the hospital account at time of discharge. |
| 53 | `PAT_DOB` | DATETIME |  | The date of birth of the patient for the hospital account at time of discharge. |
| 54 | `PAT_HOME_PHONE` | VARCHAR |  | The home phone number of the patient for the hospital account at time of discharge. |
| 55 | `PAT_SSN` | VARCHAR |  | The social security number of the patient for the hospital account at time of discharge. |
| 56 | `PAT_WRK_PHN` | VARCHAR |  | The work phone number of the patient for the hospital account at time of discharge. |
| 57 | `PAT_ZIP` | VARCHAR |  | The ZIP Code of the patient for the hospital account at time of discharge. |
| 58 | `POLICE_INVOLVD_YNU` | VARCHAR |  | Denotes whether the police were involved in the circumstances of the patient's hospital stay. |
| 59 | `POST_ADM_EXP_HA_C_NAME` | VARCHAR | org | Denotes whether the patient expired after admission. |
| 60 | `POST_OP_EXP_HA_C_NAME` | VARCHAR |  | Denotes whether the patient expired after an operation. |
| 61 | `PREBILL_BUCKET_ID` | NUMERIC |  | This column stores the unique identifier for the hospital account's prebilled bucket. |
| 62 | `PRIM_SVC_HA_C_NAME` | VARCHAR | org | The primary service stored in the hospital account for the patient's hospital stay. |
| 63 | `PSYCH_CASE_YNU` | VARCHAR |  | Denotes whether the patient is classified as a psychiatric case. |
| 64 | `REHAB_INDICATOR` | VARCHAR |  | Denotes whether the patient was undergoing rehab. |
| 65 | `SCNDRY_SVC_HA_C_NAME` | VARCHAR |  | The secondary service stored in the hospital account for the patient's hospital stay. |
| 66 | `SELF_PAY_BUCKET_ID` | NUMERIC |  | This column stores the unique identifier for the hospital account's self-pay bucket. |
| 67 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 68 | `TOT_ADJ` | NUMERIC |  | The total of all adjustments on the hospital account. |
| 69 | `TOT_CHGS` | NUMERIC |  | The total of all charges on the hospital account. |
| 70 | `TRANSFER_FROM` | VARCHAR |  | Denotes where the patient was transferred from. |
| 71 | `TREATMENT_AUTH_NUM` | VARCHAR |  | Note: This column will be deprecated in a future release. Please start referring to the column HSP_ACCT_CLAIM_HAR.AUTHORIZATION_NUM in your reports. Authorization Number: Used on claims for identifying patient referrals and affected reimbursements. Refer to CLAIM_INFO2 table if not set on the hospital account. |
| 72 | `UB92_COINS_DAYS` | INTEGER |  | The number of coinsurance days that were listed on a UB92 claim for the hospital account. This is a user-entered value that overrides the value calculated by the system. Refer to AP_CLAIM table if not set on the hospital account. |
| 73 | `UB92_COVERED_DAYS` | INTEGER |  | The number of covered days that were listed on a UB92 claim for the hospital account. This is a user-entered value that overrides the value calculated by the system. Refer to AP_CLAIM table if not set on the hospital account. |
| 74 | `UB92_LIFETIME_DAYS` | INTEGER |  | The number of lifetime reserve days that were listed on a UB92 claim for the hospital account. Refer to AP_CLAIM table if not set on the hospital account. |
| 75 | `UB92_NONCOVRD_DAYS` | INTEGER |  | The number of noncovered days that were listed on a UB92 claim for the hospital account. This is a user-entered value that overrides the value calculated by the system. Refer to AP_CLAIM table if not set on the hospital account. |
| 76 | `UB92_TOB_OVERRIDE` | VARCHAR |  | Note: This column will be deprecated in a future release. Please start referring to the column HSP_ACCT_CLAIM_HAR.UB92_TOB_OVERRIDE in your reports. Type of Bill (TOB) override: TOB is a numeric code printed on claims that provide encounter information to a payer. Values entered here will override system settings that normally determine the Type of Bill. Refer to CLAIM_INFO2 table if not set on the hospital account. |
| 77 | `UNDISTRB_BUCKET_ID` | NUMERIC |  | This column stores the unique identifier for a hospital account's undistributed bucket. |
| 78 | `PATIENT_STATUS_C_NAME` | VARCHAR |  | The patient status (discharge disposition) category ID for the hospital account. |
| 79 | `ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The point of origin category ID (admission source) for the hospital account. |
| 80 | `ADMISSION_TYPE_C_NAME` | VARCHAR | org | The admission type category ID for the hospital account. |
| 81 | `PRIMARY_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 82 | `PRIMARY_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 83 | `NUM_OF_CHARGES` | INTEGER |  | The total number of charge transactions posted to the hospital account. This number may include inactive charges, such as reversals and reversed charges. |
| 84 | `SIGN_ON_FILE_C_NAME` | VARCHAR | org | The category ID indicating whether a hospital account signature is on file. This is an abstracting item. |
| 85 | `SIGN_ON_FILE_DATE` | DATETIME |  | The date the signature on file was entered for the hospital account. This is an abstracting item. |
| 86 | `PRIM_CONTACT_OVRD` | VARCHAR |  | The value for the primary contact override associated with the hospital account. |
| 87 | `CODING_STATUS_C_NAME` | VARCHAR | org | The coding status category ID for the hospital account. |
| 88 | `CODING_STS_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user when the coding status for the hospital account last changed. |
| 89 | `CODING_STS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 90 | `CODING_DATETIME` | DATETIME (Local) |  | The date and time that the coding status for the hospital account was last changed. |
| 91 | `ABSTRACT_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who last changed the abstracting status of the hospital account. |
| 92 | `ABSTRACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 93 | `OLD_RECUR_PRNT_ID` | NUMERIC |  | This column stores the unique identifier for the parent recurring account before combine. |
| 94 | `CASE_MIX_GRP_CODE` | VARCHAR |  | The case-mix group code associated with the hospital account. |
| 95 | `LAST_CMG_CODE` | VARCHAR |  | The CMG code from the last CPT merge. |
| 96 | `LAST_INT_CVG_ID` | NUMERIC |  | This column stores the unique identifier for the last interim coverage associated with the hospital account. |
| 97 | `BIRTH_WEIGHT` | NUMERIC |  | The birth weight of the newborn associated with the hospital account. This is an abstracting item. |
| 98 | `GESTATIONAL_AGE` | VARCHAR |  | On the mother's hospital account, the gestational age of the baby. This is an abstracting item. |
| 99 | `DISCHARGE_WEIGHT` | NUMERIC |  | The discharge weight of the newborn associated with the hospital account. This is an abstracting item. |
| 100 | `ORGAN_DONOR_YN` | VARCHAR |  | Indicates whether the patient associated with hospital account is an organ donor. This is an abstracting item. |
| 101 | `PREMATURE_BABY_YN` | VARCHAR |  | Indicates whether the baby associated with the hospital account is premature. This is an abstracting item. |
| 102 | `CODER_INITIALS` | VARCHAR |  | The initials of the user to last change the coding status on the hospital account. |
| 103 | `ADMIT_CATEGORY_C_NAME` | VARCHAR | org | This column stores the admission category ID for this hospital account. See column ADMIT_CATEGORY_C in table PAT_ENC_HSP if coding has not been performed on this hospital account. Alternatively, see V_ARHB_HSP_ACCOUNT_ADDL_INFO for the calculated value for this column based on both hospital account and encounter data. This view should be used to maintain backwards compatibility with reports created before upgrading to the Summer 2009 release. |
| 104 | `FIRST_BILLED_DATE` | DATETIME |  | This column stores the date when the account moved to the billed state for the first time. |
| 105 | `LAST_CODING_DATE` | DATETIME |  | The date of the last coding status change for the hospital account. This is an abstracting item. |
| 106 | `EXP_TOTAL_CHG_AMT` | NUMERIC |  | The expected total charge amount for the hospital account. |
| 107 | `EXP_TOTAL_CHG_CMT` | VARCHAR |  | The expected total charge user comment for the hospital account. |
| 108 | `EXP_PAT_LIAB_CMT` | VARCHAR |  | The expected patient liability user comment for the hospital account. |
| 109 | `BILL_DRG_IDTYPE_ID` | NUMERIC |  | This column stores the unique identifier for the billing DRG code set on the hospital account. |
| 110 | `BILL_DRG_IDTYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 111 | `BILL_DRG_MDC_VAL` | VARCHAR |  | The Major Diagnostic Category value for the billing DRG on the hospital account. |
| 112 | `BILL_DRG_WEIGHT` | VARCHAR |  | The weight for the billing DRG on the hospital account. |
| 113 | `BILL_DRG_PS_NAME` | VARCHAR |  | The severity of illness (SOI) category ID associated with the billing DRG on the hospital account. |
| 114 | `BILL_DRG_ROM_NAME` | VARCHAR |  | The risk of mortality category ID associated with the billing DRG on the hospital account. |
| 115 | `BILL_DRG_SHORT_LOS` | VARCHAR |  | The short length of stay for the billing DRG on the hospital account. |
| 116 | `BILL_DRG_LONG_LOS` | VARCHAR |  | The long length of stay for the billing DRG on the hospital account. |
| 117 | `BILL_DRG_AMLOS` | VARCHAR |  | The arithmetic mean length of stay for the billing DRG on the hospital account. |
| 118 | `BILL_DRG_GMLOS` | VARCHAR |  | The geometric mean length of stay for the billing DRG on the hospital account. |
| 119 | `BASE_INV_NUM` | VARCHAR |  | The base invoice number for this row. |
| 120 | `INV_NUM_SEQ_CTR` | INTEGER |  | The invoice number sequence counter for the hospital account. |
| 121 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 122 | `SPECIALTY_SVC_C_NAME` | VARCHAR | org | The specialty service category ID associated with the hospital account. This is an abstracting item. |
| 123 | `XFER_TO_NURSE_C_NAME` | VARCHAR | org | The category value of the transfer to nursing home item for the hospital account. This is an abstracting item. |
| 124 | `XFER_TO_ACUTE_C_NAME` | VARCHAR | org | The category value of the transfer to acute care facility item for the hospital account. This is an abstracting item. |
| 125 | `DEATH_TYPE_C_NAME` | VARCHAR | org | The type of death category ID for the hospital account. This is an abstracting item. |
| 126 | `APGAR_1_MIN` | INTEGER |  | The Apgar score at one minute for the newborn associated with the hospital account. This is an abstracting item. |
| 127 | `APGAR_5_MIN` | INTEGER |  | The Apgar score at five minutes for the newborn associated with the hospital account. This is an abstracting item. |
| 128 | `GRAVIDA` | INTEGER |  | The total number of pregnancies the patient on the hospital account has had, regardless of whether they were carried to term. This is an abstracting item. |
| 129 | `PARA` | INTEGER |  | The number of pregnancies that the patient on the hospital account has carried until the point where the fetus is viable. This is an abstracting item. |
| 130 | `BIRTH_CERT_SENT_YN` | VARCHAR |  | Indicates whether a birth certificate has been sent for this account. A null value for this column indicates that a birth certificate has not been sent. This is an abstracting item. |
| 131 | `FAILED_VBAC_YN` | VARCHAR |  | Indicates whether a vaginal birth after caesarian failed. This is an abstracting item. |
| 132 | `DELIVERY_DATE_TIME` | DATETIME (Local) |  | The date and time of the delivery associated with the hospital account. This is an abstracting item. |
| 133 | `PRENATAL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 134 | `DELIVER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 135 | `HOLD_STATUS_C_NAME` | VARCHAR | org | The coding hold status category ID for the hospital account. This is an abstracting item. |
| 136 | `GEST_AGE_BABY` | INTEGER |  | The gestational age of the baby associated with the hospital account. This is an abstracting item. |
| 137 | `ACCT_FOLLOWUP_DT` | DATETIME |  | This column stores the self-pay follow-up date associated with this hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (126)

| From | Column | Confidence |
|------|--------|------------|
| [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | `HSP_ACCOUNT_ID` | high |
| [BILL_SCHED_PMT_PP_HAR](BILL_SCHED_PMT_PP_HAR.md) | `HSP_ACCOUNT_ID` | high |
| [CLAIM_INFO_VISITS](CLAIM_INFO_VISITS.md) | `HSP_ACCOUNT_ID` | high |
| [CODE_INT_CODE_INFO_LN](CODE_INT_CODE_INFO_LN.md) | `HSP_ACCOUNT_ID` | high |
| [CODE_INT_CODE_INFO_QUAN](CODE_INT_CODE_INFO_QUAN.md) | `HSP_ACCOUNT_ID` | high |
| [CODE_INT_CODE_INT_QUAN](CODE_INT_CODE_INT_QUAN.md) | `HSP_ACCOUNT_ID` | high |
| [CODE_INT_COMB_LN](CODE_INT_COMB_LN.md) | `HSP_ACCOUNT_ID` | high |
| [CODING_COMMENTS](CODING_COMMENTS.md) | `HSP_ACCOUNT_ID` | high |
| [COD_CMTS](COD_CMTS.md) | `HSP_ACCOUNT_ID` | high |
| [COD_COMMENTS](COD_COMMENTS.md) | `HSP_ACCOUNT_ID` | high |
| [COD_RECORD_INFO](COD_RECORD_INFO.md) | `HSP_ACCOUNT_ID` | high |
| [FIN_ASST_INFO](FIN_ASST_INFO.md) | `HSP_ACCOUNT_ID` | high |
| [HBP_STMT_HAR_DETAIL](HBP_STMT_HAR_DETAIL.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ADJ_LIST](HSP_ACCT_ADJ_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ADMIT_DX](HSP_ACCT_ADMIT_DX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ALT_DRGS](HSP_ACCT_ALT_DRGS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_AR_AC_SUM](HSP_ACCT_AR_AC_SUM.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ATND_PROV](HSP_ACCT_ATND_PROV.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_BILL_DRG](HSP_ACCT_BILL_DRG.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_BILL_NOTE](HSP_ACCT_BILL_NOTE.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_BLD_REV](HSP_ACCT_BLD_REV.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CDSTS_HX](HSP_ACCT_CDSTS_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CHG_LIST](HSP_ACCT_CHG_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CLM_CPT](HSP_ACCT_CLM_CPT.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CL_AG_HIS](HSP_ACCT_CL_AG_HIS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CONS_SP_BAL](HSP_ACCT_CONS_SP_BAL.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CONS_SP_CHG](HSP_ACCT_CONS_SP_CHG.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CONS_SP_CVG](HSP_ACCT_CONS_SP_CVG.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CONS_SP_PMT_ADJ](HSP_ACCT_CONS_SP_PMT_ADJ.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CPT_CODES](HSP_ACCT_CPT_CODES.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CPT_PRVCM](HSP_ACCT_CPT_PRVCM.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CPT_PRVDR](HSP_ACCT_CPT_PRVDR.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CPT_PRVRO](HSP_ACCT_CPT_PRVRO.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_CVG_LIST](HSP_ACCT_CVG_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DETAIL_BILL_HX](HSP_ACCT_DETAIL_BILL_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DLY_CHGS](HSP_ACCT_DLY_CHGS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DNB_SB_HX](HSP_ACCT_DNB_SB_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DX_LIST](HSP_ACCT_DX_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DX_LIST_AU_HACS](HSP_ACCT_DX_LIST_AU_HACS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_DX_LIST_HACS](HSP_ACCT_DX_LIST_HACS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC](HSP_ACCT_EBC.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_2](HSP_ACCT_EBC_2.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_ABN_CND_NB](HSP_ACCT_EBC_ABN_CND_NB.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_ACTPR](HSP_ACCT_EBC_ACTPR.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_CHAR_LANDD](HSP_ACCT_EBC_CHAR_LANDD.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_CMPLD](HSP_ACCT_EBC_CMPLD.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_CNGAN](HSP_ACCT_EBC_CNGAN.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_DLVMD](HSP_ACCT_EBC_DLVMD.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_FATHER_RAC](HSP_ACCT_EBC_FATHER_RAC.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_INFECTION](HSP_ACCT_EBC_INFECTION.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_MADRS](HSP_ACCT_EBC_MADRS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_MAT_MORB](HSP_ACCT_EBC_MAT_MORB.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_MMLAD](HSP_ACCT_EBC_MMLAD.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_MOTHER_RAC](HSP_ACCT_EBC_MOTHER_RAC.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_OB_PX](HSP_ACCT_EBC_OB_PX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_ONSET_LBR](HSP_ACCT_EBC_ONSET_LBR.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_RSKFC](HSP_ACCT_EBC_RSKFC.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_VG_CNGAN](HSP_ACCT_EBC_VG_CNGAN.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_VG_OB_PX](HSP_ACCT_EBC_VG_OB_PX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EBC_VG_RSK](HSP_ACCT_EBC_VG_RSK.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ECDDX_ALT_HACS](HSP_ACCT_ECDDX_ALT_HACS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_ED_PROVIDERS](HSP_ACCT_ED_PROVIDERS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EVENTS](HSP_ACCT_EVENTS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EXTINJ_CD](HSP_ACCT_EXTINJ_CD.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_EXTINJ_CD_HACS](HSP_ACCT_EXTINJ_CD_HACS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_FINDX_ALT_HACS](HSP_ACCT_FINDX_ALT_HACS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_HX_PHYS](HSP_ACCT_HX_PHYS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_INS_BKTS](HSP_ACCT_INS_BKTS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_LETTERS](HSP_ACCT_LETTERS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_MPI](HSP_ACCT_MPI.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_MULT_DRGS](HSP_ACCT_MULT_DRGS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_NOTES](HSP_ACCT_NOTES.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_OPERATIVE](HSP_ACCT_OPERATIVE.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_OTHR_PROV](HSP_ACCT_OTHR_PROV.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PAT_CSN](HSP_ACCT_PAT_CSN.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PMT_PLAN_EST](HSP_ACCT_PMT_PLAN_EST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PRORATION](HSP_ACCT_PRORATION.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PX_LIST](HSP_ACCT_PX_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PX_PRVCMT](HSP_ACCT_PX_PRVCMT.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PX_PRVDRS](HSP_ACCT_PX_PRVDRS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PX_PRVROL](HSP_ACCT_PX_PRVROL.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_PYMT_LIST](HSP_ACCT_PYMT_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_RFND_TX](HSP_ACCT_RFND_TX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_RFV_LIST](HSP_ACCT_RFV_LIST.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_SBO](HSP_ACCT_SBO.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_SNF_PPS](HSP_ACCT_SNF_PPS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_STMT_HX](HSP_ACCT_STMT_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_ACCT_STOP_BILL](HSP_ACCT_STOP_BILL.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_ACT_HX](HSP_BKT_ACT_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_ACT_WO_TX](HSP_BKT_ACT_WO_TX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_ADDTL_REC](HSP_BKT_ADDTL_REC.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_ADJ_TXS](HSP_BKT_ADJ_TXS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_DSCNT_ADJ](HSP_BKT_DSCNT_ADJ.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_EOB_INFO](HSP_BKT_EOB_INFO.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_EXCL_DATES](HSP_BKT_EXCL_DATES.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_INV_NUM](HSP_BKT_INV_NUM.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_NAA_HX_HTR](HSP_BKT_NAA_HX_HTR.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_NAA_TX_TYP](HSP_BKT_NAA_TX_TYP.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_PAYMENT](HSP_BKT_PAYMENT.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_REC_HX](HSP_BKT_REC_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_SPLIT_CLMS](HSP_BKT_SPLIT_CLMS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_SPLIT_PMT](HSP_BKT_SPLIT_PMT.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_SRCHG_HX](HSP_BKT_SRCHG_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BKT_SURCHARGE](HSP_BKT_SURCHARGE.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_BUCKET](HSP_BUCKET.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_CLAIM_PRINT](HSP_CLAIM_PRINT.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_CLM_EDIT_ERROR](HSP_CLM_EDIT_ERROR.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_CLP_CLAIM_HX](HSP_CLP_CLAIM_HX.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_CLP_PMT_CLASS](HSP_CLP_PMT_CLASS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_CLP_REV_CODE](HSP_CLP_REV_CODE.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_HOME_LINK_VISITS](HSP_HOME_LINK_VISITS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_QI_ELIXHAUSER_COMORB](HSP_QI_ELIXHAUSER_COMORB.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_TX_DIAG](HSP_TX_DIAG.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_TX_LINE_INFO](HSP_TX_LINE_INFO.md) | `HSP_ACCOUNT_ID` | high |
| [HSP_TX_RFNDEXP](HSP_TX_RFNDEXP.md) | `HSP_ACCOUNT_ID` | high |
| [PAT_ENC](PAT_ENC.md) | `HSP_ACCOUNT_ID` | high |
| [PC_FEEDBACK](PC_FEEDBACK.md) | `HSP_ACCOUNT_ID` | high |
| [RECONCILE_CLM](RECONCILE_CLM.md) | `HSP_ACCOUNT_ID` | high |
| [STMT_EB_HOSP_ACCT_DETAIL](STMT_EB_HOSP_ACCT_DETAIL.md) | `HSP_ACCOUNT_ID` | high |
| [STMT_ETR_DETAIL](STMT_ETR_DETAIL.md) | `HSP_ACCOUNT_ID` | high |
| [STMT_HSP_ACCT_DETAIL](STMT_HSP_ACCT_DETAIL.md) | `HSP_ACCOUNT_ID` | high |
| [STMT_PMT_PLAN_EST_ACCTS](STMT_PMT_PLAN_EST_ACCTS.md) | `HSP_ACCOUNT_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_HAR](V_EHI_REG_ITEM_AUDIT_HAR.md) | `HSP_ACCOUNT_ID` | high |

