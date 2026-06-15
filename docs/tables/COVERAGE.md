# COVERAGE

> The COVERAGE table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow family:** [COVERAGE_2](COVERAGE_2.md), [COVERAGE_3](COVERAGE_3.md), [COVERAGE_4](COVERAGE_4.md), [COVERAGE_5](COVERAGE_5.md), [COVERAGE_6](COVERAGE_6.md)  
**Primary key:** `COVERAGE_ID`  
**Columns:** 65  
**Org-specific columns:** 8  
**Joined by:** 133 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `COVERAGE_TYPE_C_NAME` | VARCHAR |  | The category value that indicates whether a coverage is managed care or indemnity; 1 – Indemnity, 2 – Managed Care. |
| 3 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 5 | `PLAN_GRP_ID` | VARCHAR | FK→ | The ID of the employer group that determines the benefits in a managed care coverage. This item is NULL for indemnity coverages. |
| 6 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 7 | `COBRA_STATUS_YN` | VARCHAR |  | This yes/no flag is set to “Y” if the coverage has been extended beyond termination of the subscriber’s employment according to a COBRA arrangement. If the coverage has not been extended under such an arrangement, this value is “N” or null. |
| 8 | `COBRA_DATE` | DATETIME |  | The termination date for any COBRA arrangement. |
| 9 | `LATE_ENROLL_YN` | VARCHAR |  | Y if the subscriber applied for coverage outside of the open enrollment period. N or NULL if not specified as a late enrollment coverage. |
| 10 | `STUDENT_REVIEW_DT` | DATETIME |  | The date on which you should review the status of any members on this coverage who are students. |
| 11 | `EPIC_CVG_ID` | NUMERIC |  | The unique ID of the coverage record. This column may be hidden if you have elected to use enterprise reporting’s security utility. |
| 12 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique ID of premium billing account associated with the coverage. |
| 13 | `CVG_EFF_DT` | DATETIME |  | The effective date of the coverage. |
| 14 | `CVG_TERM_DT` | DATETIME |  | The termination date of the coverage. |
| 15 | `CASEHEAD_NUMBER` | VARCHAR |  | The Medicaid ID number on the case head. |
| 16 | `CASEHEAD_NAME` | VARCHAR |  | The Medicaid name on the case head. |
| 17 | `TNSFRD_COVERAGE_ID` | NUMERIC |  | The ID of the coverage from which this coverage is transferred from. |
| 18 | `CVG_REG_STATUS_C_NAME` | VARCHAR | org | The verification status of the coverage, such as verified, changed, elapsed, etc. |
| 19 | `VERIFY_USER_ID` | VARCHAR |  | The ID of the user who performed the verification. |
| 20 | `VERIFY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `GROUP_NAME` | VARCHAR |  | The name of the coverage group. |
| 22 | `CVG_ADDR1` | VARCHAR |  | The first line of the address of the coverage (administrative offices). |
| 23 | `CVG_ADDR2` | VARCHAR |  | The second line of the address of the coverage (administrative offices). |
| 24 | `CVG_CITY` | VARCHAR |  | The city of the mailing address of the coverage (administrative offices). |
| 25 | `CVG_ZIP` | VARCHAR |  | The zip code of the mailing address of the coverage (administrative offices). |
| 26 | `CVG_PHONE1` | VARCHAR |  | The primary phone number of the coverage (administrative offices). |
| 27 | `GROUP_NUM` | VARCHAR |  | The identification number assigned to this subscriber's employer/plan group by the payor. This number will appear in box 11 of the HCFA claim form. |
| 28 | `CLAIM_MAIL_CODE_C_NAME` | VARCHAR |  | The category value associated with where to send the claim on a coverage (i.e. send claim to payor, send claim to account, etc.) |
| 29 | `WC_EMPLOYER_ID` | VARCHAR |  | Workers' compensation employer at the time of injury. |
| 30 | `WC_EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 31 | `WC_DATE_OF_INJURY` | DATETIME |  | Workers Comp date of injury. This is the date the injury occurred on the job. This field is populated as the user sets up the WC account. |
| 32 | `IS_SIG_ON_FILE_YN` | VARCHAR |  | Appears in Box 12 of HCFA claims. This is a Yes/No field that denotes whether authorization has been obtained to send bill or other documentation to payor for services relating to the claim. |
| 33 | `ENROLL_REASON_C_NAME` | VARCHAR | org | This category value stores the enrollment reason of the coverage. |
| 34 | `CVG_TERM_REASON_C_NAME` | VARCHAR | org | This category value stores the termination reason of the coverage. |
| 35 | `PAT_REC_OF_SUBS_ID` | VARCHAR |  | If the subscriber is the same person as a patient, this item contains the patient ID. |
| 36 | `ECD_TABLE_DEF_COPAY` | NUMERIC |  | Numeric default copay value. |
| 37 | `COINSURANCE_OVR` | NUMERIC |  | Numeric Value for the coverage level coinsurance override. |
| 38 | `MEDC_COVERED_LEFT` | NUMERIC |  | This is the number of Medicare Covered Days Remaining |
| 39 | `MEDC_COINS_LEFT` | NUMERIC |  | This is the number of Medicare Coinsurance Days Remaining |
| 40 | `MEDC_RESERVE_LEFT` | NUMERIC |  | This is the number of Medicare Reserved Days Remaining |
| 41 | `CCS_PAT_ID` | VARCHAR | FK→ | The patient's Comprehensive Community Services (CCS) ID. |
| 42 | `CCS_DX` | VARCHAR |  | Stores the diagnosis that makes the patient eligible for Comprehensive Community Services (CCS) coverage. |
| 43 | `CCS_CC_NAME` | VARCHAR |  | Stores the name of the Comprehensive Community Services (CCS) Case Coordinator. |
| 44 | `CCS_COOR_PHONE` | VARCHAR |  | Stores the phone number for the Comprehensive Community Services (CCS) Case Coordinator. |
| 45 | `CCS_COUNTY_PHONE` | VARCHAR |  | Stores the phone number for the Comprehensive Community Services (CCS) County Office. |
| 46 | `CVG_COUNTY_C_NAME` | VARCHAR | org | The county of the mailing address of the coverage (administrative offices). |
| 47 | `CVG_COUNTRY_C_NAME` | VARCHAR | org | The country of the mailing address of the coverage (administrative offices). |
| 48 | `CVG_HOUSE_NUM` | VARCHAR |  | The house number of the mailing address of the coverage (administrative offices). |
| 49 | `CVG_DISTRICT_C_NAME` | VARCHAR | org | The district of the mailing address of the coverage (administrative offices). |
| 50 | `EFF_HOSP_CVG_DT` | DATETIME |  | The effective date of Medicare Part A. |
| 51 | `EFF_PROV_CVG_DT` | DATETIME |  | The effective date of Medicare Part B. |
| 52 | `MEDICARE_CVG_TYPE_C_NAME` | VARCHAR |  | The category number for the type of Medicare coverage the patient has. |
| 53 | `Q4CO_BUCKETS_EXC_YN` | VARCHAR |  | Flag to indicate if bucket limits exceeded during carryover |
| 54 | `MED_SEC_TYPE_C_NAME` | VARCHAR |  | Medicare Secondary Insurance Type Code. |
| 55 | `CHDP_COUNTY_C_NAME` | VARCHAR |  | The Child Health and Disability Prevention County Code. |
| 56 | `CHDP_AID_CODE` | VARCHAR |  | The Child Health and Disability Prevention Aid Code. |
| 57 | `CVG_CARD_ISSUE_DT` | DATETIME |  | Stores the card issue date. |
| 58 | `CVG_DEDUCTIBLE_YN` | VARCHAR |  | This item will serve as a flag to let the end user know if the response has any deductible information |
| 59 | `FIRST_SPEC_AID_CODE` | VARCHAR |  | First special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| 60 | `SEC_SPEC_AID_CODE` | VARCHAR |  | Second special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| 61 | `THRD_SPEC_AID_CODE` | VARCHAR |  | Third special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| 62 | `EVC_NUM` | VARCHAR |  | Eligibility Verification Confirmation (EVC) that is used on the Treatment Authorization Request (TAR) for Medi-Cal. |
| 63 | `COUNTY_CODE_C_NAME` | VARCHAR | org | This item will store the county code that is returned from the 271 message. |
| 64 | `EXT_ROUTING_NUM_C_NAME` | VARCHAR | org | The external routing number for the coverage |
| 65 | `SUBSCR_OR_SELF_MEM_PAT_ID` | VARCHAR | FK→ | This item contains the subscriber patient Id of a coverage and will be used to associate patients with linked premium billing accounts for EHI. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CCS_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |
| `SUBSCR_OR_SELF_MEM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (133)

| From | Column | Confidence |
|------|--------|------------|
| [ACCOUNT_DISCON_CVG](ACCOUNT_DISCON_CVG.md) | `COVERAGE_ID` | high |
| [ACCT_COVERAGE](ACCT_COVERAGE.md) | `COVERAGE_ID` | high |
| [APPEAL_GRV](APPEAL_GRV.md) | `COVERAGE_ID` | high |
| [AP_CLAIM](AP_CLAIM.md) | `COVERAGE_ID` | high |
| [AP_CLAIM_PROC](AP_CLAIM_PROC.md) | `CVG_ID` | high |
| [AP_CLM_RX](AP_CLM_RX.md) | `COVERAGE_ID` | high |
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `COVERAGE_ID` | high |
| [ARPB_VISITS](ARPB_VISITS.md) | `COVERAGE_ID` | high |
| [ATB_ROOT](ATB_ROOT.md) | `COVERAGE_ID` | high |
| [AUTHORIZATIONS](AUTHORIZATIONS.md) | `CVG_ID` | high |
| [AUTHORIZATION_COMMENT](AUTHORIZATION_COMMENT.md) | `COVERAGE_ID` | high |
| [AUTH_REQUEST](AUTH_REQUEST.md) | `COVERAGE_ID` | high |
| [AUT_ONC_EXP_REQCOUNT](AUT_ONC_EXP_REQCOUNT.md) | `COVERAGE_ID` | high |
| [BEN_ACCUMULATION](BEN_ACCUMULATION.md) | `COVERAGE_ID` | high |
| [BEN_ACCUMULATION_HX_ACCT](BEN_ACCUMULATION_HX_ACCT.md) | `COVERAGE_ID` | high |
| [BEN_ACCUMULATION_HX_PAT](BEN_ACCUMULATION_HX_PAT.md) | `COVERAGE_ID` | high |
| [BEN_ACCUMULATION_SYS_ADJ](BEN_ACCUMULATION_SYS_ADJ.md) | `COVERAGE_ID` | high |
| [BND_EPSD_INFO](BND_EPSD_INFO.md) | `COVERAGE_ID` | high |
| [BUNDLE_CHARGE_MAIN](BUNDLE_CHARGE_MAIN.md) | `CVG_ID` | high |
| [CAP_PAYMENT](CAP_PAYMENT.md) | `COVERAGE_ID` | high |
| [CAP_PAY_REPL](CAP_PAY_REPL.md) | `COVERAGE_ID` | high |
| [CASE_RATE_CVG](CASE_RATE_CVG.md) | `COVERAGE_ID` | high |
| [CLAIM_INFO](CLAIM_INFO.md) | `COVERAGE_ID` | high |
| [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | `COVERAGE_ID` | high |
| [COVERAGE_BENEFITS](COVERAGE_BENEFITS.md) | `CVG_ID` | high |
| [COVERAGE_COPAY_ECD](COVERAGE_COPAY_ECD.md) | `COVERAGE_ID` | high |
| [COVERAGE_LOC_PCP](COVERAGE_LOC_PCP.md) | `COVERAGE_ID` | high |
| [COVERAGE_M3P_BEN_TRACKING](COVERAGE_M3P_BEN_TRACKING.md) | `COVERAGE_ID` | high |
| [COVERAGE_M3P_EFF_PERIODS](COVERAGE_M3P_EFF_PERIODS.md) | `COVERAGE_ID` | high |
| [COVERAGE_M3P_ELECT_REQS](COVERAGE_M3P_ELECT_REQS.md) | `COVERAGE_ID` | high |
| [COVERAGE_MEMBER_LIST](COVERAGE_MEMBER_LIST.md) | `COVERAGE_ID` | high |
| [COVERAGE_MEMBER_RIDERS](COVERAGE_MEMBER_RIDERS.md) | `COVERAGE_ID` | high |
| [COVERAGE_MEM_ATTR](COVERAGE_MEM_ATTR.md) | `COVERAGE_ID` | high |
| [COVERAGE_MEM_RIDERS_HX](COVERAGE_MEM_RIDERS_HX.md) | `COVERAGE_ID` | high |
| [COVERAGE_MISC_COMMENTS](COVERAGE_MISC_COMMENTS.md) | `COVERAGE_ID` | high |
| [COVERAGE_NOTE_INFO](COVERAGE_NOTE_INFO.md) | `COVERAGE_ID` | high |
| [COVERAGE_SPONSOR](COVERAGE_SPONSOR.md) | `CVG_ID` | high |
| [COVERAGE_STATUS](COVERAGE_STATUS.md) | `COVERAGE_ID` | high |
| [COVERAGE_STATUS_HX](COVERAGE_STATUS_HX.md) | `COVERAGE_ID` | high |
| [COVERAGE_THRD_PARTY_PAYER](COVERAGE_THRD_PARTY_PAYER.md) | `COVERAGE_ID` | high |
| [COVERAGE_TYPE_INDEMNITY](COVERAGE_TYPE_INDEMNITY.md) | `COVERAGE_ID` | high |
| [CVG_ACCT_LIST](CVG_ACCT_LIST.md) | `CVG_ID` | high |
| [CVG_ADDR](CVG_ADDR.md) | `COVERAGE_ID` | high |
| [CVG_ADDR_HX](CVG_ADDR_HX.md) | `CVG_ID` | high |
| [CVG_ADDR_HX_DESC](CVG_ADDR_HX_DESC.md) | `CVG_ID` | high |
| [CVG_ADDR_HX_STREET](CVG_ADDR_HX_STREET.md) | `CVG_ID` | high |
| [CVG_ALT_ADDR](CVG_ALT_ADDR.md) | `CVG_ID` | high |
| [CVG_AP_CLAIMS](CVG_AP_CLAIMS.md) | `COVERAGE_ID` | high |
| [CVG_CCS_AUTH](CVG_CCS_AUTH.md) | `CVG_ID` | high |
| [CVG_COMMENTS](CVG_COMMENTS.md) | `CVG_ID` | high |
| [CVG_CUST_ATTR](CVG_CUST_ATTR.md) | `CVG_ID` | high |
| [CVG_ITEM_HX_VALUE_AFTER](CVG_ITEM_HX_VALUE_AFTER.md) | `COVERAGE_ID` | high |
| [CVG_ITEM_HX_VALUE_BEFORE](CVG_ITEM_HX_VALUE_BEFORE.md) | `COVERAGE_ID` | high |
| [CVG_MA_ERROR_HISTORY](CVG_MA_ERROR_HISTORY.md) | `COVERAGE_ID` | high |
| [CVG_MEMBER_STAT_OUTST_ACT](CVG_MEMBER_STAT_OUTST_ACT.md) | `COVERAGE_ID` | high |
| [CVG_MEM_CUSTODIAL_PT_ADDR](CVG_MEM_CUSTODIAL_PT_ADDR.md) | `COVERAGE_ID` | high |
| [CVG_MEM_MAIL_ADDR](CVG_MEM_MAIL_ADDR.md) | `COVERAGE_ID` | high |
| [CVG_MEM_RESP_ADDR](CVG_MEM_RESP_ADDR.md) | `COVERAGE_ID` | high |
| [CVG_MEM_RISK_ADJ_FACT](CVG_MEM_RISK_ADJ_FACT.md) | `CVG_ID` | high |
| [CVG_MEM_RISK_ADJ_FACT_HX](CVG_MEM_RISK_ADJ_FACT_HX.md) | `CVG_ID` | high |
| [CVG_MEM_STAT_OUTST_ACT_HX](CVG_MEM_STAT_OUTST_ACT_HX.md) | `COVERAGE_ID` | high |
| [CVG_PREMIUM_RATES](CVG_PREMIUM_RATES.md) | `CVG_ID` | high |
| [CVG_Q4_CARRYOVER](CVG_Q4_CARRYOVER.md) | `CVG_ID` | high |
| [CVG_REL_OF_INFO](CVG_REL_OF_INFO.md) | `COVERAGE_ID` | high |
| [CVG_RIDERS](CVG_RIDERS.md) | `CVG_ID` | high |
| [CVG_RIDERS_RATES](CVG_RIDERS_RATES.md) | `CVG_ID` | high |
| [CVG_RTE_QUERY](CVG_RTE_QUERY.md) | `CVG_ID` | high |
| [CVG_STREET_ADDR](CVG_STREET_ADDR.md) | `CVG_ID` | high |
| [CVG_SUBSCR_ADDR](CVG_SUBSCR_ADDR.md) | `CVG_ID` | high |
| [CVG_SUBSCR_EMPR_ADDR](CVG_SUBSCR_EMPR_ADDR.md) | `CVG_ID` | high |
| [DENTAL_PLAN_COVERAGES](DENTAL_PLAN_COVERAGES.md) | `COVERAGE_ID` | high |
| [DENTAL_TREAT_PLAN](DENTAL_TREAT_PLAN.md) | `COVERAGE_ID` | high |
| [DOCS_RCVD](DOCS_RCVD.md) | `COVERAGE_ID` | high |
| [EXCHANGE_SOURCE](EXCHANGE_SOURCE.md) | `CVG_ID` | high |
| [FILING_ORDER_HX](FILING_ORDER_HX.md) | `CVG_ID` | high |
| [FIN_ASST_TRKR_COVERAGES](FIN_ASST_TRKR_COVERAGES.md) | `COVERAGE_ID` | high |
| [HIX_MEM_RATES](HIX_MEM_RATES.md) | `CVG_ID` | high |
| [HSPC_BENEFIT_PRDS](HSPC_BENEFIT_PRDS.md) | `CVG_ID` | high |
| [HSP_ACCT_CVG_LIST](HSP_ACCT_CVG_LIST.md) | `COVERAGE_ID` | high |
| [HSP_ACCT_PRORATION](HSP_ACCT_PRORATION.md) | `COVERAGE_ID` | high |
| [HSP_BKT_SPLIT_EOB_INFO](HSP_BKT_SPLIT_EOB_INFO.md) | `COVERAGE_ID` | high |
| [HSP_BUCKET](HSP_BUCKET.md) | `COVERAGE_ID` | high |
| [HSP_CLM_EDIT_ERROR](HSP_CLM_EDIT_ERROR.md) | `COVERAGE_ID` | high |
| [IB_MESSAGES_3](IB_MESSAGES_3.md) | `CVG_ID` | high |
| [IB_MESSAGES_5](IB_MESSAGES_5.md) | `COVERAGE_ID` | high |
| [INV_BASIC_INFO](INV_BASIC_INFO.md) | `CVG_ID` | high |
| [INV_CLM_ICN_LIST](INV_CLM_ICN_LIST.md) | `COVERAGE_ID` | high |
| [MA_PREMIUM_LIS](MA_PREMIUM_LIS.md) | `COVERAGE_ID` | high |
| [MA_PREMIUM_OVERRIDE](MA_PREMIUM_OVERRIDE.md) | `COVERAGE_ID` | high |
| [MCARE_PREMIUM_PMT_OPT](MCARE_PREMIUM_PMT_OPT.md) | `COVERAGE_ID` | high |
| [MC_CVG_ELIG_VERIFICATION](MC_CVG_ELIG_VERIFICATION.md) | `COVERAGE_ID` | high |
| [MC_NOTIFICATIONS](MC_NOTIFICATIONS.md) | `COVERAGE_ID` | high |
| [MEMBER_CUSTODIAL_COM_NUM](MEMBER_CUSTODIAL_COM_NUM.md) | `CVG_ID` | high |
| [MEMBER_CUSTODIAL_COM_TYPE](MEMBER_CUSTODIAL_COM_TYPE.md) | `CVG_ID` | high |
| [MEMBER_LANGUAGES](MEMBER_LANGUAGES.md) | `CVG_ID` | high |
| [MEMBER_LANGUAGE_FLUENCY](MEMBER_LANGUAGE_FLUENCY.md) | `CVG_ID` | high |
| [MEMBER_LANG_DESCRIPTION](MEMBER_LANG_DESCRIPTION.md) | `CVG_ID` | high |
| [MEMBER_RESP_PERSON](MEMBER_RESP_PERSON.md) | `CVG_ID` | high |
| [MYC_CONVO_ABT_COVERAGES](MYC_CONVO_ABT_COVERAGES.md) | `COVERAGE_ID` | high |
| [ORIGINAL_ENROLL_VALS](ORIGINAL_ENROLL_VALS.md) | `CVG_ID` | high |
| [PAT_ACCT_CVG](PAT_ACCT_CVG.md) | `COVERAGE_ID` | high |
| [PAT_CVG_FILE_ORDER](PAT_CVG_FILE_ORDER.md) | `COVERAGE_ID` | high |
| [PAT_CVG_ID](PAT_CVG_ID.md) | `CVG_ID` | high |
| [PAT_ENC](PAT_ENC.md) | `COVERAGE_ID` | high |
| [PAT_ENC_PAYOR_NOTF](PAT_ENC_PAYOR_NOTF.md) | `COVERAGE_ID` | high |
| [PB_DTL_TX](PB_DTL_TX.md) | `COVERAGE_ID` | high |
| [PMT_EOB_INFO_I](PMT_EOB_INFO_I.md) | `COVERAGE_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `COVERAGE_ID` | high |
| [PR_EST_COVERAGES](PR_EST_COVERAGES.md) | `COVERAGE_ID` | high |
| [PR_EST_INFO](PR_EST_INFO.md) | `COVERAGE_ID` | high |
| [REFERRAL](REFERRAL.md) | `COVERAGE_ID` | high |
| [REFERRAL_CVG](REFERRAL_CVG.md) | `CVG_ID` | high |
| [REIMB_CALC_HX](REIMB_CALC_HX.md) | `COVERAGE_ID` | high |
| [RESP_PERSON_COM_NUM](RESP_PERSON_COM_NUM.md) | `CVG_ID` | high |
| [RTE_DATA_MISMATCH](RTE_DATA_MISMATCH.md) | `COVERAGE_ID` | high |
| [RXA_CVG_TABLE](RXA_CVG_TABLE.md) | `CVG_ID` | high |
| [SCAN_IMAGE](SCAN_IMAGE.md) | `COVERAGE_ID` | high |
| [SLR_REVIEW](SLR_REVIEW.md) | `COVERAGE_ID` | high |
| [STMT_ETR_DETAIL](STMT_ETR_DETAIL.md) | `COVERAGE_ID` | high |
| [SUBSCRIBER_ADDR_MSG](SUBSCRIBER_ADDR_MSG.md) | `COVERAGE_ID` | high |
| [V_EHI_AUDIT_CVG](V_EHI_AUDIT_CVG.md) | `COVERAGE_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_1](V_EHI_AUDIT_CVG_MEM_1.md) | `COVERAGE_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_2](V_EHI_AUDIT_CVG_MEM_2.md) | `COVERAGE_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_3](V_EHI_AUDIT_CVG_MEM_3.md) | `COVERAGE_ID` | high |
| [V_EHI_AUDIT_CVG_SUBS](V_EHI_AUDIT_CVG_SUBS.md) | `COVERAGE_ID` | high |
| [V_EHI_COVERAGE_SUBS](V_EHI_COVERAGE_SUBS.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_BEN_ACCUM_AT](V_EHI_CVG_BEN_ACCUM_AT.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_BEN_ACCUM_SYS_ADJ_AT](V_EHI_CVG_BEN_ACCUM_SYS_ADJ_AT.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_COVERAGE_HIST_ALL](V_EHI_CVG_COVERAGE_HIST_ALL.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_COVERAGE_HIST_MEM](V_EHI_CVG_COVERAGE_HIST_MEM.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_COVERAGE_HIST_SUB](V_EHI_CVG_COVERAGE_HIST_SUB.md) | `COVERAGE_ID` | high |
| [V_EHI_CVG_VERIF_HX_FILTER_PAT](V_EHI_CVG_VERIF_HX_FILTER_PAT.md) | `CVG_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_CVG](V_EHI_REG_ITEM_AUDIT_CVG.md) | `COVERAGE_ID` | high |

