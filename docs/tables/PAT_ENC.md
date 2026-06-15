# PAT_ENC

> The patient encounter table contains one record for each patient encounter in your system. By default, this table does not contain Registration or PCP/Clinic Change contacts (encounter types 1 and 31). It does contain all appointments, office visits, telephone encounters, and other types of encounters. The primary key for the patient encounter table is PAT_ENC_CSN_ID. Note that there is an index named EIX_FILT_PAT_ENC_RFL on the REFERRAL_ID column in Oracle that does not appear in the index list. The index is created by EFN_FAUX_RFL_FILT_INX.

**Overflow family:** [PAT_ENC_2](PAT_ENC_2.md), [PAT_ENC_3](PAT_ENC_3.md), [PAT_ENC_4](PAT_ENC_4.md), [PAT_ENC_5](PAT_ENC_5.md), [PAT_ENC_6](PAT_ENC_6.md), [PAT_ENC_7](PAT_ENC_7.md), [PAT_ENC_8](PAT_ENC_8.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 72  
**Org-specific columns:** 9  
**Joined by:** 691 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | PK | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `FIN_CLASS_C_NAME` | VARCHAR | org | The category value associated with the Financial Class of the encounter. Note: This item is only populated through an interface. It is not populated if you have billing system installed. |
| 7 | `VISIT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `VISIT_PROV_TITLE_NAME` | VARCHAR | org | The visit provider’s provider title (SER 5). See VISIT_PROV_ID above for the definition of visit provider. |
| 9 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `LMP_DATE` | DATETIME |  | The date of the patient’s Last Menstrual Period. Only contains data for encounters with female patients. |
| 11 | `ENC_CLOSED_YN` | VARCHAR |  | A flag that signifies if this encounter is closed as of the time of the enterprise reporting extract. This column will have the value Y, N or null. Null indicates that closing the encounter does not apply, such as a future appointment. |
| 12 | `ENC_CLOSED_USER_ID` | VARCHAR |  | The unique ID of the system user who closed the patient encounter. This ID may be encrypted. |
| 13 | `ENC_CLOSED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `ENC_CLOSE_DATE` | DATETIME |  | The date on which the patient encounter was closed. |
| 15 | `LOS_MODIFIER1_ID` | VARCHAR |  | The first Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| 16 | `LOS_MODIFIER1_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 17 | `LOS_MODIFIER2_ID` | VARCHAR |  | The second Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| 18 | `LOS_MODIFIER2_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 19 | `LOS_MODIFIER3_ID` | VARCHAR |  | The third Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| 20 | `LOS_MODIFIER3_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 21 | `LOS_MODIFIER4_ID` | VARCHAR |  | The fourth Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| 22 | `LOS_MODIFIER4_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 23 | `APPT_STATUS_C_NAME` | VARCHAR | org | The category value associated with the appointment status of the encounter as of the most recent enterprise reporting extract, such as 1 – Scheduled, 2 – Completed, 3 – Canceled, etc. |
| 24 | `APPT_CANC_USER_ID` | VARCHAR |  | The unique ID of the user who canceled the appointment. |
| 25 | `APPT_CANC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `CHECKIN_USER_ID` | VARCHAR |  | The unique ID of the system user who checked in the patient for this encounter. If the encounter has not been through the Check In process this field will be NULL. This ID may be encrypted. |
| 27 | `CHECKIN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `HOSP_ADMSN_TIME` | DATETIME (Local) |  | The date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. |
| 29 | `HOSP_DISCHRG_TIME` | DATETIME (Local) |  | The hospital discharge date and time for this patient contact. |
| 30 | `HOSP_ADMSN_TYPE_C_NAME` | VARCHAR | org | The category value for the type of admission for this encounter. |
| 31 | `NONCVRED_SERVICE_YN` | VARCHAR |  | A flag used to indicate whether the appointment is scheduled in a service not covered by the patient's coverage benefits. The flag is set to "Y" when the service is not covered and an "N" when it is covered. |
| 32 | `REFERRAL_REQ_YN` | VARCHAR |  | A flag used to indicate whether an appointment requires a referral as determined by the visit coverage. This flag is set to “Y” when the appointment requires a referral. If the appointment does not require a referral, it is set to “N." |
| 33 | `REFERRAL_ID` | NUMERIC | FK→ | The unique ID of the referral record linked to this appointment. |
| 34 | `ACCOUNT_ID` | NUMERIC | FK→ | The ID number of the guarantor account assigned to the visit at the time it is scheduled or when it is checked in. This ID may be encrypted. |
| 35 | `COVERAGE_ID` | NUMERIC | FK→ | The ID number of the coverage record assigned to the visit at the time it is scheduled or when it is checked in. This ID may be encrypted. |
| 36 | `CLAIM_ID` | NUMERIC | FK→ | The unique ID of the billing system Claim record (CLM record) linked to charges associated with this visit. |
| 37 | `PRIMARY_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 38 | `CHARGE_SLIP_NUMBER` | VARCHAR |  | The encounter form number or charge slip number assigned to this encounter. Note: The charge slip number is also stored in the financial table CLARITY_TDL. You can use this field to link to CLARITY_TDL to identify financial transactions associated with the encounter. |
| 39 | `COPAY_DUE` | NUMERIC |  | The dollar amount shown in the Copay Due field of the scheduling system's Check In Patient activity. This amount may be calculated by the system using the patient's coverage benefit information or be manually entered by a user. This field may also be empty if no copay amount was entered when the patient's appointment was checked in. |
| 40 | `UPDATE_DATE` | DATETIME (Local) |  | The time this patient encounter was pulled into enterprise reporting. |
| 41 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The ID number of the hospital billing account assigned to the encounter. |
| 42 | `ADM_FOR_SURG_YN` | VARCHAR |  | Indicates whether the patient is being admitted for surgery. |
| 43 | `SURGICAL_SVC_C_NAME` | VARCHAR | org | The category value corresponding to the surgical service for this patient contact. |
| 44 | `INPATIENT_DATA_ID` | VARCHAR | shared | The ID number of the record used to determine how inpatient data is stored for the encounter. |
| 45 | `IP_EPISODE_ID` | NUMERIC |  | The ID number of the inpatient episode of care. This includes discharges from the ED. |
| 46 | `EXTERNAL_VISIT_ID` | VARCHAR |  | The ID for the contact as assigned by a non-system. Usually populated by an interface. |
| 47 | `CONTACT_COMMENT` | VARCHAR |  | Comments entered by the provider for the contact. |
| 48 | `OUTGOING_CALL_YN` | VARCHAR |  | Indicates whether a call associated with a telephone encounter was initiated by the patient or by the clinic / hospital. A "Y" indicates an outgoing call placed by the clinic / hospital while an "N" indicates and incoming call from the patient. |
| 49 | `DATA_ENTRY_PERSON` | VARCHAR |  | This is the name of the user who created the encounter. |
| 50 | `REFERRAL_SOURCE_ID` | VARCHAR |  | The referral ID number of the referring physician. This physician may be from an external organization. |
| 51 | `REFERRAL_SOURCE_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 52 | `WC_TPL_VISIT_C_NAME` | VARCHAR | org | A field used to indicate whether the patient's contact is related to workers compensation or third party liability situation. |
| 53 | `CONSENT_TYPE_C_NAME` | VARCHAR | org | This item describes the type of consent that was filed for a given encounter. It is a single-response customer-defined category. |
| 54 | `BMI` | NUMERIC |  | This is the patient's Body Mass Index, which is calculated based on the recorded height and weight. |
| 55 | `BSA` | NUMERIC |  | This is the patient's Body Surface Area, which is calculated based on the recorded height and weight. |
| 56 | `AVS_PRINT_TM` | DATETIME (Local) |  | The instant that the After Visit Summary (AVS) was printed for this encounter. |
| 57 | `AVS_FIRST_USER_ID` | VARCHAR |  | Unique ID of the user who first prints out the After Visit Summary (AVS) for the encounter. |
| 58 | `AVS_FIRST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 59 | `ENC_MED_FRZ_RSN_C_NAME` | VARCHAR |  | The encounter medication freeze reason's category value. |
| 60 | `EFFECTIVE_DATE_DT` | DATETIME |  | The date of the encounter. The returned date is handled differently depending on the contact type of the encounter: If it is a surgery encounter, the date of the surgery will be returned. If it is a Hospital encounter, Admission/Discharge/Transfer (ADT) info will be used to return an appropriate date. If ADT info cannot be found, then the Hospital Admission date (I EPT 18850) will be returned. If the Hospital Admission Date cannot be found, the temporary admission date (I EPT 18846) will be returned.. |
| 61 | `DISCHARGE_DATE_DT` | DATETIME |  | The discharge date for the encounter. |
| 62 | `COPAY_PD_THRU_NAME` | VARCHAR | org | The method by which the copay for an appointment was paid (e.g., via MyChart, a kiosk). |
| 63 | `INTERPRETER_NEED_YN` | VARCHAR |  | A flag used to indicate whether a patient requires an interpreter for an encounter. |
| 64 | `VST_SPECIAL_NEEDS_C_NAME` | VARCHAR | org | This field captures any special needs for a visit. |
| 65 | `BEN_ENG_SP_AMT` | NUMERIC |  | Stores the adjudicated self-pay amount (the amount required to be paid by the patient) when determining the copay amount for the visit. |
| 66 | `BEN_ADJ_COPAY_AMT` | NUMERIC |  | Stores the adjudicated copy amount for the visit according to the patient's coverage benefits. |
| 67 | `BEN_ADJ_METHOD_C_NAME` | VARCHAR |  | Flag to indicate if and how the adjudicated copay was overridden |
| 68 | `ENC_CREATE_USER_ID` | VARCHAR |  | The ID number of the user who create the patient or encounter record. |
| 69 | `ENC_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 70 | `ENC_INSTANT` | DATETIME (Local) |  | The instant an encounter was created |
| 71 | `EFFECTIVE_DATE_DTTM` | DATETIME (Local) |  | The start date and time of an encounter. The start date is pulled from the date stored in the EFFECTIVE_DATE_DT column. The time references the first populated time in the following fields: hospital admission time (EPT 18851), hospital temporary admission time (EPT 18847), ADT arrival time (EPT 10815), and expected admission time (EPT 10300). The SlicerDicer reporting application uses this column to determine the EffectiveStartDate of encounters. |
| 72 | `CALCULATED_ENC_STAT_C_NAME` | VARCHAR |  | A status flag used to determine whether to include data from the encounter in the SlicerDicer reporting application. Statuses includes 1-Possible (e.g., the encounter is a scheduled outpatient appointment or the admission is pending) or 2-Complete (e.g., the appointment is complete, the admission is discharged). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (691)

| From | Column | Confidence |
|------|--------|------------|
| [ABN_DOCUMENT_ID](ABN_DOCUMENT_ID.md) | `PAT_ENC_CSN_ID` | high |
| [ABN_NOTES](ABN_NOTES.md) | `PAT_CSN` | low |
| [ACTIVE_ASYNC_BPAS](ACTIVE_ASYNC_BPAS.md) | `PAT_ENC_CSN_ID` | high |
| [ADDITIONAL_EM_CODE](ADDITIONAL_EM_CODE.md) | `PAT_ENC_CSN_ID` | high |
| [ADMISSION_COMMENTS](ADMISSION_COMMENTS.md) | `PAT_ENC_CSN_ID` | high |
| [ADM_EXPECT_DATES](ADM_EXPECT_DATES.md) | `PAT_ENC_CSN_ID` | high |
| [AGENDA_INFO](AGENDA_INFO.md) | `LINKED_PAT_ENC_CSN_ID` | low |
| [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ALERT](ALERT.md) | `PAT_CSN` | low |
| [ALLERGY](ALLERGY.md) | `ALLERGY_PAT_CSN` | low |
| [ALLOWED_TLH_MODES_LIST](ALLOWED_TLH_MODES_LIST.md) | `PAT_ENC_CSN_ID` | high |
| [ALTERNATIVE_MEDS](ALTERNATIVE_MEDS.md) | `PAT_ENC_CSN_ID` | high |
| [ALTERNATIVE_PROCS](ALTERNATIVE_PROCS.md) | `PAT_ENC_CSN_ID` | high |
| [ALT_ORD_PROV_ADDR](ALT_ORD_PROV_ADDR.md) | `PAT_ENC_CSN_ID` | high |
| [ALT_ORD_PROV_CMTS](ALT_ORD_PROV_CMTS.md) | `PAT_ENC_CSN_ID` | high |
| [ALT_ORD_PROV_MEDLC](ALT_ORD_PROV_MEDLC.md) | `PAT_ENC_CSN_ID` | high |
| [ALT_ORD_PROV_SINGL](ALT_ORD_PROV_SINGL.md) | `PAT_ENC_CSN_ID` | high |
| [ANTICOAG_AUDIT](ANTICOAG_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [ANTICOAG_ENC_PAUSE_DATES](ANTICOAG_ENC_PAUSE_DATES.md) | `PAT_ENC_CSN_ID` | high |
| [AN_HSB_LINK_INFO](AN_HSB_LINK_INFO.md) | `AN_52_ENC_CSN_ID` | low |
| [AN_HSB_LINK_INFO](AN_HSB_LINK_INFO.md) | `PRIMARY_LOG_ENC_CSN` | low |
| [AN_HSB_LINK_INFO](AN_HSB_LINK_INFO.md) | `PRIMARY_PRC_ENC_CSN` | low |
| [AN_PAT_MU_PROV](AN_PAT_MU_PROV.md) | `PAT_ENC_CSN_ID` | high |
| [AN_RELINK_INFO](AN_RELINK_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [APPEAL_GRV_2](APPEAL_GRV_2.md) | `PAT_ENC_CSN_ID` | high |
| [APPT_DECL_DATES_AUDIT](APPT_DECL_DATES_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [APPT_LENGTH_OVERRIDE](APPT_LENGTH_OVERRIDE.md) | `PAT_ENC_CSN_ID` | high |
| [APPT_LETTER_RECIPIENTS](APPT_LETTER_RECIPIENTS.md) | `PAT_ENC_CSN_ID` | high |
| [APPT_SELF_CHECKIN_INFO](APPT_SELF_CHECKIN_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `PAT_ENC_CSN_ID` | high |
| [ARPB_VISITS](ARPB_VISITS.md) | `PRIM_ENC_CSN_ID` | low |
| [ARRIVAL_EVENT_TASK_ITEM](ARRIVAL_EVENT_TASK_ITEM.md) | `PAT_ENC_CSN_ID` | high |
| [ARRIVAL_EVENT_TASK_RULE](ARRIVAL_EVENT_TASK_RULE.md) | `PAT_ENC_CSN_ID` | high |
| [ARR_EVENT_TASK_EXTENSION](ARR_EVENT_TASK_EXTENSION.md) | `PAT_ENC_CSN_ID` | high |
| [ARR_EVENT_TASK_ITEM_NAME](ARR_EVENT_TASK_ITEM_NAME.md) | `PAT_ENC_CSN_ID` | high |
| [ASSOCIATED_REFERRALS](ASSOCIATED_REFERRALS.md) | `PAT_ENC_CSN_ID` | high |
| [ASSOCIATED_RFL_ERR_CODES](ASSOCIATED_RFL_ERR_CODES.md) | `PAT_ENC_CSN_ID` | high |
| [AUTHORIZATIONS](AUTHORIZATIONS.md) | `FIRST_PAT_ENC_CSN_ID` | low |
| [AUTHORIZATIONS](AUTHORIZATIONS.md) | `LAST_PAT_ENC_CSN_ID` | low |
| [AUTO_WORKFLOW_DETAILS](AUTO_WORKFLOW_DETAILS.md) | `PAT_ENC_CSN_ID` | high |
| [AUTO_WT_LST_OFFER_UTC](AUTO_WT_LST_OFFER_UTC.md) | `PAT_ENC_CSN_ID` | high |
| [AVS_ACK_MED_INFO](AVS_ACK_MED_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [AVS_ESIG_INFO](AVS_ESIG_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [BEDSIDE_ENC_ACTIVATION](BEDSIDE_ENC_ACTIVATION.md) | `PAT_ENC_CSN_ID` | high |
| [BEDSIDE_WHITEBOARD_DEPT](BEDSIDE_WHITEBOARD_DEPT.md) | `PAT_ENC_CSN_ID` | high |
| [BEREAVE_FOL_INFO](BEREAVE_FOL_INFO.md) | `PAT_CSN` | low |
| [BILLING_ENC_HX](BILLING_ENC_HX.md) | `PAT_ENC_CSN_ID` | high |
| [BILL_SCHED_PMT_PAT_CSN](BILL_SCHED_PMT_PAT_CSN.md) | `PAT_ENC_CSN_ID` | high |
| [BLOOD_SPECIAL_REQTS_AUDIT](BLOOD_SPECIAL_REQTS_AUDIT.md) | `BLOOD_REQTS_PAT_ENC_CSN_ID` | low |
| [BREAST_IMG_HORMONES](BREAST_IMG_HORMONES.md) | `PAT_ENC_CSN_ID` | high |
| [BUNDLE_CHARGE_MAIN](BUNDLE_CHARGE_MAIN.md) | `PAT_CSN` | low |
| [CAL_COMM_HX_PAT_CSN](CAL_COMM_HX_PAT_CSN.md) | `REF_PAT_CSN` | low |
| [CANCER_RISK_INFO](CANCER_RISK_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_PERSONAL](CANCER_RISK_PERSONAL.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_REQ_COMMENT](CANCER_RISK_REQ_COMMENT.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_REQ_INFO](CANCER_RISK_REQ_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_REQ_MODEL](CANCER_RISK_REQ_MODEL.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_REQ_STATUS](CANCER_RISK_REQ_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_SCORE_AGE](CANCER_RISK_SCORE_AGE.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_SCORE_DX](CANCER_RISK_SCORE_DX.md) | `PAT_ENC_CSN_ID` | high |
| [CANCER_RISK_SCORE_TYPE](CANCER_RISK_SCORE_TYPE.md) | `PAT_ENC_CSN_ID` | high |
| [CAREPLAN_CNCT_INFO](CAREPLAN_CNCT_INFO.md) | `READING_PAT_ENC_CSN_ID` | low |
| [CAREPLAN_ENROLLMENT_INFO](CAREPLAN_ENROLLMENT_INFO.md) | `SURGICAL_PAT_ENC_CSN_ID` | low |
| [CAREPLAN_INFO](CAREPLAN_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [CHAT_CONVERSATIONS](CHAT_CONVERSATIONS.md) | `PAT_ENC_CSN_ID` | high |
| [CHAT_MESSAGE_CONTENT](CHAT_MESSAGE_CONTENT.md) | `LINK_RDS_PAT_ENC_CSN_ID` | low |
| [CHRT_ROUTING_HX](CHRT_ROUTING_HX.md) | `PAT_ENC_CSN_ID` | high |
| [CLARITY_ADT](CLARITY_ADT.md) | `PAT_ENC_CSN_ID` | high |
| [CL_LNK_ORDERS](CL_LNK_ORDERS.md) | `PAT_CSN` | low |
| [CL_PAT_EDU_OS](CL_PAT_EDU_OS.md) | `PAT_CSN` | low |
| [CL_PLC](CL_PLC.md) | `PAT_ENC_CSN_ID` | high |
| [CMGMT_EPISODE_HX](CMGMT_EPISODE_HX.md) | `ACTION_ENC_CSN_ID` | low |
| [CMGMT_EPISODE_HX](CMGMT_EPISODE_HX.md) | `REMOVING_ENC_CSN_ID` | low |
| [CMGMT_REV_ENC_EPSD_UPDT](CMGMT_REV_ENC_EPSD_UPDT.md) | `PAT_ENC_CSN_ID` | high |
| [CODING_CLA_NOTES](CODING_CLA_NOTES.md) | `PAT_ENC_CSN_ID` | high |
| [COD_CONTACT_INFO](COD_CONTACT_INFO.md) | `CDI_REVIEW_PAT_ENC_CSN_ID` | low |
| [COHORT_LEN_OF_STAY_BENCH](COHORT_LEN_OF_STAY_BENCH.md) | `PAT_ENC_CSN_ID` | high |
| [COMMUNITY_RESOURCE](COMMUNITY_RESOURCE.md) | `CREATING_PAT_ENC_CSN_ID` | low |
| [COMMUNITY_RESOURCE_CNCT](COMMUNITY_RESOURCE_CNCT.md) | `DOCUMENTING_PAT_ENC_CSN_ID` | low |
| [COMMUNITY_RESRC_REVIEWED](COMMUNITY_RESRC_REVIEWED.md) | `CBO_REVIEW_PAT_ENC_CSN_ID` | low |
| [COMMUNITY_RESRC_REVIEW_HX](COMMUNITY_RESRC_REVIEW_HX.md) | `CBO_HX_REVIEW_PAT_ENC_CSN_ID` | low |
| [COMP_ASMT_FORMS](COMP_ASMT_FORMS.md) | `PAT_ENC_CSN_ID` | high |
| [CONTRACEPTIVES_EXIT](CONTRACEPTIVES_EXIT.md) | `PAT_ENC_CSN_ID` | high |
| [CONTRACEPTIVES_INTAKE](CONTRACEPTIVES_INTAKE.md) | `PAT_ENC_CSN_ID` | high |
| [CRF_ASSOCIATED_CSN](CRF_ASSOCIATED_CSN.md) | `REF_DATA_PAT_ENC_CSN_ID` | low |
| [CUST_SERVICE](CUST_SERVICE.md) | `PAT_ENC_CSN_ID` | high |
| [DC_VN_PRV_ACTN_ADT](DC_VN_PRV_ACTN_ADT.md) | `DC_VN_PAT_CSN` | low |
| [DECISION_LETTERS](DECISION_LETTERS.md) | `LETTER_PAT_ENC_CSN_ID` | low |
| [DENTAL_PAT_PHASE](DENTAL_PAT_PHASE.md) | `PAT_ENC_CSN_ID` | high |
| [DENTAL_VOUCHER_FEES](DENTAL_VOUCHER_FEES.md) | `PAT_ENC_CSN_ID` | high |
| [DENT_ORTHO_APPLIANCE](DENT_ORTHO_APPLIANCE.md) | `MODIFIED_PAT_ENC_CSN_ID` | low |
| [DENT_ORTH_EXAM_NOTES](DENT_ORTH_EXAM_NOTES.md) | `PAT_ENC_CSN_ID` | high |
| [DEPT_PAT_CARE_SELECTION](DEPT_PAT_CARE_SELECTION.md) | `DPCAR_PAT_ENC_CSN_ID` | low |
| [DIET_ORDERS](DIET_ORDERS.md) | `PAT_ENC_CSN_ID` | high |
| [DIFF_DX_MOD_TYPE](DIFF_DX_MOD_TYPE.md) | `PAT_ENC_CSN_ID` | high |
| [DIFF_DX_MOD_VALUES](DIFF_DX_MOD_VALUES.md) | `PAT_ENC_CSN_ID` | high |
| [DISCHARGE_DELAYS](DISCHARGE_DELAYS.md) | `PAT_ENC_CSN_ID` | high |
| [DISCHARGE_DELAYS_HX](DISCHARGE_DELAYS_HX.md) | `PAT_ENC_CSN_ID` | high |
| [DISCHARGE_MILESTONES_HX](DISCHARGE_MILESTONES_HX.md) | `PAT_ENC_CSN_ID` | high |
| [DISCH_DISPOSITION_HX](DISCH_DISPOSITION_HX.md) | `PAT_ENC_CSN_ID` | high |
| [DISCH_INSTR_MTHD](DISCH_INSTR_MTHD.md) | `PAT_ENC_CSN_ID` | high |
| [DISCONTINUED_MEDS](DISCONTINUED_MEDS.md) | `PAT_ENC_CSN_ID` | high |
| [DISCRETE_PAT_INSTR_EDIT](DISCRETE_PAT_INSTR_EDIT.md) | `PAT_CSN` | low |
| [DOCS_RCVD_ALGS](DOCS_RCVD_ALGS.md) | `ALG_PAT_ENC_CSN_ID` | low |
| [DOCS_RCVD_DETAILS_2](DOCS_RCVD_DETAILS_2.md) | `PEHX_SRC_PAT_ENC_CSN_ID` | low |
| [DOCS_RCVD_MEDS](DOCS_RCVD_MEDS.md) | `MED_PAT_ENC_CSN_ID` | low |
| [DOCS_RCVD_PROBS](DOCS_RCVD_PROBS.md) | `PROB_PAT_ENC_CSN_ID` | low |
| [DOC_ENC_LNK_REF](DOC_ENC_LNK_REF.md) | `DOC_LNK_PAT_ENC_CSN_ID` | low |
| [DOC_INFORMATION_2](DOC_INFORMATION_2.md) | `CLN_DOC_SRC_APT_PAT_ENC_CSN_ID` | low |
| [DOC_LINKED_PAT_CSNS](DOC_LINKED_PAT_CSNS.md) | `LINKED_PAT_ENC_CSN_ID` | low |
| [DP_COMM_ATTACHMENTS](DP_COMM_ATTACHMENTS.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_EOW_RM](DP_COMM_EOW_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_IDENTIFIER_RM](DP_COMM_IDENTIFIER_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_INST_RM](DP_COMM_INST_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_LRP_RM](DP_COMM_LRP_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_MEMO_NOTE](DP_COMM_MEMO_NOTE.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_MODE_RM](DP_COMM_MODE_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_ORIG_LINE_RM](DP_COMM_ORIG_LINE_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COMM_ROI_RM](DP_COMM_ROI_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COORD_COMP_STATUS](DP_COORD_COMP_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [DP_COORD_TYPE_DOC](DP_COORD_TYPE_DOC.md) | `PAT_ENC_CSN_ID` | high |
| [DP_FACILITY](DP_FACILITY.md) | `PAT_ENC_CSN_ID` | high |
| [DP_FAC_COMMUNICATIONS](DP_FAC_COMMUNICATIONS.md) | `PAT_ENC_CSN_ID` | high |
| [DP_FAC_DECLN_RSN_RM](DP_FAC_DECLN_RSN_RM.md) | `PAT_ENC_CSN_ID` | high |
| [DP_FAC_FOLLOW_UP](DP_FAC_FOLLOW_UP.md) | `PAT_ENC_CSN_ID` | high |
| [DP_FAC_REASON_COMMENT](DP_FAC_REASON_COMMENT.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SECONDARY_SVC_TO_COORD](DP_SECONDARY_SVC_TO_COORD.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SEC_SVC_TO_COORD_AUDIT](DP_SEC_SVC_TO_COORD_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SELECTED_SERVICE](DP_SELECTED_SERVICE.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SEL_CNCT_PT_PURPOSE](DP_SEL_CNCT_PT_PURPOSE.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SERVICE_COORD_PLAN](DP_SERVICE_COORD_PLAN.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SVC_COORD_NOTE](DP_SVC_COORD_NOTE.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SVC_COORD_PLAN_AUDIT](DP_SVC_COORD_PLAN_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SVC_TO_COORDINATE](DP_SVC_TO_COORDINATE.md) | `PAT_ENC_CSN_ID` | high |
| [DP_SVC_TO_COORD_AUDIT](DP_SVC_TO_COORD_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [DTREE_NODES_USED](DTREE_NODES_USED.md) | `CREATED_PAT_ENC_CSN_ID` | low |
| [DUAL_ADMISSION_UPDATES](DUAL_ADMISSION_UPDATES.md) | `DUAL_ADMSN_PAT_ENC_CSN_ID` | low |
| [DUAL_ADMISSION_UPDATES](DUAL_ADMISSION_UPDATES.md) | `PAT_ENC_CSN_ID` | high |
| [DXR_REVIEW_INFO](DXR_REVIEW_INFO.md) | `REVIEW_ENC_CSN` | low |
| [ECHKIN_PHASE_INFO](ECHKIN_PHASE_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ECHKIN_SESSION_INFO](ECHKIN_SESSION_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ECHKIN_STEP_INFO](ECHKIN_STEP_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ECHKIN_WARNINGS](ECHKIN_WARNINGS.md) | `PAT_ENC_CSN_ID` | high |
| [EDBDSIDE_PAT_ENC_WAITPRED](EDBDSIDE_PAT_ENC_WAITPRED.md) | `PAT_ENC_CSN_ID` | high |
| [ED_CONSULT_STATUS](ED_CONSULT_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [ED_DISPO_AUDIT](ED_DISPO_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [ED_FOLLOWUP_AUDIT](ED_FOLLOWUP_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [ED_FOLLOWUP_INFO](ED_FOLLOWUP_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ED_IEV_PAT_INFO](ED_IEV_PAT_INFO.md) | `PAT_CSN` | low |
| [ED_IEV_PAT_INFO](ED_IEV_PAT_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [ED_LAB_STATUS](ED_LAB_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [ED_OTHER_STATUS](ED_OTHER_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [ED_PAT_STATUS](ED_PAT_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [ED_RAD_STATUS](ED_RAD_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [EM_CODE_CALC](EM_CODE_CALC.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_CLASS](ENC_CLASS.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_CLIENT_SERVICES](ENC_CLIENT_SERVICES.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_DX_ASSOC_AMBIENT_DX](ENC_DX_ASSOC_AMBIENT_DX.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_DX_ASSOC_DATA](ENC_DX_ASSOC_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_DX_ASSOC_NOTES](ENC_DX_ASSOC_NOTES.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_DX_EDIT_TRAIL](ENC_DX_EDIT_TRAIL.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_FRM_GROUPS](ENC_FRM_GROUPS.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_INFO_RFL_AUTH_REQUEST](ENC_INFO_RFL_AUTH_REQUEST.md) | `AUTH_PAT_ENC_CSN_ID` | low |
| [ENC_LETTERS](ENC_LETTERS.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_METRIC_ENGINE_CALC](ENC_METRIC_ENGINE_CALC.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_METRIC_ENGINE_RSLT](ENC_METRIC_ENGINE_RSLT.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_METRIC_ENGINE_SRC](ENC_METRIC_ENGINE_SRC.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_METRIC_ENGINE_VAR](ENC_METRIC_ENGINE_VAR.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_METRIC_ENGINE_VARVAL](ENC_METRIC_ENGINE_VARVAL.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_MULT_REF_ID](ENC_MULT_REF_ID.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_SPEC_NEEDS](ENC_SPEC_NEEDS.md) | `PAT_ENC_CSN_ID` | high |
| [ENC_SPEC_NEEDS_CMT](ENC_SPEC_NEEDS_CMT.md) | `PAT_ENC_CSN_ID` | high |
| [ENROLL_LINKED_CSN2](ENROLL_LINKED_CSN2.md) | `PAT_CSN` | low |
| [ENROLL_LINKED_CSN_HX](ENROLL_LINKED_CSN_HX.md) | `HX_LINKED_ENC_CSN` | low |
| [EPA_INFO](EPA_INFO.md) | `PAT_EPA_ENC_CSN_ID` | low |
| [EPA_INFO_2](EPA_INFO_2.md) | `ELIG_PAT_ENC_CSN_ID` | low |
| [EPISODE_2](EPISODE_2.md) | `CRT_PAT_ENC_CSN_ID` | low |
| [EPT_CARE_TEAMS](EPT_CARE_TEAMS.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_INSTANT_ORDER_POLICY](EPT_INSTANT_ORDER_POLICY.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_ORD_SPEC_QUESN](EPT_ORD_SPEC_QUESN.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_OR_PAT_SURG_PREORD](EPT_OR_PAT_SURG_PREORD.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_OR_PAT_SURG_PREORD_NC](EPT_OR_PAT_SURG_PREORD_NC.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_SEL_SMARTSETS](EPT_SEL_SMARTSETS.md) | `PAT_ENC_CSN_ID` | high |
| [EPT_TEAM_AUDIT](EPT_TEAM_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [EVENT_NOTIF_HX](EVENT_NOTIF_HX.md) | `PAT_ENC_CSN_ID` | high |
| [EVENT_NOT_HX_FAC](EVENT_NOT_HX_FAC.md) | `PAT_ENC_CSN_ID` | high |
| [EVENT_NOT_HX_POOLS](EVENT_NOT_HX_POOLS.md) | `PAT_ENC_CSN_ID` | high |
| [EVENT_NOT_HX_PROV](EVENT_NOT_HX_PROV.md) | `PAT_ENC_CSN_ID` | high |
| [EXCUSE_TEMPLATE](EXCUSE_TEMPLATE.md) | `PAT_ENC_CSN_ID` | high |
| [EXCUSE_TEMPLATE_DATA](EXCUSE_TEMPLATE_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [EXCUSE_TEMPLATE_LQL](EXCUSE_TEMPLATE_LQL.md) | `PAT_ENC_CSN_ID` | high |
| [EXCUSE_TEMPLT_QUESNS](EXCUSE_TEMPLT_QUESNS.md) | `PAT_ENC_CSN_ID` | high |
| [EXPECTED_DISCHARGE_HX](EXPECTED_DISCHARGE_HX.md) | `PAT_ENC_CSN_ID` | high |
| [EXPECTED_LOS_HISTORY](EXPECTED_LOS_HISTORY.md) | `PAT_ENC_CSN_ID` | high |
| [EXPECT_DISCH_DISP_HX](EXPECT_DISCH_DISP_HX.md) | `PAT_ENC_CSN_ID` | high |
| [EXT_ELIG_STATUS](EXT_ELIG_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [EXT_ELIG_STATUS_1](EXT_ELIG_STATUS_1.md) | `PAT_ENC_CSN_ID` | high |
| [EXT_FORMULARY_ID](EXT_FORMULARY_ID.md) | `PAT_ENC_CSN_ID` | high |
| [EXT_GUARANTOR_DATA](EXT_GUARANTOR_DATA.md) | `EXT_GUAR_PAT_ENC_CSN_ID` | low |
| [EXT_PHARM_TYPE_COVERED](EXT_PHARM_TYPE_COVERED.md) | `PAT_ENC_CSN_ID` | high |
| [EXT_PHARM_TYPE_NONCVRD](EXT_PHARM_TYPE_NONCVRD.md) | `PAT_ENC_CSN_ID` | high |
| [FAC_CHG_AI_RUN_INFO](FAC_CHG_AI_RUN_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [FAC_CHG_OVERRIDE](FAC_CHG_OVERRIDE.md) | `PAT_ENC_CSN_ID` | high |
| [FAC_CHG_RULE_SCORE](FAC_CHG_RULE_SCORE.md) | `PAT_ENC_CSN_ID` | high |
| [FAMILY_HX](FAMILY_HX.md) | `PAT_ENC_CSN_ID` | high |
| [FAMILY_HX_STATUS](FAMILY_HX_STATUS.md) | `HX_LNK_ENC_CSN` | low |
| [FAMILY_HX_STATUS](FAMILY_HX_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [FAM_DOC_PATS](FAM_DOC_PATS.md) | `LINKED_PAT_ENC_CSN_ID` | low |
| [FAM_HX_PAT_ONLY](FAM_HX_PAT_ONLY.md) | `PAT_ENC_CSN_ID` | high |
| [FAM_PAT_ENC_RELATIONLIST](FAM_PAT_ENC_RELATIONLIST.md) | `PAT_ENC_CSN_ID` | high |
| [FAM_PAT_ENC_RELATIONSHIPS](FAM_PAT_ENC_RELATIONSHIPS.md) | `PAT_ENC_CSN_ID` | high |
| [FB_DISMISS_QUESTIONNAIRE](FB_DISMISS_QUESTIONNAIRE.md) | `PAT_ENC_CSN_ID` | high |
| [FCC_RULES_AUDIT](FCC_RULES_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [FCC_SCORE_AUDIT](FCC_SCORE_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [FILED_HNO_ID](FILED_HNO_ID.md) | `PAT_ENC_CSN_ID` | high |
| [FIRST_CALL_AUDIT](FIRST_CALL_AUDIT.md) | `PAT_ENC_CSN_ID` | high |
| [FORM_REPRINT_HX](FORM_REPRINT_HX.md) | `PAT_ENC_CSN_ID` | high |
| [FRONT_END_PMT_COLL_HX](FRONT_END_PMT_COLL_HX.md) | `PAT_ENC_CSN_ID` | high |
| [HAR_ALL](HAR_ALL.md) | `PRIM_ENC_CSN_ID` | low |
| [HEALTH_PLAN_DX_CODING](HEALTH_PLAN_DX_CODING.md) | `RA_SOURCE_PAT_ENC_CSN_ID` | low |
| [HELD_ORDERS_REVIEW](HELD_ORDERS_REVIEW.md) | `PAT_ENC_CSN_ID` | high |
| [HH_ADMN_PAT_DATA](HH_ADMN_PAT_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [HH_DATASET_INFO](HH_DATASET_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [HH_ENC_ENCODER_HX](HH_ENC_ENCODER_HX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_EPSD_INFO](HH_EPSD_INFO.md) | `DISCH_SOURCE_PAT_ENC_CSN_ID` | low |
| [HH_EPSD_INFO](HH_EPSD_INFO.md) | `INTAKE_PAT_ENC_CSN_ID` | low |
| [HH_EVV_DATA](HH_EVV_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [HH_FORMS_ACCESSED](HH_FORMS_ACCESSED.md) | `PAT_ENC_CSN_ID` | high |
| [HH_MEDS_ADDL_INFO](HH_MEDS_ADDL_INFO.md) | `PAT_ENC_CSN` | high |
| [HH_MED_ORD_POC_STATUS](HH_MED_ORD_POC_STATUS.md) | `PAT_ENC_CSN_ID` | high |
| [HH_OASIS_ICD10_DX](HH_OASIS_ICD10_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_OASIS_INFO](HH_OASIS_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_ADDEND_EDTS](HH_PAT_ADDEND_EDTS.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_CASE_MIX_DX](HH_PAT_CASE_MIX_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_CERT_PERIOD](HH_PAT_CERT_PERIOD.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_CHARGE](HH_PAT_CHARGE.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_CSMX_OTH_DX](HH_PAT_CSMX_OTH_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_DSCH_INSTR](HH_PAT_DSCH_INSTR.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_DSCH_SUM](HH_PAT_DSCH_SUM.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_ENC](HH_PAT_ENC.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_ENC_ACTIONS](HH_PAT_ENC_ACTIONS.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_ENC_NAR](HH_PAT_ENC_NAR.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_FIN_FACTORS](HH_PAT_FIN_FACTORS.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_FUNC_LIMIT](HH_PAT_FUNC_LIMIT.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_HOMEBOUND](HH_PAT_HOMEBOUND.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_INSTRUCTION](HH_PAT_INSTRUCTION.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_IP_DX](HH_PAT_IP_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_IP_FACILITY](HH_PAT_IP_FACILITY.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_IP_PROC](HH_PAT_IP_PROC.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_MENTAL_STAT](HH_PAT_MENTAL_STAT.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_NOTES](HH_PAT_NOTES.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_NUTR_REQ](HH_PAT_NUTR_REQ.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_OTHER_DX](HH_PAT_OTHER_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_PAYMENT_DX](HH_PAT_PAYMENT_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_PAYMNT_SRC](HH_PAT_PAYMNT_SRC.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_PRIOR_COND](HH_PAT_PRIOR_COND.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_REG_CHG_DX](HH_PAT_REG_CHG_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PAT_SAFETY_MSRS](HH_PAT_SAFETY_MSRS.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PBLST_HX_WND_ED](HH_PBLST_HX_WND_ED.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PBLST_INFO](HH_PBLST_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [HH_PBLST_WOUNDS](HH_PBLST_WOUNDS.md) | `PAT_ENC_CSN_ID` | high |
| [HL_REQ_ADDL_LINKED_ENC](HL_REQ_ADDL_LINKED_ENC.md) | `PAT_ENC_CSN_ID` | high |
| [HL_REQ_INFO](HL_REQ_INFO.md) | `REQ_ADMISSION_PAT_ENC_CSN_ID` | low |
| [HL_REQ_INFO](HL_REQ_INFO.md) | `REQ_END_APPT_PAT_ENC_CSN_ID` | low |
| [HL_REQ_INFO](HL_REQ_INFO.md) | `REQ_START_APPT_PAT_ENC_CSN_ID` | low |
| [HM_ENC_DATE](HM_ENC_DATE.md) | `HM_LET_PAT_ENC_CSN_ID` | low |
| [HNO_INFO](HNO_INFO.md) | `PAT_ENC_CSN_ID` | high |
| [HNO_INFO_2](HNO_INFO_2.md) | `RFL_LETTER_ENC_CSN` | low |
| [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | `PAT_ENC_CSN_ID` | high |
| [HOMUNCULUS_INP_DATA](HOMUNCULUS_INP_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [HOMUNCULUS_PAT_DATA](HOMUNCULUS_PAT_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [HOSPICE_CODED_DX](HOSPICE_CODED_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HOSPICE_DX](HOSPICE_DX.md) | `PAT_ENC_CSN_ID` | high |
| [HOSPICE_DX_HX](HOSPICE_DX_HX.md) | `PAT_ENC_CSN_ID` | high |
| [HOSP_PROC_CODE_ID](HOSP_PROC_CODE_ID.md) | `PAT_ENC_CSN_ID` | high |
| [HPF_ADMIT_DIAG](HPF_ADMIT_DIAG.md) | `PAT_ENC_CSN_ID` | high |
| [HPF_TRTMNT_TEAM](HPF_TRTMNT_TEAM.md) | `PAT_ENC_CSN_ID` | high |
| [HSC_SPEC_INFO](HSC_SPEC_INFO.md) | `PAT_CSN` | low |
| [HSP_ACCT_PAT_CSN](HSP_ACCT_PAT_CSN.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_ADMIT_DIAG](HSP_ADMIT_DIAG.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_ADMIT_PROC](HSP_ADMIT_PROC.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_ATND_PROV](HSP_ATND_PROV.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_DISCH_DIAG](HSP_DISCH_DIAG.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_HOME_LINK_VISITS](HSP_HOME_LINK_VISITS.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_PREADM_CONFRM](HSP_PREADM_CONFRM.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_PREADM_TEST](HSP_PREADM_TEST.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_PRE_AR_TX](HSP_PRE_AR_TX.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md) | `PAT_ENC_CSN_ID` | high |
| [HSP_TRTMT_TEAM](HSP_TRTMT_TEAM.md) | `PAT_ENC_CSN_ID` | high |
| [HV_ORDER_PROC](HV_ORDER_PROC.md) | `PAT_ENC_CSN_ID` | high |
| [HX_QNR_PT_DATA](HX_QNR_PT_DATA.md) | `PAT_ENC_CSN_ID` | high |
| [IB_MESSAGES](IB_MESSAGES.md) | `PAT_ENC_CSN_ID` | high |
| [IB_MESSAGE_PAT_ENC](IB_MESSAGE_PAT_ENC.md) | `PAT_ENC_CSN_ID` | high |
| [IHS_ELIGIBILITY_REASONS](IHS_ELIGIBILITY_REASONS.md) | `PAT_ENC_CSN_ID` | high |
| [ILLICIT_DRUG_TYPES](ILLICIT_DRUG_TYPES.md) | `PAT_ENC_CSN_ID` | high |
| [IMMUNE_HISTORY](IMMUNE_HISTORY.md) | `IMMNZTN_HX_ENC_CSN` | low |
| [IMPLANT_OT](IMPLANT_OT.md) | `PAT_ENC_CSN_ID` | high |
| [INCOMPLETE_NOTE_EPT](INCOMPLETE_NOTE_EPT.md) | `PAT_ENC_CSN_ID` | high |
| [INFECTIONS](INFECTIONS.md) | `PAT_ENC_CSN_ID` | high |

_… and 391 more (see `data/references.jsonl`)._

