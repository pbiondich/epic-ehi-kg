# PATIENT

> The PATIENT table contains one record for each patient in your system. The data contained in each record consists of demographics, PCP and primary location information, registration information, and other information.

**Overflow family:** [PATIENT_2](PATIENT_2.md), [PATIENT_3](PATIENT_3.md), [PATIENT_4](PATIENT_4.md), [PATIENT_5](PATIENT_5.md), [PATIENT_6](PATIENT_6.md)  
**Primary key:** `PAT_ID`  
**Columns:** 85  
**Org-specific columns:** 20  
**Joined by:** 659 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used by other tables to link to PATIENT. |
| 2 | `PAT_NAME` | VARCHAR |  | The patient’s name in the format Lastname, Firstname MI. |
| 3 | `CITY` | VARCHAR |  | The city in which the patient lives. |
| 4 | `STATE_C_NAME` | VARCHAR | org | The category value corresponding to the state in which the patient lives. |
| 5 | `COUNTY_C_NAME` | VARCHAR | org | The category value corresponding to the county in which the patient lives. |
| 6 | `COUNTRY_C_NAME` | VARCHAR | org | The category value corresponding to the country in which the patient lives. |
| 7 | `ZIP` | VARCHAR |  | The ZIP Code area in which the patient lives. |
| 8 | `HOME_PHONE` | VARCHAR |  | The patient’s home phone number. |
| 9 | `WORK_PHONE` | VARCHAR |  | The patient’s work phone number. |
| 10 | `EMAIL_ADDRESS` | VARCHAR |  | The patient’s e-mail address. |
| 11 | `BIRTH_DATE` | DATETIME (Local) |  | The date on which the patient was born. |
| 12 | `ETHNIC_GROUP_C_NAME` | VARCHAR | org | The category value associated with the patient’s ethnic background. |
| 13 | `RELIGION_C_NAME` | VARCHAR | org | The category value associated with the patient’s religion. |
| 14 | `LANGUAGE_C_NAME` | VARCHAR | org | The category value associated with the patient’s language. |
| 15 | `SSN` | VARCHAR |  | The patient’s Social Security Number. This number is formatted as 999-99-9999, and a single trailing alphabetic character is also allowed. |
| 16 | `REG_DATE` | DATETIME |  | The date on which the last patient verification occurred. If a patient was verified and then re-verified at a later date, this column will show the re-verified date. This column will be null for patients that have never been verified. |
| 17 | `REG_STATUS_C_NAME` | VARCHAR | org | The category value associated with the patient’s status in terms of the patient registration process as of the enterprise reporting extract. This is a customizable list, examples may include: 1 – New, 2 – Verified, and so on. |
| 18 | `MEDICARE_NUM` | VARCHAR |  | The patient’s Medicare-assigned identification number, if applicable. |
| 19 | `MEDICAID_NUM` | VARCHAR |  | Patient's Medicaid ID. |
| 20 | `ADV_DIRECTIVE_YN` | VARCHAR |  | This column contains the value “Y” if the patient has a signed living will on file with your facility indicating how they want their health chare to be handled in the event of an incapacitating emergency. This information is entered in clinical system. If the patient has no signed living will on file this column contains the value “N”. |
| 21 | `ADV_DIRECTIVE_DATE` | DATETIME |  | The date a living will was received from the patient. |
| 22 | `CUR_PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `CUR_PRIM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 24 | `LEGAL_STATUS_C_NAME` | VARCHAR | org | The medical and/or legal status associated with the patient’s death. This item is populated through Admission/Discharge/Transfer (ADT) workflows. |
| 25 | `BIRTH_STATUS_C_NAME` | VARCHAR | org | The category value associated with the newborn’s status at birth as entered in ADT. |
| 26 | `PED_MULT_BIRTH_ORD` | INTEGER |  | For multiple births, the place in the birth order of the current newborn patient. |
| 27 | `PED_MULT_BIRTH_TOT` | INTEGER |  | The total number of births during the mother’s labor and delivery of this newborn patient. |
| 28 | `CREATE_USER_ID` | VARCHAR |  | The unique ID of the system user who entered this patient’s record. This ID may be encrypted. |
| 29 | `CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `PAT_MRN_ID` | VARCHAR |  | The patient's medical record number (MRN), of the type associated with the patient's current primary location. |
| 31 | `DEATH_DATE` | DATETIME (Local) |  | The date of death for the patient. |
| 32 | `REC_CREATE_PAT_ID` | VARCHAR |  | The unique ID of the system user who created this patient’s record. This ID may be encrypted. NOTE: For historical reasons, the column name ends in PAT_ID and cannot be changed; despite its name, it does not link to patient ID. It instead links to CLARITY_EMP.USER_ID. |
| 33 | `REC_CREATE_PAT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 34 | `ORGAN_DONOR_YN` | VARCHAR |  | Indicates if the patient is an organ donor. |
| 35 | `TMP_CITY` | VARCHAR |  | Contains the city in which the patient is temporarily residing. |
| 36 | `TMP_STATE_C_NAME` | VARCHAR |  | Contains the state in which the patient is temporarily residing. |
| 37 | `TMP_COUNTRY_C_NAME` | VARCHAR |  | Contains the country in which the patient is temporarily residing. |
| 38 | `TMP_ZIP` | VARCHAR |  | Contains the ZIP Code in which the patient is temporarily residing. |
| 39 | `TMP_HOME_PHONE` | VARCHAR |  | Contains the temporary phone number where the patient can be reached. |
| 40 | `TMP_COUNTY_C_NAME` | VARCHAR |  | Contains the county in which the patient is temporarily residing. |
| 41 | `TMP_ADDR_START_DT` | DATETIME |  | Contains the starting effective date of the patients temporary address information. |
| 42 | `TMP_ADDR_END_DT` | DATETIME |  | Contains the ending effective date of the patients temporary address information. |
| 43 | `TMP_CARE_OF_PERSON` | VARCHAR |  | Contains the name of the contact person for the patient at the temporary residence. |
| 44 | `PAT_LAST_NAME` | VARCHAR |  | The last name of the patient. |
| 45 | `PAT_FIRST_NAME` | VARCHAR |  | The first name of the patient. |
| 46 | `PAT_MIDDLE_NAME` | VARCHAR |  | The middle name of the patient. |
| 47 | `PAT_TITLE_C_NAME` | VARCHAR | org | The patient's title, e.g. Mr., Mrs., Miss, Dr., etc. |
| 48 | `PAT_NAME_SUFFIX_C_NAME` | VARCHAR | org | The suffix to the patient's name, e.g. Jr., Sr., III, etc. |
| 49 | `SPECIAL_STATUS_C_NAME` | VARCHAR | org | The special status of the patient, such as employee or VIP. |
| 50 | `LANG_CARE_C_NAME` | VARCHAR |  | The patient's preferred language to receive care. |
| 51 | `LANG_WRIT_C_NAME` | VARCHAR |  | The patient's preferred language to receive written material. |
| 52 | `PROXY_PAT_YN` | VARCHAR | org | Indicates if the patient has a proxy already. |
| 53 | `PROXY_PACK_YN` | VARCHAR | org | Indicates if the proxy packet was given to the patient. |
| 54 | `EMPLOYER_ID` | VARCHAR | FK→ | This is the unique ID of the patient's employer if the item linking the patient to an employer (I EAF 6410) is set to 1. This is free text if the item linking the patient to an employer (I EAF 6410) is set to 2. |
| 55 | `EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 56 | `EMPY_STATUS_C_NAME` | VARCHAR | org | The employee's employment status (e.g. Full Time, Part time, Not Employed, etc.) |
| 57 | `GUARDIAN_NAME` | VARCHAR |  | The name of the patient's legal guardian, if any. |
| 58 | `PREF_CLIN_ZIP` | VARCHAR |  | The zip code of the patient's preferred clinic. |
| 59 | `PREF_PCP_SEX_C_NAME` | VARCHAR | org | The category value of the sex of the patient's preferred primary care physician. |
| 60 | `PREF_PCP_SPEC_C_NAME` | VARCHAR | org | The category value of the specialty of the patient's preferred physician. |
| 61 | `PREF_PCP_LANG_C_NAME` | VARCHAR |  | The category value of the language of the patient's preferred primary care physician. |
| 62 | `COUNTRY_OF_ORIG_C_NAME` | VARCHAR |  | Holds data on the country in which a patient was born |
| 63 | `PED_CESAREAN_YN` | VARCHAR |  | This column contains the value "Y" if the patient was delivered by Cesarean Section. If the patient was not delivered by Cesarean Section, this column contains the value "N". |
| 64 | `PED_NOUR_METH_C_NAME` | VARCHAR | org | Indicates the patient's pediatric nourishment method. |
| 65 | `PED_DELIVR_METH_C_NAME` | VARCHAR | org | Indicates the patient's delivery method at birth. |
| 66 | `PED_MULTI_BIRTH_YN` | VARCHAR |  | This column contains the value "Y" if the patient is one of a multiple birth. This column contains the value "N" if the patient was a single birth. |
| 67 | `EDD_DT` | DATETIME |  | The patient's Expected Date of Delivery. |
| 68 | `EDD_ENTERED_DT` | DATETIME |  | Date the Expected Date of Delivery was entered. |
| 69 | `EDD_CMT` | VARCHAR |  | Expected Date of Delivery comment. |
| 70 | `INTRPTR_NEEDED_YN` | VARCHAR |  | Indicates whether the patient needs an interpreter. |
| 71 | `PCP_DON_CHART_YN` | VARCHAR |  | Indicates whether the primary care physician has finished moving all the information from the paper chart into the system. |
| 72 | `PAT_HAS_IOL_YN` | VARCHAR |  | This item is used as a data item to mark those patients having intraocular lenses. |
| 73 | `PED_BIRTH_LABOR` | VARCHAR |  | Stores the duration of labor related to a patient's birth history. |
| 74 | `PED_HOSP_DAYS` | VARCHAR |  | Stores the number of days spent in the hospital related to a patient's birth history. |
| 75 | `PED_HOSP_NAME` | VARCHAR |  | Stores the name of the hospital where the patient was born as part of birth history. |
| 76 | `PED_HOSP_LOCATION` | VARCHAR |  | Stores the hospital location where the patient was born as part of birth history. |
| 77 | `MEDS_LAST_REV_TM` | DATETIME (Local) |  | Stores the last time the encounter medications list was reviewed. |
| 78 | `MEDS_LST_REV_USR_ID` | VARCHAR |  | Stores the last user to review the encounter medications list. |
| 79 | `MEDS_LST_REV_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 80 | `SELF_EC_VERIF_DATE` | DATETIME |  | Most recent date patient marked their emergency contact information as verified. |
| 81 | `SELF_EC_VERIF_ST_YN` | VARCHAR |  | The status of the patient's last verified emergency contact request (e.g. verified yes or no). |
| 82 | `EMPR_ID_CMT` | VARCHAR |  | A free text comment that can be entered when the value that is considered to be "Other" is selected as the employer. This option is available only if your organization has chosen to link the patient employer to the Employer (EEP) master file in the Facility Profile. |
| 83 | `PAT_STATUS_C_NAME` | VARCHAR | org | The category value of the patient status. Possible statuses include alive and deceased. Note that there are many patient creation workflows that do not populate this item so many alive patients could have blank statuses. If using this column to report on the Alive or Deceased status of a patient population use PATIENT_4.PAT_LIVING_STAT_C instead. |
| 84 | `MEDS_LAST_REV_CSN` | NUMERIC |  | Stores the contact serial number of the encounter in which the patient's current medications list was last reviewed. |
| 85 | `SEX_C_NAME` | VARCHAR |  | The category number corresponding to the patient's sex. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EMPLOYER_ID` | [CLARITY_EEP](CLARITY_EEP.md) | sole_pk | high |

## Joined in — referenced by (659)

| From | Column | Confidence |
|------|--------|------------|
| [ACCESSIBLE_DOCUMENTS_PREF](ACCESSIBLE_DOCUMENTS_PREF.md) | `PAT_ID` | medium |
| [ACCESSIBLE_SERVICES](ACCESSIBLE_SERVICES.md) | `PAT_ID` | medium |
| [ACCT_GUAR_PAT_INFO](ACCT_GUAR_PAT_INFO.md) | `PAT_ID` | medium |
| [ACCUM_GENERAL](ACCUM_GENERAL.md) | `ACCUM_PAT_ID` | low |
| [ACCUM_GRP_GENERAL](ACCUM_GRP_GENERAL.md) | `PAT_ID` | medium |
| [ADDR_HX](ADDR_HX.md) | `PAT_ID` | medium |
| [ADDR_HX_DESC](ADDR_HX_DESC.md) | `PAT_ID` | medium |
| [ADDR_HX_STREET](ADDR_HX_STREET.md) | `PAT_ID` | medium |
| [ADMISSION_COMMENTS](ADMISSION_COMMENTS.md) | `PAT_ID` | medium |
| [ADM_EXPECT_DATES](ADM_EXPECT_DATES.md) | `PAT_ID` | medium |
| [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | `PAT_ID` | medium |
| [ALERT](ALERT.md) | `PAT_ID` | medium |
| [ALLERGY_FLAG](ALLERGY_FLAG.md) | `PAT_ID` | medium |
| [ALLOWED_TLH_MODES_LIST](ALLOWED_TLH_MODES_LIST.md) | `PAT_ID` | medium |
| [ALT_ORD_PROV_ADDR](ALT_ORD_PROV_ADDR.md) | `PAT_ID` | medium |
| [ALT_ORD_PROV_CMTS](ALT_ORD_PROV_CMTS.md) | `PAT_ID` | medium |
| [ALT_ORD_PROV_MEDLC](ALT_ORD_PROV_MEDLC.md) | `PAT_ID` | medium |
| [ALT_ORD_PROV_SINGL](ALT_ORD_PROV_SINGL.md) | `PAT_ID` | medium |
| [ANTICOAG_AUDIT](ANTICOAG_AUDIT.md) | `PAT_ID` | medium |
| [ANTICOAG_ENC_PAUSE_DATES](ANTICOAG_ENC_PAUSE_DATES.md) | `PAT_ID` | medium |
| [ANTICOAG_SELF_REGULATING](ANTICOAG_SELF_REGULATING.md) | `PAT_ID` | medium |
| [ANTICOAG_TABS](ANTICOAG_TABS.md) | `PAT_ID` | medium |
| [APPEAL_GRV](APPEAL_GRV.md) | `PAT_ID` | medium |
| [APPT_DECL_DATES_AUDIT](APPT_DECL_DATES_AUDIT.md) | `PAT_ID` | medium |
| [APPT_LENGTH_OVERRIDE](APPT_LENGTH_OVERRIDE.md) | `PAT_ID` | medium |
| [AP_CLAIM_PROC_4](AP_CLAIM_PROC_4.md) | `PAT_ID` | medium |
| [ARRIVAL_EVENT_TASK_ITEM](ARRIVAL_EVENT_TASK_ITEM.md) | `PAT_ID` | medium |
| [ARRIVAL_EVENT_TASK_RULE](ARRIVAL_EVENT_TASK_RULE.md) | `PAT_ID` | medium |
| [ARR_EVENT_TASK_EXTENSION](ARR_EVENT_TASK_EXTENSION.md) | `PAT_ID` | medium |
| [ARR_EVENT_TASK_ITEM_NAME](ARR_EVENT_TASK_ITEM_NAME.md) | `PAT_ID` | medium |
| [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | `PAT_ID` | medium |
| [ATB_ROOT](ATB_ROOT.md) | `PAT_ID` | medium |
| [ATTRIBUTED_PROVIDER](ATTRIBUTED_PROVIDER.md) | `PAT_ID` | medium |
| [ATTR_PROV_FILE_PERIOD](ATTR_PROV_FILE_PERIOD.md) | `PAT_ID` | medium |
| [AUTHORIZATIONS](AUTHORIZATIONS.md) | `PAT_ID` | medium |
| [AUTH_REQUEST](AUTH_REQUEST.md) | `PAT_ID` | medium |
| [AUTO_WORKFLOW_DETAILS](AUTO_WORKFLOW_DETAILS.md) | `PAT_ID` | medium |
| [AUTO_WT_LST_OFFER_UTC](AUTO_WT_LST_OFFER_UTC.md) | `PAT_ID` | medium |
| [BAT_DB_MAIN](BAT_DB_MAIN.md) | `INTENDED_PAT_ID` | low |
| [BAT_REL_GRP](BAT_REL_GRP.md) | `PAT_ID` | medium |
| [BAT_REQ_IN_BATCH](BAT_REQ_IN_BATCH.md) | `REQ_PAT_ID` | low |
| [BEDSIDE_ENC_ACTIVATION](BEDSIDE_ENC_ACTIVATION.md) | `PAT_ID` | medium |
| [BEDSIDE_WHITEBOARD_DEPT](BEDSIDE_WHITEBOARD_DEPT.md) | `PAT_ID` | medium |
| [BENEFITS](BENEFITS.md) | `PAT_ID` | medium |
| [BEN_ACCUMULATION](BEN_ACCUMULATION.md) | `PAT_ID` | medium |
| [BEN_ACCUMULATION_HX_ACCT](BEN_ACCUMULATION_HX_ACCT.md) | `ACCT_BKT_PAT_ID` | low |
| [BEN_ACCUMULATION_HX_PAT](BEN_ACCUMULATION_HX_PAT.md) | `PAT_BKT_PAT_ID` | low |
| [BEN_ACCUMULATION_SYS_ADJ](BEN_ACCUMULATION_SYS_ADJ.md) | `PAT_ID` | medium |
| [BEREAVE_FOL_INFO](BEREAVE_FOL_INFO.md) | `PAT_ID` | medium |
| [BILLING_NUMS](BILLING_NUMS.md) | `PAT_ID` | medium |
| [BILL_MUNICIPALITY_HX](BILL_MUNICIPALITY_HX.md) | `PAT_ID` | medium |
| [BLOCKED_CLAIMS](BLOCKED_CLAIMS.md) | `PAT_ID` | medium |
| [BLOCKED_CLAIMS_LIST](BLOCKED_CLAIMS_LIST.md) | `PAT_ID` | medium |
| [BLOOD_REQTS_ADD_INFO_AUDT](BLOOD_REQTS_ADD_INFO_AUDT.md) | `PAT_ID` | medium |
| [BLOOD_REQTS_DEG_VALS_AUDT](BLOOD_REQTS_DEG_VALS_AUDT.md) | `PAT_ID` | medium |
| [BLOOD_REQTS_VALS_AUDIT](BLOOD_REQTS_VALS_AUDIT.md) | `PAT_ID` | medium |
| [BLOOD_SPECIAL_REQTS](BLOOD_SPECIAL_REQTS.md) | `PAT_ID` | medium |
| [BLOOD_SPECIAL_REQTS_AUDIT](BLOOD_SPECIAL_REQTS_AUDIT.md) | `PAT_ID` | medium |
| [BUNDLE_CHARGE_MAIN](BUNDLE_CHARGE_MAIN.md) | `PAT_ID` | medium |
| [CAL_COMM_VERIFICATION](CAL_COMM_VERIFICATION.md) | `VERIF_PAT_ID` | low |
| [CAP_DTL_TX](CAP_DTL_TX.md) | `AR_MEMBER_PAT_ID` | low |
| [CAP_DTL_TX](CAP_DTL_TX.md) | `AR_SUBSCRIBER_PAT_ID` | low |
| [CARE_COORDINATION](CARE_COORDINATION.md) | `PAT_ID` | medium |
| [CARE_TEAM_PROV_STATUS](CARE_TEAM_PROV_STATUS.md) | `CT_PAT_ID` | low |
| [CASE_MGMT](CASE_MGMT.md) | `PAT_ID` | medium |
| [CASE_RPT_ABSTNS](CASE_RPT_ABSTNS.md) | `PAT_ID` | medium |
| [CBO_REVIEW_HX_CRC_IDS](CBO_REVIEW_HX_CRC_IDS.md) | `PAT_ID` | medium |
| [CCS_RECENT_FOLLOWUP_REPL](CCS_RECENT_FOLLOWUP_REPL.md) | `PAT_ID` | medium |
| [CHAT_CONVERSATIONS](CHAT_CONVERSATIONS.md) | `PAT_ID` | medium |
| [CLAIMS_DERIVE_PAT_FLAGS](CLAIMS_DERIVE_PAT_FLAGS.md) | `PAT_ID` | medium |
| [CLAIM_REFERENCE_DATA](CLAIM_REFERENCE_DATA.md) | `PAT_ID` | medium |
| [CLARITY_ADT](CLARITY_ADT.md) | `PAT_ID` | medium |
| [CLARITY_HVR](CLARITY_HVR.md) | `PAT_ID` | medium |
| [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | `PAT_ID` | medium |
| [CL_LEARN_ASSESS_NS](CL_LEARN_ASSESS_NS.md) | `PAT_ID` | medium |
| [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | `PAT_ID` | medium |
| [CL_PLC](CL_PLC.md) | `PAT_ID` | medium |
| [CL_REMIT](CL_REMIT.md) | `PAT_ID` | medium |
| [CMS_SEP1_ABSTN](CMS_SEP1_ABSTN.md) | `PAT_ID` | medium |
| [COD_RECORD_INFO](COD_RECORD_INFO.md) | `RA_CDI_PAT_ID` | low |
| [COHORT_LEN_OF_STAY_BENCH](COHORT_LEN_OF_STAY_BENCH.md) | `PAT_ID` | medium |
| [COMMISSION_PAYMENT](COMMISSION_PAYMENT.md) | `COMMISSION_PAT_ID` | low |
| [COMMUNICATION_AIDS](COMMUNICATION_AIDS.md) | `PAT_ID` | medium |
| [COMMUNITY_RESOURCE](COMMUNITY_RESOURCE.md) | `PAT_ID` | medium |
| [COMMUNITY_RESRC_REVIEWED](COMMUNITY_RESRC_REVIEWED.md) | `PAT_ID` | medium |
| [COMMUNITY_RESRC_REVIEW_HX](COMMUNITY_RESRC_REVIEW_HX.md) | `PAT_ID` | medium |
| [COMM_ROUTING](COMM_ROUTING.md) | `PAT_ID` | medium |
| [COMM_TRACE_BEHAVIOR_HX](COMM_TRACE_BEHAVIOR_HX.md) | `ACTOR_PAT_ID` | low |
| [COMM_TRACE_EMAIL_RECPNTS](COMM_TRACE_EMAIL_RECPNTS.md) | `PAT_ID` | medium |
| [COMM_TRACE_INFO](COMM_TRACE_INFO.md) | `ABOUT_PAT_ID` | low |
| [COMM_TRACE_INFO](COMM_TRACE_INFO.md) | `RECV_PAT_ID` | low |
| [CONF_ADDR_COMMENTS](CONF_ADDR_COMMENTS.md) | `PAT_ID` | medium |
| [CONF_OTHER_COMM](CONF_OTHER_COMM.md) | `PAT_ID` | medium |
| [CONTRACEPTIVES_EXIT](CONTRACEPTIVES_EXIT.md) | `PAT_ID` | medium |
| [CONTRACEPTIVES_INTAKE](CONTRACEPTIVES_INTAKE.md) | `PAT_ID` | medium |
| [COVERAGE](COVERAGE.md) | `CCS_PAT_ID` | low |
| [COVERAGE](COVERAGE.md) | `SUBSCR_OR_SELF_MEM_PAT_ID` | low |
| [COVERAGE_MEMBER_LIST](COVERAGE_MEMBER_LIST.md) | `PAT_ID` | medium |
| [COVERAGE_MEMBER_RIDERS](COVERAGE_MEMBER_RIDERS.md) | `PAT_ID` | medium |
| [COVERAGE_MEM_ATTR](COVERAGE_MEM_ATTR.md) | `PAT_ID` | medium |
| [COVERAGE_MEM_RIDERS_HX](COVERAGE_MEM_RIDERS_HX.md) | `PAT_ID` | medium |
| [CPR_CHANGE_HX](CPR_CHANGE_HX.md) | `PAT_ID` | medium |
| [CVG_MEMBER_STAT_OUTST_ACT](CVG_MEMBER_STAT_OUTST_ACT.md) | `PAT_ID` | medium |
| [CVG_MEM_RISK_ADJ_FACT](CVG_MEM_RISK_ADJ_FACT.md) | `PAT_ID` | medium |
| [CVG_MEM_RISK_ADJ_FACT_HX](CVG_MEM_RISK_ADJ_FACT_HX.md) | `PAT_ID` | medium |
| [CVG_MEM_STAT_OUTST_ACT_HX](CVG_MEM_STAT_OUTST_ACT_HX.md) | `PAT_ID` | medium |
| [CVG_REL_OF_INFO](CVG_REL_OF_INFO.md) | `ROI_PAT_ID` | low |
| [CVG_RTE_QUERY](CVG_RTE_QUERY.md) | `PAT_ID` | medium |
| [CX_PAT_TRANSITION_TRACKER](CX_PAT_TRANSITION_TRACKER.md) | `PAT_ID` | medium |
| [DEFAULT_PAYOR_PLAN](DEFAULT_PAYOR_PLAN.md) | `PAT_ID` | medium |
| [DEMOG_AUTH_AUDIT](DEMOG_AUTH_AUDIT.md) | `PAT_ID` | medium |
| [DEMOG_AUTH_INFO](DEMOG_AUTH_INFO.md) | `PAT_ID` | medium |
| [DENTAL_CLASS_AUDIT](DENTAL_CLASS_AUDIT.md) | `PAT_ID` | medium |
| [DENTAL_PAT_PHASE](DENTAL_PAT_PHASE.md) | `PAT_ID` | medium |
| [DENTAL_VISIT_INFO](DENTAL_VISIT_INFO.md) | `PAT_ID` | medium |
| [DENT_ORTH_EXAM_NOTES](DENT_ORTH_EXAM_NOTES.md) | `PAT_ID` | medium |
| [DEVICE_TRACKING_DETAILS](DEVICE_TRACKING_DETAILS.md) | `PAT_ID` | medium |
| [DICOM_MANIFEST](DICOM_MANIFEST.md) | `PAT_ID` | medium |
| [DIFFERENCE_PERIOD](DIFFERENCE_PERIOD.md) | `PAT_ID` | medium |
| [DISCHARGE_DELAYS](DISCHARGE_DELAYS.md) | `PAT_ID` | medium |
| [DISCHARGE_DELAYS_HX](DISCHARGE_DELAYS_HX.md) | `PAT_ID` | medium |
| [DISCHARGE_MILESTONES_HX](DISCHARGE_MILESTONES_HX.md) | `PAT_ID` | medium |
| [DISCH_DISPOSITION_HX](DISCH_DISPOSITION_HX.md) | `PAT_ID` | medium |
| [DISCRETE_PAT_INSTRUCTIONS](DISCRETE_PAT_INSTRUCTIONS.md) | `PAT_ID` | medium |
| [DME_RENTAL_INFO](DME_RENTAL_INFO.md) | `PAT_ID` | medium |
| [DOCS_RCVD](DOCS_RCVD.md) | `PAT_ID` | medium |
| [DOCS_RCVD_OB_HX](DOCS_RCVD_OB_HX.md) | `BABY_LINK_PAT_ID` | low |
| [DOC_LINKED_PATS](DOC_LINKED_PATS.md) | `LINKED_PAT_ID` | low |
| [DP_COMM_ATTACHMENTS](DP_COMM_ATTACHMENTS.md) | `PAT_ID` | medium |
| [DP_COMM_IDENTIFIER_RM](DP_COMM_IDENTIFIER_RM.md) | `PAT_ID` | medium |
| [DP_COMM_MEMO_NOTE](DP_COMM_MEMO_NOTE.md) | `PAT_ID` | medium |
| [DP_FAC_COMMUNICATIONS](DP_FAC_COMMUNICATIONS.md) | `PAT_ID` | medium |
| [DP_FAC_REASON_COMMENT](DP_FAC_REASON_COMMENT.md) | `PAT_ID` | medium |
| [DP_SECONDARY_SVC_TO_COORD](DP_SECONDARY_SVC_TO_COORD.md) | `PAT_ID` | medium |
| [DP_SEC_SVC_TO_COORD_AUDIT](DP_SEC_SVC_TO_COORD_AUDIT.md) | `PAT_ID` | medium |
| [DP_SEL_CNCT_PT_PURPOSE](DP_SEL_CNCT_PT_PURPOSE.md) | `PAT_ID` | medium |
| [DP_SERVICE_COORD_PLAN](DP_SERVICE_COORD_PLAN.md) | `PAT_ID` | medium |
| [DP_SVC_COORD_NOTE](DP_SVC_COORD_NOTE.md) | `PAT_ID` | medium |
| [DP_SVC_COORD_PLAN_AUDIT](DP_SVC_COORD_PLAN_AUDIT.md) | `PAT_ID` | medium |
| [DP_SVC_TO_COORDINATE](DP_SVC_TO_COORDINATE.md) | `PAT_ID` | medium |
| [DP_SVC_TO_COORD_AUDIT](DP_SVC_TO_COORD_AUDIT.md) | `PAT_ID` | medium |
| [DUAL_ADMISSION_UPDATES](DUAL_ADMISSION_UPDATES.md) | `PAT_ID` | medium |
| [ECHKIN_PHASE_INFO](ECHKIN_PHASE_INFO.md) | `PAT_ID` | medium |
| [ECHKIN_SESSION_INFO](ECHKIN_SESSION_INFO.md) | `PAT_ID` | medium |
| [EDBDSIDE_PAT_ENC_WAITPRED](EDBDSIDE_PAT_ENC_WAITPRED.md) | `PAT_ID` | medium |
| [ED_IEV_PAT_INFO](ED_IEV_PAT_INFO.md) | `PAT_ID` | medium |
| [EMPR_ADDRESS](EMPR_ADDRESS.md) | `PAT_ID` | medium |
| [ENC_CLIENT_SERVICES](ENC_CLIENT_SERVICES.md) | `PAT_ID` | medium |
| [ENC_DX_ASSOC_AMBIENT_DX](ENC_DX_ASSOC_AMBIENT_DX.md) | `PAT_ID` | medium |
| [ENC_DX_ASSOC_DATA](ENC_DX_ASSOC_DATA.md) | `PAT_ID` | medium |
| [ENC_DX_ASSOC_NOTES](ENC_DX_ASSOC_NOTES.md) | `PAT_ID` | medium |
| [ENC_LETTERS](ENC_LETTERS.md) | `PAT_ID` | medium |
| [ENC_METRIC_ENGINE_CALC](ENC_METRIC_ENGINE_CALC.md) | `PAT_ID` | medium |
| [ENC_METRIC_ENGINE_RSLT](ENC_METRIC_ENGINE_RSLT.md) | `PAT_ID` | medium |
| [ENC_METRIC_ENGINE_SRC](ENC_METRIC_ENGINE_SRC.md) | `PAT_ID` | medium |
| [ENC_METRIC_ENGINE_VAR](ENC_METRIC_ENGINE_VAR.md) | `PAT_ID` | medium |
| [ENC_METRIC_ENGINE_VARVAL](ENC_METRIC_ENGINE_VARVAL.md) | `PAT_ID` | medium |
| [ENC_SPEC_NEEDS](ENC_SPEC_NEEDS.md) | `PAT_ID` | medium |
| [ENC_SPEC_NEEDS_CMT](ENC_SPEC_NEEDS_CMT.md) | `PAT_ID` | medium |
| [ENROLL_INFO](ENROLL_INFO.md) | `PAT_ID` | medium |
| [EOW_LINKED_PATS](EOW_LINKED_PATS.md) | `LINKED_PAT_ID` | low |
| [EPT_CARE_TEAMS](EPT_CARE_TEAMS.md) | `PAT_ID` | medium |
| [EPT_INSTANT_ORDER_POLICY](EPT_INSTANT_ORDER_POLICY.md) | `PAT_ID` | medium |
| [EPT_OR_PAT_SURG_PREORD_NC](EPT_OR_PAT_SURG_PREORD_NC.md) | `PAT_ID` | medium |
| [ESCALATION_DYN](ESCALATION_DYN.md) | `PAT_ID` | medium |
| [ETHNIC_BACKGROUND](ETHNIC_BACKGROUND.md) | `PAT_ID` | medium |
| [EVENT_NOTIF_HX](EVENT_NOTIF_HX.md) | `PAT_ID` | medium |
| [EVENT_NOT_HX_FAC](EVENT_NOT_HX_FAC.md) | `PAT_ID` | medium |
| [EVENT_NOT_HX_POOLS](EVENT_NOT_HX_POOLS.md) | `PAT_ID` | medium |
| [EVENT_NOT_HX_PROV](EVENT_NOT_HX_PROV.md) | `PAT_ID` | medium |
| [EXPECTED_DISCHARGE_HX](EXPECTED_DISCHARGE_HX.md) | `PAT_ID` | medium |
| [EXPECTED_LOS_HISTORY](EXPECTED_LOS_HISTORY.md) | `PAT_ID` | medium |
| [EXPECT_DISCH_DISP_HX](EXPECT_DISCH_DISP_HX.md) | `PAT_ID` | medium |
| [EXPOSURE_ABSTNS](EXPOSURE_ABSTNS.md) | `EXPOSER_PAT_ID` | low |
| [EXPOSURE_ABSTNS](EXPOSURE_ABSTNS.md) | `PAT_ID` | medium |
| [EXTERNAL_DEATH_REPORTS](EXTERNAL_DEATH_REPORTS.md) | `PAT_ID` | medium |
| [EXTERNAL_DEATH_REPORTS_HX](EXTERNAL_DEATH_REPORTS_HX.md) | `PAT_ID` | medium |
| [EXTERNAL_ELIG_INFO](EXTERNAL_ELIG_INFO.md) | `PAT_ID` | medium |
| [EXT_ACCT_TOKEN](EXT_ACCT_TOKEN.md) | `PAT_ID` | medium |
| [EXT_ACCT_TOKEN_ORD](EXT_ACCT_TOKEN_ORD.md) | `PAT_ID` | medium |
| [EXT_DATA_LAST_DONE](EXT_DATA_LAST_DONE.md) | `PAT_ID` | medium |
| [EXT_DATA_REQ_PAYER_API](EXT_DATA_REQ_PAYER_API.md) | `PAT_ID` | medium |
| [EXT_DEM_UPDATES](EXT_DEM_UPDATES.md) | `PAT_ID` | medium |
| [EXT_ELIG_STATUS](EXT_ELIG_STATUS.md) | `PAT_ID` | medium |
| [EXT_ELIG_STATUS_1](EXT_ELIG_STATUS_1.md) | `PAT_ID` | medium |
| [EXT_FORMULARY_ID](EXT_FORMULARY_ID.md) | `PAT_ID` | medium |
| [FAC_CHG_AI_RUN_INFO](FAC_CHG_AI_RUN_INFO.md) | `PAT_ID` | medium |
| [FAILED_ACCESS](FAILED_ACCESS.md) | `PAT_ID` | medium |
| [FAMILY_PATS](FAMILY_PATS.md) | `PAT_ID` | medium |
| [FAM_DOC_PATS](FAM_DOC_PATS.md) | `LINKED_PAT_ID` | low |
| [FAM_PAT_ENC_RELATIONLIST](FAM_PAT_ENC_RELATIONLIST.md) | `PAT_ID` | medium |
| [FAM_PAT_ENC_RELATIONSHIPS](FAM_PAT_ENC_RELATIONSHIPS.md) | `PAT_ID` | medium |
| [FA_NOTES_QUERY_RESP](FA_NOTES_QUERY_RESP.md) | `QRY_PAT_ID` | low |
| [FB_DISMISS_QUESTIONNAIRE](FB_DISMISS_QUESTIONNAIRE.md) | `PAT_ID` | medium |
| [FIN_ASST_CASE_ASSOC_PAT](FIN_ASST_CASE_ASSOC_PAT.md) | `ASSOC_PAT_ID` | low |
| [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | `PAT_ID` | medium |
| [FIRST_CALL_AUDIT](FIRST_CALL_AUDIT.md) | `PAT_ID` | medium |
| [FOLLOW_UP_TOPICS](FOLLOW_UP_TOPICS.md) | `PAT_ID` | medium |
| [FORM_REPRINT_HX](FORM_REPRINT_HX.md) | `PAT_ID` | medium |
| [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | `PAT_ID` | medium |
| [GYN_CCS_FOLLOWUP_REPL](GYN_CCS_FOLLOWUP_REPL.md) | `PAT_ID` | medium |
| [GYN_CCS_STATUS](GYN_CCS_STATUS.md) | `PAT_ID` | medium |
| [HAR_ALL](HAR_ALL.md) | `PAT_ID` | medium |
| [HEALTH_CARE_AGENT_HX](HEALTH_CARE_AGENT_HX.md) | `PAT_ID` | medium |
| [HELD_ORDERS_REVIEW](HELD_ORDERS_REVIEW.md) | `PAT_ID` | medium |
| [HH_DATASET_INFO](HH_DATASET_INFO.md) | `PAT_ID` | medium |
| [HH_EVV_DATA](HH_EVV_DATA.md) | `PAT_ID` | medium |
| [HH_FORMS_ACCESSED](HH_FORMS_ACCESSED.md) | `PAT_ID` | medium |
| [HH_OASIS_INFO](HH_OASIS_INFO.md) | `PAT_ID` | medium |
| [HH_PAT_CERT_PERIOD](HH_PAT_CERT_PERIOD.md) | `PAT_ID` | medium |
| [HH_PAT_CG1_ADDRESS](HH_PAT_CG1_ADDRESS.md) | `PAT_ID` | medium |
| [HH_PAT_CG1_COMMENT](HH_PAT_CG1_COMMENT.md) | `PAT_ID` | medium |
| [HH_PAT_CG2_ADDRESS](HH_PAT_CG2_ADDRESS.md) | `PAT_ID` | medium |
| [HH_PAT_CG2_COMMENT](HH_PAT_CG2_COMMENT.md) | `PAT_ID` | medium |
| [HH_PAT_INFO](HH_PAT_INFO.md) | `PAT_ID` | medium |
| [HL_REQ_INFO](HL_REQ_INFO.md) | `REQ_PAT_ID` | low |
| [HMT_PPN_AT](HMT_PPN_AT.md) | `PAT_ID` | medium |
| [HM_ACTIVE](HM_ACTIVE.md) | `PAT_ID` | medium |
| [HM_EDIT_AUD](HM_EDIT_AUD.md) | `PAT_ID` | medium |
| [HM_ENC_DATE](HM_ENC_DATE.md) | `PAT_ID` | medium |
| [HM_FORECAST_INFO](HM_FORECAST_INFO.md) | `PAT_ID` | medium |
| [HM_HISTORICAL_STATUS](HM_HISTORICAL_STATUS.md) | `PAT_ID` | medium |
| [HM_HISTORY](HM_HISTORY.md) | `PAT_ID` | medium |
| [HM_PAT_ATTEST_HISTORY](HM_PAT_ATTEST_HISTORY.md) | `PAT_ID` | medium |
| [HM_TOPIC_EDITS](HM_TOPIC_EDITS.md) | `PAT_ID` | medium |
| [HM_TOPIC_METADATA](HM_TOPIC_METADATA.md) | `PAT_ID` | medium |
| [HNO_LINKED_PATS](HNO_LINKED_PATS.md) | `LINKED_PAT_ID` | low |
| [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | `PAT_ID` | medium |
| [HOSPICE_DX_HX](HOSPICE_DX_HX.md) | `PAT_ID` | medium |
| [HSC_SPEC_INFO](HSC_SPEC_INFO.md) | `PAT_ID` | medium |
| [HSP_CLAIM_DETAIL2](HSP_CLAIM_DETAIL2.md) | `SG_PAT_ID` | low |
| [HSP_DEATH_STATUS](HSP_DEATH_STATUS.md) | `PAT_ID` | medium |
| [HSP_HOME_LINK_VISITS](HSP_HOME_LINK_VISITS.md) | `PAT_ID` | medium |
| [HSP_PREADM_CONFRM](HSP_PREADM_CONFRM.md) | `PAT_ID` | medium |
| [HSP_PREADM_TEST](HSP_PREADM_TEST.md) | `PAT_ID` | medium |
| [HSP_SPEC_NEED](HSP_SPEC_NEED.md) | `PAT_ID` | medium |
| [HSP_SPEC_NEED_CMT](HSP_SPEC_NEED_CMT.md) | `PAT_ID` | medium |
| [IB_MESSAGES](IB_MESSAGES.md) | `PAT_ID` | medium |
| [IDENTITY_ID](IDENTITY_ID.md) | `PAT_ID` | medium |
| [IDENTITY_ID_HX](IDENTITY_ID_HX.md) | `PAT_ID` | medium |
| [IMMNZTN_LAST_REVIEW](IMMNZTN_LAST_REVIEW.md) | `PAT_ID` | medium |
| [IMMUNE_REVIEW](IMMUNE_REVIEW.md) | `PAT_ID` | medium |
| [INCOMPLETE_NOTE_EPT](INCOMPLETE_NOTE_EPT.md) | `PAT_ID` | medium |
| [INFECTIONS](INFECTIONS.md) | `PAT_ID` | medium |
| [INFECTION_ABSTNS](INFECTION_ABSTNS.md) | `PAT_ID` | medium |
| [INFERTILITY_CYCLE_LINKS](INFERTILITY_CYCLE_LINKS.md) | `LINKED_PAT_ID` | low |
| [INFO_REQUEST](INFO_REQUEST.md) | `PAT_ID` | medium |
| [INTERVENTION](INTERVENTION.md) | `PAT_ID` | medium |
| [INTRAOP_EMERGENCIES](INTRAOP_EMERGENCIES.md) | `PAT_ID` | medium |
| [INTRAOP_EMERG_PUSH_NOTIF](INTRAOP_EMERG_PUSH_NOTIF.md) | `PAT_ID` | medium |
| [INVOICE](INVOICE.md) | `PAT_ID` | medium |
| [IP_ALERT_AUDIT_ITM](IP_ALERT_AUDIT_ITM.md) | `PAT_ID` | medium |
| [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | `PAT_ID` | medium |
| [IP_LDA_NOADDSINGLE](IP_LDA_NOADDSINGLE.md) | `PAT_ID` | medium |
| [IP_WORKLIST_2](IP_WORKLIST_2.md) | `LINKED_PAT_ID` | low |
| [ISOLATIONS](ISOLATIONS.md) | `PAT_ID` | medium |
| [KIOSK_QUESTIONNAIR](KIOSK_QUESTIONNAIR.md) | `PAT_ID` | medium |
| [LCA_COMM_USERS](LCA_COMM_USERS.md) | `COMM_PAT_ID` | low |
| [LCA_RECORD_STATUS](LCA_RECORD_STATUS.md) | `PAT_ID` | medium |
| [LENGTH_OF_STAY](LENGTH_OF_STAY.md) | `PAT_ID` | medium |
| [LNO_NOADD_SINGLE](LNO_NOADD_SINGLE.md) | `PAT_ID` | medium |
| [LOADED_EXTERNAL_CVG_DATA](LOADED_EXTERNAL_CVG_DATA.md) | `PAT_ID` | medium |
| [LOC_PRIOR_STAY](LOC_PRIOR_STAY.md) | `PAT_ID` | medium |
| [MCARE_MCAID_DUAL_ELIGIB](MCARE_MCAID_DUAL_ELIGIB.md) | `PAT_ID` | medium |
| [MC_CLAIM_PRICER](MC_CLAIM_PRICER.md) | `ASSOC_PAT_ID` | low |
| [MC_CVG_ELIG_VERIFICATION](MC_CVG_ELIG_VERIFICATION.md) | `MEMBER_PAT_ID` | low |
| [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | `MC_PAT_ID` | low |
| [MDS_RECS](MDS_RECS.md) | `PAT_ID` | medium |
| [MEDICAL_READINESS_HX](MEDICAL_READINESS_HX.md) | `PAT_ID` | medium |
| [MEDS_REV_HX](MEDS_REV_HX.md) | `PAT_ID` | medium |
| [MEDS_REV_HX_LIST](MEDS_REV_HX_LIST.md) | `PAT_ID` | medium |
| [MEDS_REV_LAST_LIST](MEDS_REV_LAST_LIST.md) | `PAT_ID` | medium |
| [MED_CVG_INFO](MED_CVG_INFO.md) | `PAT_ID` | medium |
| [MED_PAUSE_LOG](MED_PAUSE_LOG.md) | `PAT_ID` | medium |
| [MED_THERAPY_PROB_INFO](MED_THERAPY_PROB_INFO.md) | `PAT_ID` | medium |
| [MEMBER_NOTES](MEMBER_NOTES.md) | `PAT_ID` | medium |
| [MEMBER_PAT_LINKS](MEMBER_PAT_LINKS.md) | `PAT_ID` | medium |
| [MEM_ALL_PROV_CONSENT_INFO](MEM_ALL_PROV_CONSENT_INFO.md) | `PAT_ID` | medium |
| [MEM_CUST_ATTR](MEM_CUST_ATTR.md) | `PAT_ID` | medium |
| [MEM_PAYER_API_CON_INFO](MEM_PAYER_API_CON_INFO.md) | `PAT_ID` | medium |
| [MODALITY_DATA](MODALITY_DATA.md) | `PAT_ID` | medium |
| [MSG_ROUTING_PAT_ENC](MSG_ROUTING_PAT_ENC.md) | `PAT_ID` | medium |
| [MYC_CONVO](MYC_CONVO.md) | `PAT_ID` | medium |
| [MYC_DISPLAY_FB_QUESTION](MYC_DISPLAY_FB_QUESTION.md) | `PAT_ID` | medium |
| [MYC_FEEDBACK_QNR_DATA](MYC_FEEDBACK_QNR_DATA.md) | `PAT_ID` | medium |
| [MYC_MESG](MYC_MESG.md) | `PAT_ID` | medium |
| [MYC_PATIENT](MYC_PATIENT.md) | `PAT_ID` | medium |
| [NATIONALITY](NATIONALITY.md) | `PAT_ID` | medium |
| [NCDR_AFIBV2_DEMOGRAPHICS](NCDR_AFIBV2_DEMOGRAPHICS.md) | `PAT_ID` | medium |
| [NCDR_EPDIV3_DEMOGRAPHICS](NCDR_EPDIV3_DEMOGRAPHICS.md) | `PAT_ID` | medium |
| [NEPHROLOGY_COMORB_COND](NEPHROLOGY_COMORB_COND.md) | `PAT_ID` | medium |
| [NEW_CP_PAT_NOTIF_LOG](NEW_CP_PAT_NOTIF_LOG.md) | `NOTIF_RECIP_PAT_ID` | low |
| [NHSN_CLIP_ABSTNS](NHSN_CLIP_ABSTNS.md) | `PAT_ID` | medium |
| [NHSN_PROC_ABSTNS](NHSN_PROC_ABSTNS.md) | `PAT_ID` | medium |
| [NSQIP_INFO](NSQIP_INFO.md) | `PAT_ID` | medium |
| [OBGYN_STAT](OBGYN_STAT.md) | `PAT_ID` | medium |
| [ODC_BASIC](ODC_BASIC.md) | `ODC_PAT_ID` | low |
| [ONE_PAGER_REVIEW_COMPONS](ONE_PAGER_REVIEW_COMPONS.md) | `PAT_ID` | medium |
| [ONE_PAGER_REVIEW_INFO](ONE_PAGER_REVIEW_INFO.md) | `PAT_ID` | medium |
| [ORDER_MED](ORDER_MED.md) | `PAT_ID` | medium |

_… and 359 more (see `data/references.jsonl`)._

