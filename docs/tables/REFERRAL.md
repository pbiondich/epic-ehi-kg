# REFERRAL

> The REFERRAL table is the primary table for referral information stored in system.

**Overflow family:** [REFERRAL_2](REFERRAL_2.md), [REFERRAL_3](REFERRAL_3.md), [REFERRAL_4](REFERRAL_4.md), [REFERRAL_5](REFERRAL_5.md), [REFERRAL_6](REFERRAL_6.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 97  
**Org-specific columns:** 17  
**Joined by:** 171 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The unique ID of the referral in database. This is the primary key for the REFERRAL table. |
| 2 | `EXTERNAL_ID_NUM` | VARCHAR |  | The external identification number used on the referral. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient associated with the referral. |
| 4 | `PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ENTRY_DATE` | DATETIME |  | The date the referral was entered. |
| 6 | `RFL_STATUS_C_NAME` | VARCHAR | org | The category value representing the status of the referral (I.e. authorized, open, pending, etc.). |
| 7 | `REFERRING_PROV_ID` | VARCHAR | FK→ | The unique ID of the referral source (REF) record of the provider who made the referral. This column is frequently used to link to the REFERRAL_SOURCE table. The actual provider (SER) ID can be found in column REF_PROVIDER_ID of table REFERRAL_SOURCE. |
| 8 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 9 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 10 | `REFERRAL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `PROV_SPEC_C_NAME` | VARCHAR | org | The category value indicating the provider specialty being referred to. |
| 12 | `RFL_TYPE_C_NAME` | VARCHAR | org | The category value indicating the type of referral. |
| 13 | `RSN_FOR_RFL_C_NAME` | VARCHAR | org | The category value indicating the main (first) reason for the referral. Since multiple reasons can be listed, use table REFERRAL_REASONS to view all of them. |
| 14 | `RFL_CLASS_C_NAME` | VARCHAR |  | The category value indicating the class of the referral. |
| 15 | `AUTH_VIS_PERIOD` | INTEGER |  | The number of authorized visits in each visit period. |
| 16 | `AUTH_PERIOD_TYPE_C_NAME` | VARCHAR |  | The category value indicating the type of period for authorized visits - i.e. hour, day, week, month, year. |
| 17 | `AUTH_NUM_PERIODS` | INTEGER |  | The number of periods authorized for this referral. |
| 18 | `AUTH_NUM_OF_VISITS` | NUMERIC |  | The number of visits authorized for this referral. |
| 19 | `ADMISSION_DATE` | DATETIME |  | The admission date associated with the referral. |
| 20 | `DISCHARGE_DATE` | DATETIME |  | The discharge date associated with the referral. |
| 21 | `ESTIMATED_DAYS` | INTEGER |  | The authorized length of stay if the patient is being admitted. |
| 22 | `START_DATE` | DATETIME |  | The start date of the referral. |
| 23 | `EXP_DATE` | DATETIME |  | The expiration date of the referral. |
| 24 | `PEND_TO` | VARCHAR |  | The person or pool to whom an In Basket message should be sent about this referral. |
| 25 | `PEND_RSN_C_NAME` | VARCHAR | org | For pended referrals, the category value indicating the reason for pending. |
| 26 | `DENY_RSN_C_NAME` | VARCHAR | org | For denied referrals, the category value indicating the reason for denial. |
| 27 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 28 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID of the coverage associated with the referral. |
| 29 | `NUM_PROC` | NUMERIC |  | The number of procedures associated with the referral. |
| 30 | `SVC_DATE_REAL` | FLOAT |  | If available, this column is populated by the authorized start date (I RFL 85). If not, it is populated by the expiration date on the referral (I RFL 90). If neither of these are available, the column will be empty. The date in this column is based on days since December 31, 1840. |
| 31 | `CARRIER_ID` | VARCHAR | FK→ | The ID number of the carrier associated with the referral. |
| 32 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 33 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 34 | `PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 35 | `SERV_DATE` | DATETIME |  | This column is populated by the authorized start date (I RFL 85) if available. If not, it is populated by the expiration date on the referral (I RFL 90). If neither of these are available, the column will be empty. The date in this column is in MM/DD/YYYY format. |
| 36 | `RETRO_FLAG_YN` | VARCHAR |  | The category value used to mark a referral as being "Retro" entered. |
| 37 | `IBNR` | NUMERIC |  | The "Incurred but not reported" amount associated with this referral. |
| 38 | `AUTO_APPROVED_DATE` | DATETIME |  | The date on which the referral was approved automatically by the system. |
| 39 | `AUTH_RSN_C_NAME` | VARCHAR | org | The category value indicating the authorization reason associated with the referral. |
| 40 | `REFD_BY_LOC_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 41 | `REFD_TO_LOC_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 42 | `REFD_TO_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 43 | `REFD_TO_SPEC_C_NAME` | VARCHAR | org | The category value indicating the specialty the department was referred to. |
| 44 | `PRIORITY_C_NAME` | VARCHAR | org | The category value indicating the priority of the referral. |
| 45 | `TOTAL_PRICE` | NUMERIC |  | The total cost of the procedures authorized under the referral. |
| 46 | `TOTAL_PAYABLE` | NUMERIC |  | The portion of the total price for which your facility is responsible. |
| 47 | `PATIENT_AMOUNT` | NUMERIC |  | The total patient liability, under the parameters of the primary coverage used, for the procedures authorized under the referral. |
| 48 | `EXPECT_TO_PAY` | NUMERIC |  | The total amount you expect your facility will pay for the procedures authorized under the referral. This amount entered by you overrides the total payable amount for the purpose of calculating IBNR. |
| 49 | `IBNR_PAY_UNTIL_DT` | DATETIME |  | The date up to which your facility will pay claims for the procedures approved on this referral. |
| 50 | `CASE_RATE_YN` | VARCHAR |  | The category value indicating whether this referral involves services that are reimbursed at a specific case rate. |
| 51 | `PRIM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 52 | `ACUTE_AMOUNT` | NUMERIC |  | The amount of the confirmation if the confirmation is acute. |
| 53 | `CHRONIC_AMOUNT` | NUMERIC |  | The amount of the confirmation if the confirmation is chronic. |
| 54 | `PAT_AMOUNT` | NUMERIC |  | The amount of the confirmation if the confirmation is an acute medication that was suggested by the pharmacist or over-the-counter medication. |
| 55 | `RFL_LOB_ID` | VARCHAR |  | ID of the Line of Business (LOB) assigned to the referral. |
| 56 | `RFL_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 57 | `ACTUAL_NUM_VISITS` | NUMERIC |  | The actual number of completed visits for this referral. |
| 58 | `SCHED_NUM_VISITS` | NUMERIC |  | The number of visits scheduled for this referral. |
| 59 | `REQUEST_NUM_VISITS` | NUMERIC |  | The number of visits requested for this referral. |
| 60 | `GUIDELINE_DAYS` | NUMERIC |  | Guideline days for this referral. |
| 61 | `OVRD_ADMIT_DATE` | DATETIME |  | Override admit date for this referral. |
| 62 | `OVRD_DISCHARGE_DT` | DATETIME |  | Override discharge date for this referral. |
| 63 | `DISP_VAL_C_NAME` | VARCHAR |  | Whether the referral was accepted ("appointed") or refused ("denied") by the referred-to provider, department or facility. |
| 64 | `DISP_RSN_C_NAME` | VARCHAR | org | The reason that a referral's disposition has a status of "denied." |
| 65 | `DISP_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 66 | `REFD_BY_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 67 | `CLOSE_RSN_C_NAME` | VARCHAR | org | For closed referrals, the category value indicating the reason for closing. |
| 68 | `SCHED_STATUS_C_NAME` | VARCHAR | org | Scheduling status of the referral to keep track of internally schedulable referrals. For category list use ZC_SCHED_STATUS. |
| 69 | `SCHED_BY_DATE` | DATETIME |  | Indicates deadline to schedule a referral. |
| 70 | `PREAUTH_REQ_C_NAME` | VARCHAR |  | For referrals created from an order, indicates if a preauthorization number must be collected before scheduling. |
| 71 | `NOT_COLLCTD_RSN_C_NAME` | VARCHAR | org | Reason indicating why the preauth number will not be collected for this referral. |
| 72 | `PROCESSED_RSN_C_NAME` | VARCHAR | org | Reason indicating why the preauth number is marked as processed for this referral. |
| 73 | `PREAUTH_CHG_EMP_ID` | VARCHAR |  | The unique ID of the user who last changed the preauthorization data. |
| 74 | `PREAUTH_CHG_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 75 | `PREAUTH_CHNGD_DTTM` | DATETIME (Local) |  | Date/time stamp for last time the preauthorization data was changed. |
| 76 | `AUTH_NUM` | VARCHAR |  | Authorization number. |
| 77 | `PRE_CERT_NUM` | VARCHAR |  | Pre-certification number. |
| 78 | `NON_PREF_PROV_RSN_C_NAME` | VARCHAR | org | Stores the reason why a non preferred level provider was chosen. |
| 79 | `EXT_REF_DATE` | DATETIME |  | This is the external referring date. |
| 80 | `EOW_ID` | VARCHAR |  | The unique EOW ID associated with the referral. |
| 81 | `REQ_VIS_PER_PERIOD` | INTEGER |  | The requested visits per period on the referral. |
| 82 | `REQ_PERIOD_TYPE_C_NAME` | VARCHAR |  | The requested period type on the referral. |
| 83 | `REQ_NUM_OF_PERIODS` | INTEGER |  | The requested number of periods on the referral. |
| 84 | `REF_TO_PROV_ADDR_ID` | VARCHAR |  | This stores the address ID of the referred to provider. The format is as follows: ProvID-AddressID. AddressID is the line number of the multiple response address items in the SER masterfile. To use this column, join to CLARITY_SER_ADDR on REFERRAL.REF_TO_PROV_ADDR_ID = CLARITY_SER_ADDR.ADDR_UNIQUE_ID. If you use IntraConnect, also join on REFERRAL.REFERRAL_PROV_ID = CLARITY_SER_ADDR.PROV_ID. |
| 85 | `DECISION_DATE` | DATETIME |  | Date on which the referral's current status was assigned. |
| 86 | `NUM_CLMS_EXPECTED` | INTEGER |  | Number of claims expected to be filed on this referral. |
| 87 | `RFL_STATCHG_RSN_C_NAME` | VARCHAR | org | The reason category number describing why the referral status was changed. |
| 88 | `TOTAL_EST_DAYS` | NUMERIC |  | Total estimated days for the referral. |
| 89 | `TOTAL_OVERRIDE_DAYS` | NUMERIC |  | The total number of override days on the referral. |
| 90 | `TOTAL_CONVTD_DAYS` | NUMERIC |  | The total number of converted days on the referral. |
| 91 | `AMT_CLMS_ADJUDICTD` | NUMERIC |  | The amount of claims adjudicated. |
| 92 | `AMT_CLMS_PAID` | NUMERIC |  | The amount of claims paid. |
| 93 | `ADJ_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 94 | `ADJ_MEMBER_GROUP_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 95 | `ADJ_NET_STATUS_C_NAME` | VARCHAR | org | Adjudication network status. |
| 96 | `NO_CLAIMS_PAID` | NUMERIC |  | The number of claims paid on the claim. |
| 97 | `ADJUD_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRING_PROV_ID` | [REFERRAL_SOURCE](REFERRAL_SOURCE.md) | sole_pk | high |

## Joined in — referenced by (171)

| From | Column | Confidence |
|------|--------|------------|
| [ALT_PYR_SVC_TYP_C](ALT_PYR_SVC_TYP_C.md) | `REFERRAL_ID` | high |
| [APPEAL_INST_TXT](APPEAL_INST_TXT.md) | `REFERRAL_ID` | high |
| [AP_CLAIM_AUTH_ASGN_RFLS](AP_CLAIM_AUTH_ASGN_RFLS.md) | `REFERRAL_ID` | high |
| [AP_CLAIM_PX_RFLS_USED](AP_CLAIM_PX_RFLS_USED.md) | `REFERRAL_ID` | high |
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `REFERRAL_ID` | high |
| [ATB_ROOT](ATB_ROOT.md) | `REFERRAL_ID` | high |
| [AUTHCERT_DEFAULTED_ORDERS](AUTHCERT_DEFAULTED_ORDERS.md) | `REFERRAL_ID` | high |
| [AUTHORIZATIONS](AUTHORIZATIONS.md) | `REFERRAL_ID` | high |
| [AUTH_REQUEST](AUTH_REQUEST.md) | `REFERRAL_ID` | high |
| [AVOIDABLE_DAYS_CMT](AVOIDABLE_DAYS_CMT.md) | `REFERRAL_ID` | high |
| [CASE_RFL](CASE_RFL.md) | `REFERRAL_ID` | high |
| [CHART_REVIEW_BOOKMARKS](CHART_REVIEW_BOOKMARKS.md) | `REFERRAL_ID` | high |
| [CLAIM_REFERRAL_LK](CLAIM_REFERRAL_LK.md) | `REFERRAL_ID` | high |
| [CLAIM_REFERRAL_LK_HX](CLAIM_REFERRAL_LK_HX.md) | `REFERRAL_ID` | high |
| [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | `REFERRAL_ID` | high |
| [CUSTOM_DOCS](CUSTOM_DOCS.md) | `REFERRAL_ID` | high |
| [DME_RENTAL_REFERRALS](DME_RENTAL_REFERRALS.md) | `REFERRAL_ID` | high |
| [DOCS_RCVD_DETAILS](DOCS_RCVD_DETAILS.md) | `REFERRAL_ID` | high |
| [DX_MODS_TXT](DX_MODS_TXT.md) | `REFERRAL_ID` | high |
| [ENC_INFO_RFL_AUTH_REQUEST](ENC_INFO_RFL_AUTH_REQUEST.md) | `REFERRAL_ID` | high |
| [EPA_ATTACHMENT_NOTES](EPA_ATTACHMENT_NOTES.md) | `REFERRAL_ID` | high |
| [EPA_CODED_REFS](EPA_CODED_REFS.md) | `REFERRAL_ID` | high |
| [EPA_INFO](EPA_INFO.md) | `REFERRAL_ID` | high |
| [EPA_INFO_2](EPA_INFO_2.md) | `REFERRAL_ID` | high |
| [EPA_NUM_COMPS](EPA_NUM_COMPS.md) | `REFERRAL_ID` | high |
| [EPA_PAYER](EPA_PAYER.md) | `REFERRAL_ID` | high |
| [EPA_QUESTIONS](EPA_QUESTIONS.md) | `REFERRAL_ID` | high |
| [EPA_QUESTIONS_AUDIT_INST](EPA_QUESTIONS_AUDIT_INST.md) | `REFERRAL_ID` | high |
| [EPA_QUESTIONS_AUDIT_TYPE](EPA_QUESTIONS_AUDIT_TYPE.md) | `REFERRAL_ID` | high |
| [EPA_QUESTIONS_AUDIT_USER](EPA_QUESTIONS_AUDIT_USER.md) | `REFERRAL_ID` | high |
| [EPA_QUESTION_ANSWER](EPA_QUESTION_ANSWER.md) | `REFERRAL_ID` | high |
| [EPA_QUESTION_TEXT](EPA_QUESTION_TEXT.md) | `REFERRAL_ID` | high |
| [EPA_RENEWALS](EPA_RENEWALS.md) | `REFERRAL_ID` | high |
| [EPA_SELECT_CHOICES](EPA_SELECT_CHOICES.md) | `REFERRAL_ID` | high |
| [EPA_SELECT_QUEST_COMMENT](EPA_SELECT_QUEST_COMMENT.md) | `REFERRAL_ID` | high |
| [EPA_SELECT_QUEST_TEXT](EPA_SELECT_QUEST_TEXT.md) | `REFERRAL_ID` | high |
| [GEN_RFL_CAT_MR_10](GEN_RFL_CAT_MR_10.md) | `REFERRAL_ID` | high |
| [GEN_RFL_CAT_MR_6](GEN_RFL_CAT_MR_6.md) | `REFERRAL_ID` | high |
| [GEN_RFL_CAT_MR_7](GEN_RFL_CAT_MR_7.md) | `REFERRAL_ID` | high |
| [GEN_RFL_CAT_MR_8](GEN_RFL_CAT_MR_8.md) | `REFERRAL_ID` | high |
| [GEN_RFL_CAT_MR_9](GEN_RFL_CAT_MR_9.md) | `REFERRAL_ID` | high |
| [IB_MESSAGES](IB_MESSAGES.md) | `REFERRAL_ID` | high |
| [IP_WORKLIST_2](IP_WORKLIST_2.md) | `REFERRAL_ID` | high |
| [LCA_COMM_ATTACH](LCA_COMM_ATTACH.md) | `REFERRAL_ID` | high |
| [MEDICARE_DAYS](MEDICARE_DAYS.md) | `REFERRAL_ID` | high |
| [MED_AUTH_DETAILS](MED_AUTH_DETAILS.md) | `REFERRAL_ID` | high |
| [MED_AUTH_DET_NOTE](MED_AUTH_DET_NOTE.md) | `REFERRAL_ID` | high |
| [MED_PA_CLOSE_RSNS](MED_PA_CLOSE_RSNS.md) | `REFERRAL_ID` | high |
| [MED_PA_DETAILS](MED_PA_DETAILS.md) | `REFERRAL_ID` | high |
| [MED_PA_NOTE_FROM_PAYER](MED_PA_NOTE_FROM_PAYER.md) | `REFERRAL_ID` | high |
| [MED_PA_NOTE_TO_PAYER](MED_PA_NOTE_TO_PAYER.md) | `REFERRAL_ID` | high |
| [MED_PA_QUEST_SET_DESC](MED_PA_QUEST_SET_DESC.md) | `REFERRAL_ID` | high |
| [MED_PA_STATUS_NOTES](MED_PA_STATUS_NOTES.md) | `REFERRAL_ID` | high |
| [MYC_CONVO_ABT_REFERRALS](MYC_CONVO_ABT_REFERRALS.md) | `REFERRAL_ID` | high |
| [MYC_MESG](MYC_MESG.md) | `REFERRAL_ID` | high |
| [ORDERS_ONLY_CSN](ORDERS_ONLY_CSN.md) | `REFERRAL_ID` | high |
| [ORDER_PROC_2](ORDER_PROC_2.md) | `REFERRAL_ID` | high |
| [PAS_TRIAGE_DX_HX](PAS_TRIAGE_DX_HX.md) | `REFERRAL_ID` | high |
| [PAS_TRIAGE_HX](PAS_TRIAGE_HX.md) | `REFERRAL_ID` | high |
| [PAS_TRIAGE_PROC_HX](PAS_TRIAGE_PROC_HX.md) | `REFERRAL_ID` | high |
| [PAT_ENC](PAT_ENC.md) | `REFERRAL_ID` | high |
| [PRESC_PA_REORD_ACT](PRESC_PA_REORD_ACT.md) | `REFERRAL_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `REFERRAL_ID` | high |
| [PRE_AR_SESSION](PRE_AR_SESSION.md) | `REFERRAL_ID` | high |
| [PR_EST_INFO_3](PR_EST_INFO_3.md) | `REFERRAL_ID` | high |
| [REFERRAL_ADDL_PROV](REFERRAL_ADDL_PROV.md) | `REFERRAL_ID` | high |
| [REFERRAL_APT](REFERRAL_APT.md) | `REFERRAL_ID` | high |
| [REFERRAL_ATTACHMENTS](REFERRAL_ATTACHMENTS.md) | `REFERRAL_ID` | high |
| [REFERRAL_BED_DAY](REFERRAL_BED_DAY.md) | `REFERRAL_ID` | high |
| [REFERRAL_BED_DAY_IGN_TAT](REFERRAL_BED_DAY_IGN_TAT.md) | `REFERRAL_ID` | high |
| [REFERRAL_BED_DAY_NOTES](REFERRAL_BED_DAY_NOTES.md) | `REFERRAL_ID` | high |
| [REFERRAL_BED_DAY_UNS_NOTE](REFERRAL_BED_DAY_UNS_NOTE.md) | `REFERRAL_ID` | high |
| [REFERRAL_CE_CODE](REFERRAL_CE_CODE.md) | `REFERRAL_ID` | high |
| [REFERRAL_CE_DX_TXT](REFERRAL_CE_DX_TXT.md) | `REFERRAL_ID` | high |
| [REFERRAL_CE_PX](REFERRAL_CE_PX.md) | `REFERRAL_ID` | high |
| [REFERRAL_CE_PX_TXT](REFERRAL_CE_PX_TXT.md) | `REFERRAL_ID` | high |
| [REFERRAL_CE_REASON](REFERRAL_CE_REASON.md) | `REFERRAL_ID` | high |
| [REFERRAL_CLINICAL_DOC](REFERRAL_CLINICAL_DOC.md) | `REFERRAL_ID` | high |
| [REFERRAL_CLIN_DOC_ACNS](REFERRAL_CLIN_DOC_ACNS.md) | `REFERRAL_ID` | high |
| [REFERRAL_CROSS_ORG](REFERRAL_CROSS_ORG.md) | `REFERRAL_ID` | high |
| [REFERRAL_CVG](REFERRAL_CVG.md) | `REFERRAL_ID` | high |
| [REFERRAL_CVG_AUTH](REFERRAL_CVG_AUTH.md) | `REFERRAL_ID` | high |
| [REFERRAL_CVG_BED](REFERRAL_CVG_BED.md) | `REFERRAL_ID` | high |
| [REFERRAL_DX](REFERRAL_DX.md) | `REFERRAL_ID` | high |
| [REFERRAL_DX_MODIFIERS](REFERRAL_DX_MODIFIERS.md) | `REFERRAL_ID` | high |
| [REFERRAL_DX_NOTES](REFERRAL_DX_NOTES.md) | `REFERRAL_ID` | high |
| [REFERRAL_EOB_CODES](REFERRAL_EOB_CODES.md) | `REFERRAL_ID` | high |
| [REFERRAL_FLAGS](REFERRAL_FLAGS.md) | `REFERRAL_ID` | high |
| [REFERRAL_HIST](REFERRAL_HIST.md) | `REFERRAL_ID` | high |
| [REFERRAL_MESSAGE](REFERRAL_MESSAGE.md) | `REFERRAL_ID` | high |
| [REFERRAL_NOTES](REFERRAL_NOTES.md) | `REFERRAL_ID` | high |
| [REFERRAL_NOTIF_HIS](REFERRAL_NOTIF_HIS.md) | `REFERRAL_ID` | high |
| [REFERRAL_NOTIF_HIS_NOTES](REFERRAL_NOTIF_HIS_NOTES.md) | `REFERRAL_ID` | high |
| [REFERRAL_ORG_FILTER_SA](REFERRAL_ORG_FILTER_SA.md) | `REFERRAL_ID` | high |
| [REFERRAL_PX](REFERRAL_PX.md) | `REFERRAL_ID` | high |
| [REFERRAL_PX_NOTES](REFERRAL_PX_NOTES.md) | `REFERRAL_ID` | high |
| [REFERRAL_REASONS](REFERRAL_REASONS.md) | `REFERRAL_ID` | high |
| [REFERRAL_UM_CLIN_REVIEWER](REFERRAL_UM_CLIN_REVIEWER.md) | `REFERRAL_ID` | high |
| [REFERRAL_UM_UNSIGNED_NOTE](REFERRAL_UM_UNSIGNED_NOTE.md) | `REFERRAL_ID` | high |
| [RFL_ADD_PAYORS](RFL_ADD_PAYORS.md) | `REFERRAL_ID` | high |
| [RFL_ADJ_STRINGS](RFL_ADJ_STRINGS.md) | `REFERRAL_ID` | high |
| [RFL_APPLY_TEMPLT_HX](RFL_APPLY_TEMPLT_HX.md) | `REFERRAL_ID` | high |
| [RFL_APPT_REQUEST](RFL_APPT_REQUEST.md) | `REFERRAL_ID` | high |
| [RFL_APY_RTP_HX_TEMPLATE](RFL_APY_RTP_HX_TEMPLATE.md) | `REFERRAL_ID` | high |
| [RFL_CNT_TBL_CMTS](RFL_CNT_TBL_CMTS.md) | `REFERRAL_ID` | high |
| [RFL_CROSS_ORG_FAIL_REASON](RFL_CROSS_ORG_FAIL_REASON.md) | `REFERRAL_ID` | high |
| [RFL_CVG_AUTH_END](RFL_CVG_AUTH_END.md) | `REFERRAL_ID` | high |
| [RFL_CVG_AUTH_START](RFL_CVG_AUTH_START.md) | `REFERRAL_ID` | high |
| [RFL_CVG_BED_NUM](RFL_CVG_BED_NUM.md) | `REFERRAL_ID` | high |
| [RFL_CVG_BED_REFNUM](RFL_CVG_BED_REFNUM.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_APPEAL](RFL_CVG_DEN_APPEAL.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_APPEAL_DT](RFL_CVG_DEN_APPEAL_DT.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_DISPOS](RFL_CVG_DEN_DISPOS.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_END](RFL_CVG_DEN_END.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_NTF_DT](RFL_CVG_DEN_NTF_DT.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_REFNUM](RFL_CVG_DEN_REFNUM.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_RESLTN](RFL_CVG_DEN_RESLTN.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_RSN_C](RFL_CVG_DEN_RSN_C.md) | `REFERRAL_ID` | high |
| [RFL_CVG_DEN_START](RFL_CVG_DEN_START.md) | `REFERRAL_ID` | high |
| [RFL_CVG_PADS_END](RFL_CVG_PADS_END.md) | `REFERRAL_ID` | high |
| [RFL_CVG_PADS_PROV](RFL_CVG_PADS_PROV.md) | `REFERRAL_ID` | high |
| [RFL_CVG_PADS_REASN](RFL_CVG_PADS_REASN.md) | `REFERRAL_ID` | high |
| [RFL_CVG_PADS_START](RFL_CVG_PADS_START.md) | `REFERRAL_ID` | high |
| [RFL_CVG_TOD_ID](RFL_CVG_TOD_ID.md) | `REFERRAL_ID` | high |
| [RFL_DISC_SPEC_AUTH](RFL_DISC_SPEC_AUTH.md) | `REFERRAL_ID` | high |
| [RFL_DX_PRIM_MODS_TXT](RFL_DX_PRIM_MODS_TXT.md) | `REFERRAL_ID` | high |
| [RFL_DX_TXT](RFL_DX_TXT.md) | `REFERRAL_ID` | high |
| [RFL_ECONSULT_CSN](RFL_ECONSULT_CSN.md) | `REFERRAL_ID` | high |
| [RFL_MED_ORDERS](RFL_MED_ORDERS.md) | `REFERRAL_ID` | high |
| [RFL_NON_PREF_COMTS](RFL_NON_PREF_COMTS.md) | `REFERRAL_ID` | high |
| [RFL_NOTIF_STATUS](RFL_NOTIF_STATUS.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG](RFL_OUTSD_CVG.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_AUTH_NUM](RFL_OUTSD_CVG_AUTH_NUM.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_CMT](RFL_OUTSD_CVG_CMT.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_EFF_DT](RFL_OUTSD_CVG_EFF_DT.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_INS](RFL_OUTSD_CVG_INS.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_PAYER](RFL_OUTSD_CVG_PAYER.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_PLAN](RFL_OUTSD_CVG_PLAN.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_PRECERT_NUM](RFL_OUTSD_CVG_PRECERT_NUM.md) | `REFERRAL_ID` | high |
| [RFL_OUTSD_CVG_TERM_DT](RFL_OUTSD_CVG_TERM_DT.md) | `REFERRAL_ID` | high |
| [RFL_PAYER_NOTIF_ADMSN](RFL_PAYER_NOTIF_ADMSN.md) | `REFERRAL_ID` | high |
| [RFL_PRI_DX_MOD](RFL_PRI_DX_MOD.md) | `REFERRAL_ID` | high |
| [RFL_PROC_QUESTIONS](RFL_PROC_QUESTIONS.md) | `REFERRAL_ID` | high |
| [RFL_PROV_ID](RFL_PROV_ID.md) | `REFERRAL_ID` | high |
| [RFL_PROV_NAME](RFL_PROV_NAME.md) | `REFERRAL_ID` | high |
| [RFL_PX_PRICING](RFL_PX_PRICING.md) | `REFERRAL_ID` | high |
| [RFL_REF_TO_REGIONS](RFL_REF_TO_REGIONS.md) | `REFERRAL_ID` | high |
| [RFL_TRANSFER_OF_CARE_INFO](RFL_TRANSFER_OF_CARE_INFO.md) | `REFERRAL_ID` | high |
| [RFL_VOIDED_NOTES](RFL_VOIDED_NOTES.md) | `REFERRAL_ID` | high |
| [RXMA_QUEUE_REASON](RXMA_QUEUE_REASON.md) | `REFERRAL_ID` | high |
| [SAR_INFO](SAR_INFO.md) | `REFERRAL_ID` | high |
| [SAR_INFO_DX](SAR_INFO_DX.md) | `REFERRAL_ID` | high |
| [SAR_SVC_CODE](SAR_SVC_CODE.md) | `REFERRAL_ID` | high |
| [SAR_SVC_CODE_MOD](SAR_SVC_CODE_MOD.md) | `REFERRAL_ID` | high |
| [SAR_SVC_CODE_UNITS](SAR_SVC_CODE_UNITS.md) | `REFERRAL_ID` | high |
| [SAR_SVC_GRP](SAR_SVC_GRP.md) | `REFERRAL_ID` | high |
| [SAR_SVC_GRP_UNITS](SAR_SVC_GRP_UNITS.md) | `REFERRAL_ID` | high |
| [SAR_SVC_LN_INFO](SAR_SVC_LN_INFO.md) | `REFERRAL_ID` | high |
| [SAR_SVC_RNGE](SAR_SVC_RNGE.md) | `REFERRAL_ID` | high |
| [SAR_SVC_RNGE_UNITS](SAR_SVC_RNGE_UNITS.md) | `REFERRAL_ID` | high |
| [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | `REFERRAL_ID` | high |
| [TAR_INFO](TAR_INFO.md) | `REFERRAL_ID` | high |
| [TAR_SVC_LN_INFO](TAR_SVC_LN_INFO.md) | `REFERRAL_ID` | high |
| [TPL_INFO](TPL_INFO.md) | `REFERRAL_ID` | high |
| [TRIAGE_COMMENTS](TRIAGE_COMMENTS.md) | `REFERRAL_ID` | high |
| [TRIAGE_HX_DX_CODE_TYPE](TRIAGE_HX_DX_CODE_TYPE.md) | `REFERRAL_ID` | high |
| [TRIAGE_HX_DX_TXT](TRIAGE_HX_DX_TXT.md) | `REFERRAL_ID` | high |
| [TRIAGE_HX_RFL_DX_MOD](TRIAGE_HX_RFL_DX_MOD.md) | `REFERRAL_ID` | high |
| [TRIAGE_HX_RFL_MOD_TXT](TRIAGE_HX_RFL_MOD_TXT.md) | `REFERRAL_ID` | high |
| [TRI_HX_OTHR_USER](TRI_HX_OTHR_USER.md) | `REFERRAL_ID` | high |
| [V_EHI_AUDIT_RFL](V_EHI_AUDIT_RFL.md) | `REFERRAL_ID` | high |

