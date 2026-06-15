# CLAIM_INFO

> This table contains information from claim info records for Hospital and Professional Billing.

**Overflow family:** [CLAIM_INFO_3](CLAIM_INFO_3.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 138  
**Org-specific columns:** 18  
**Joined by:** 467 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK | The unique ID for the claim information record. |
| 2 | `CLAIM_NAME` | VARCHAR |  | The description of the claim record. |
| 3 | `ACCOUNT_ID` | NUMERIC | FK→ | The billing system accounts receivable account ID associated with this claim. |
| 4 | `CLAIM_TYPE_C_NAME` | VARCHAR | org | The claim type category of the claim. Identifies whether the claim was filed as a workers' compensation or commercial claim. |
| 5 | `USER_ID` | VARCHAR | FK→ | The ID of the staff member who entered the claim into the system. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ENTRY_DATE` | DATETIME |  | The date on which this claim was entered into the system. |
| 8 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID of the coverage used for this claim. This column can be used to report on coverages that are associated with a hospital account. |
| 9 | `ADMIT_DATETIME` | DATETIME (Local) |  | The admission date and time for the patient encounter associated with the claim. |
| 10 | `CLM_PAT_STATUS_C_NAME` | VARCHAR | org | The patient status category ID for the patient for whom this claim was filed. |
| 11 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The admission source (e.g., physician referral, clinic referral, Health Maintenance Organization (HMO) referral, transfer from a hospital, transfer from a skilled nursing facility, emergency room, court/law enforcement, information not available) for the encounter associated with this claim. |
| 13 | `ADMISSION_TYPE_C_NAME` | VARCHAR | org | The admission type for the patient encounter associated with this claim (e.g., emergency, urgent, elective, newborn, trauma center, information not available). |
| 14 | `ADMIT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 15 | `ILL_INJ_LMP_C_NAME` | VARCHAR |  | The category type identifying the claim as resulting from illness, injury or pregnancy (e.g., illness, accident (injury), pregnancy (last menstrual period, or LMP)). |
| 16 | `REL_CONDITION_C_NAME` | VARCHAR | org | The related condition for the claim (e.g. Auto, Other Party Liability, Other Accident Related Injury, Patient Employment, Crime Victim). |
| 17 | `DOC_CTRL_NUM` | VARCHAR |  | The document control number (DCN) for the claim record. |
| 18 | `INJURY_DATETIME` | DATETIME (Local) |  | The date and time on which the injury resulting in the claim occurred. |
| 19 | `ACCIDENT_TYPE_C_NAME` | VARCHAR | org | The accident type for the injury resulting in the claim (e.g., Workers' Compensation, Automobile). |
| 20 | `IS_EPSDT_YN` | VARCHAR |  | This is a yes/no flag indicating whether or not the patient is being seen for an Early Periodic Screening Diagnosis and Treatment (EPSDT) program. |
| 21 | `EPSDT_CODE_C_NAME` | VARCHAR | org | Early Periodic Screening and Diagnosis Treatment (EPSDT) program value. |
| 22 | `WC_CLAIM_NUM` | VARCHAR |  | Workers' Comp Claim Number for the claim record. |
| 23 | `WC_EMPLOYER_ID` | VARCHAR |  | The ID of the employer associated with a Workers' Comp claim. |
| 24 | `WC_EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 25 | `TRAN_CODE_C_NAME` | VARCHAR | org | Ambulance transport code. |
| 26 | `TRAN_REASON_C_NAME` | VARCHAR | org | Ambulance transport reason code. |
| 27 | `TRAN_DIST` | NUMERIC |  | Ambulance transport distance. |
| 28 | `CLM_LOGIN_SA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 29 | `ILL_INJ_LMP_DT` | DATETIME |  | The date of the onset of illness, the occurrence of the injury, or the patient's last menstrual period (related to pregnancy). |
| 30 | `AUTO_ACDNT_STATE_C_NAME` | VARCHAR | org | Auto accident State. |
| 31 | `EMPY_RELATED_YN` | VARCHAR |  | Indicates whether patient's condition is related to employment. |
| 32 | `FIRST_CONSULT_DT` | DATETIME |  | First consult date. |
| 33 | `PAT_CHIEF_COMPLAINT` | VARCHAR |  | Patients chief complaint. |
| 34 | `EMERG_YN` | VARCHAR |  | Indicates whether the procedure is related to an emergency. |
| 35 | `LAST_WORKED_DT` | DATETIME |  | Date last worked. |
| 36 | `RETURN_TO_WORK_DT` | DATETIME |  | Return to work date. |
| 37 | `DISCHARGE_DT` | DATETIME |  | Discharge date. |
| 38 | `OUTSIDE_LAB_NAME_C_NAME` | VARCHAR | org | Outside lab name. |
| 39 | `HLTH_APPR_SCRN_YN` | VARCHAR |  | Routine health appraisal/screening procedure. |
| 40 | `SIG_ON_FILE_YN` | VARCHAR |  | Signature on file? |
| 41 | `WK_COMP_CLAIM_NUM` | VARCHAR |  | Workers' Comp claim number. |
| 42 | `WK_COMP_INJ_DESC` | VARCHAR |  | Workers' Comp injury description. |
| 43 | `WK_COMP_APRV_CODE` | VARCHAR |  | Workers' Comp approval code. |
| 44 | `WK_COMP_MED_RLS_DT` | DATETIME |  | Workers' Comp medical release date. |
| 45 | `DF_DELAY_RSN_CODE_C_NAME` | VARCHAR | org | Default delay reason code. |
| 46 | `FIRST_NEXT_VISIT_C_NAME` | VARCHAR |  | First/subsequent visit indicator. |
| 47 | `MED_HX_SOC_WORKER` | VARCHAR |  | Social worker associated with this visit. |
| 48 | `MED_HX_PSYCHOLOGIST` | VARCHAR |  | Psychologist associated with this visit. |
| 49 | `MED_HX_SUP_PROV` | VARCHAR |  | Supervising medical doctor for this visit. |
| 50 | `MED_HX_COUNSELOR` | VARCHAR |  | Counselor associated with this visit. |
| 51 | `HDH_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the health and developmental history assessment. |
| 52 | `PHY_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the physical assessment. |
| 53 | `PHY_EXAM_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the physical assessment. |
| 54 | `VISION_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the vision assessment. |
| 55 | `VISION_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the vision assessment. |
| 56 | `HEARING_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the hearing assessment. |
| 57 | `HEARING_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the hearing assessment. |
| 58 | `DEV_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the developmental assessment. |
| 59 | `DEV_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the developmental assessment. |
| 60 | `NUTRI_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the nutritional assessment. |
| 61 | `NUTRI_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the nutritional assessment. |
| 62 | `OTHER_TREATMNT_DT` | DATETIME |  | Stores date of other treatment. |
| 63 | `HOSPITAL_NAME` | VARCHAR |  | Name of the hospital where the patient was admitted. |
| 64 | `HOSPITAL_ADDRESS` | VARCHAR |  | The street address of the hospital where the patient was admitted. |
| 65 | `HOSPITAL_CITY` | VARCHAR |  | The city where the hospital to which the patient was admitted is located. |
| 66 | `HOSPITAL_STATE_C_NAME` | VARCHAR |  | The state where the hospital to which the patient was admitted is located. |
| 67 | `HOSPITAL_ZIP` | VARCHAR |  | The ZIP of the hospital to which the patient was admitted. |
| 68 | `HOSP_REQ_YN` | VARCHAR |  | Flag indicating whether or not hospitalization is required. |
| 69 | `ADV_RET_WORK_YN` | VARCHAR |  | Flag to indicate whether a patient was advised to return to work. |
| 70 | `ADV_RET_WORK_DT` | DATETIME |  | The date that patient was advised to return to work. |
| 71 | `REF_PHYS_NAME` | VARCHAR |  | Stores the referring physician's name. |
| 72 | `REF_PHYS_ADDR` | VARCHAR |  | Stores the referring physician's address. |
| 73 | `REF_PHYS_CITY` | VARCHAR |  | Stores the referring physician's city. |
| 74 | `REF_PHYS_STATE_C_NAME` | VARCHAR |  | Stores the referring physician's state. |
| 75 | `REF_PHYS_ZIP` | VARCHAR |  | Stores the referring physician's ZIP code. |
| 76 | `REF_PHYS_SPEC_C_NAME` | VARCHAR | org | Stores referring physician's specialty. |
| 77 | `REF_PHYS_REASON_C_NAME` | VARCHAR | org | Stores the referring physician's reason for the referral. |
| 78 | `FIRST_TREAT_HOUR_TM` | DATETIME (Local) |  | First treatment hour. Some extensions add a value code to your claim if this item has a value. |
| 79 | `PAT_PREV_TREATED_YN` | VARCHAR |  | Is patient previously treated? |
| 80 | `IDE_NUM` | VARCHAR |  | Investigational Device Exemption Number. |
| 81 | `EST_DOB_DT` | DATETIME |  | The estimated date of delivery for the pregnancy. |
| 82 | `RESPONSIBLE_IND_YN` | VARCHAR |  | Indicate if the patient's condition is due to an accident or illness caused by another party. |
| 83 | `REFERRAL_SOURCE_ID` | VARCHAR |  | The referral source for the visit. |
| 84 | `REFERRAL_SOURCE_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 85 | `EMERGENCY_CODE_C_NAME` | VARCHAR |  | The Emergency Service Code for emergency room services. This field is required for Illinois Department of Public Aid claims for emergency related services. It will populate record EA0-05.0 in the Illinois Department of Public Aid NSF 2.00 electronic claim file and box 10b-other on the IDPA 2360 paper claim form. |
| 86 | `DISABILITY_LEVEL_C_NAME` | VARCHAR | org | The extent of the disability caused by the incident. |
| 87 | `DISABILITY_FROM_DT` | DATETIME |  | The date the disability started. |
| 88 | `DISABILITY_TO_DT` | DATETIME |  | The date the disability ended. |
| 89 | `OUTSIDE_LAB_YN` | VARCHAR |  | Indicate if lab services outside the provider's office are involved. |
| 90 | `OUTSIDE_LAB_CHARGE` | NUMERIC |  | The cost of services performed at the outside lab. |
| 91 | `FAM_PLANNING_YN` | VARCHAR |  | Indicate whether the patient is being seen for family planning care. |
| 92 | `SPECIAL_PROGRAM_C_NAME` | VARCHAR |  | The special program under which the services rendered to the patient were performed. |
| 93 | `PGM_FOR_HANDICAP_C_NAME` | VARCHAR |  | Indicates the patient's relationship to the sponsor for the program that benefits people with handicaps. |
| 94 | `EMPLOYER_LOB` | VARCHAR |  | A free text nature/line of business for the employer. |
| 95 | `OTH_INFO` | VARCHAR |  | Any additional free text information that should be recorded in conjunction with the claim. |
| 96 | `AUTH_DT` | DATETIME |  | Authorization date. |
| 97 | `CHIR_FIRST_TREAT_DT` | DATETIME |  | The initiation date of the course of treatment for chiropractic services. |
| 98 | `CHIR_X_RAY_DT` | DATETIME |  | The X-ray date for chiropractic services. |
| 99 | `NAT_OF_COND_C_NAME` | VARCHAR | org | Stores the nature of condition code for Spinal Manipulation. |
| 100 | `CHIR_ACUTE_MANI_DT` | DATETIME |  | Stores the acute manifestation date for the spinal manipulation therapy. |
| 101 | `HBG_HCT_TEST_INCL_C_NAME` | VARCHAR |  | Indicate whether hemoglobin/hematocrit (HGB/HCT) test is included. |
| 102 | `URINALYSIS_INCL_C_NAME` | VARCHAR |  | Indicate whether Urinalysis test is included. |
| 103 | `TUBERCULOSIS_INCL_C_NAME` | VARCHAR |  | Indicate whether tuberculosis test is included. |
| 104 | `LEAD_TEST_INCL_C_NAME` | VARCHAR |  | Indicate whether lead test is included. |
| 105 | `SICKLE_CELL_INCL_C_NAME` | VARCHAR |  | Indicate whether sickle-cell test is included. |
| 106 | `IMMNZTN_INCL_C_NAME` | VARCHAR |  | The exam code for the immunizations. |
| 107 | `CARDIO_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the cardiovascular assessment. |
| 108 | `CARDIO_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the cardiovascular assessment. |
| 109 | `URINARY_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the genital/urinary tract assessment. |
| 110 | `URINARY_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the genital/urinary tract assessment. |
| 111 | `DIABETE_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the diabetes assessment. |
| 112 | `DIABETE_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the diabetes assessment. |
| 113 | `DENTAL_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for the dental assessment. |
| 114 | `DENTAL_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the dental assessment. |
| 115 | `IMMNZTN_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for the immunizations. |
| 116 | `EDU_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for health education. |
| 117 | `EDU_RFL_CODE_C_NAME` | VARCHAR |  | The referral code for health education. |
| 118 | `ONLY_CAUSE_YN` | VARCHAR |  | Flag to distinguish whether or not this injury is the only cause of the patient's condition. |
| 119 | `PAT_BURNED_YN` | VARCHAR |  | Flag to determine whether or not patient has been burned. |
| 120 | `XRAY_BY_WHOM` | VARCHAR |  | The name of the person or entity that performed x-rays. |
| 121 | `WC_XRAY_DT` | DATETIME |  | The date comparative x-rays were taken. |
| 122 | `POLIO_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Polio. |
| 123 | `DPT_TD_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Diphtheria, pertussis, and tetanus (DPT)/tetanus and diphtheria (DT). |
| 124 | `MEASLES_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Measles. |
| 125 | `MUMPS_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Mumps. |
| 126 | `RUBELLA_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Rubella. |
| 127 | `HIB_IMMNZTN_C_NAME` | VARCHAR |  | The immunization status for Haemophilus influenzae type B (HIB). |
| 128 | `CHAMP_NONAVAIL_YN` | VARCHAR |  | Indicate if the provider has a signed Tricare statement of non-availability on file indicating that the services associated with this claim were not available at a military treatment facility. |
| 129 | `CHAMP_NONAV_STMT_NO` | VARCHAR |  | The number of the Tricare non-availability statement. |
| 130 | `CHAMPUS_ORG` | VARCHAR |  | Tricare Organization. |
| 131 | `CHAMPUS_STATION` | VARCHAR |  | Tricare Station. |
| 132 | `CHAMP_MILIT_ACC_YN` | VARCHAR |  | Indicate if the services performed were treatment as a result of a military accident. |
| 133 | `ALTERNATE_CLM_ID` | VARCHAR |  | Alternate Claim ID. |
| 134 | `REF_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 135 | `MC_CLAIMS_WKFLOW_C_NAME` | VARCHAR | org | Indicates the workflow associated with the claim (shadow claims, Accounts Payable claims, export only claims, etc.) |
| 136 | `CLM_SENSITIVITY_C_NAME` | VARCHAR | org | Indicates the sensitivity type of the claim. |
| 137 | `PLACE_OF_SERVICE_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 138 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

## Joined in — referenced by (467)

| From | Column | Confidence |
|------|--------|------------|
| [AMBU_DROP_ADDR](AMBU_DROP_ADDR.md) | `CLAIM_ID` | medium |
| [AMBU_PICK_ADDR](AMBU_PICK_ADDR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM](AP_CLAIM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_2](AP_CLAIM_2.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_3](AP_CLAIM_3.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_4](AP_CLAIM_4.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_ANSI_DATA](AP_CLAIM_ANSI_DATA.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_ATTACHMENTS](AP_CLAIM_ATTACHMENTS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_AUTH_ASGN](AP_CLAIM_AUTH_ASGN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_AUTH_ASGN_AUTHS](AP_CLAIM_AUTH_ASGN_AUTHS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_AUTH_ASGN_RFLS](AP_CLAIM_AUTH_ASGN_RFLS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_BLK_DATA_LOG_HX](AP_CLAIM_BLK_DATA_LOG_HX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_CDEDIT_HX](AP_CLAIM_CDEDIT_HX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_CHANGE_HX](AP_CLAIM_CHANGE_HX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_CLIN_FILTER_RSN](AP_CLAIM_CLIN_FILTER_RSN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_COMP_CONTRACTS](AP_CLAIM_COMP_CONTRACTS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_COND_CODE](AP_CLAIM_COND_CODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_DX](AP_CLAIM_DX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_ECODES](AP_CLAIM_ECODES.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_EOB_CD](AP_CLAIM_EOB_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_EOB_CD_RS](AP_CLAIM_EOB_CD_RS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_EXPORT_HISTORY](AP_CLAIM_EXPORT_HISTORY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_HELD_FROM_AP_RSN](AP_CLAIM_HELD_FROM_AP_RSN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_HLTH_ERR](AP_CLAIM_HLTH_ERR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_ICD_PROC](AP_CLAIM_ICD_PROC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_ICIV_RSN](AP_CLAIM_ICIV_RSN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ACE_DX_DISP](AP_CLAIM_IF_ACE_DX_DISP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ACE_DX_ERR](AP_CLAIM_IF_ACE_DX_ERR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ACE_DX_NERR](AP_CLAIM_IF_ACE_DX_NERR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ACE_OP_MAI](AP_CLAIM_IF_ACE_OP_MAI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ADMIT_DX_EDIT](AP_CLAIM_IF_ADMIT_DX_EDIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ADM_DX_ECODE](AP_CLAIM_IF_ADM_DX_ECODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_CCI_CD](AP_CLAIM_IF_AE_CCI_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_CCI_CNT](AP_CLAIM_IF_AE_CCI_CNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_ERR_CD](AP_CLAIM_IF_AE_ERR_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_FCLP](AP_CLAIM_IF_AE_FCLP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_FPC](AP_CLAIM_IF_AE_FPC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_MOD_CD](AP_CLAIM_IF_AE_MOD_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_OCE_CD](AP_CLAIM_IF_AE_OCE_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_OCE_CNT](AP_CLAIM_IF_AE_OCE_CNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_OCE_IND](AP_CLAIM_IF_AE_OCE_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_SCLP](AP_CLAIM_IF_AE_SCLP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AE_SPC](AP_CLAIM_IF_AE_SPC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AGE_EDIT_IND](AP_CLAIM_IF_AGE_EDIT_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_AGE_SX_DX_FLG](AP_CLAIM_IF_AGE_SX_DX_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ANALYZER](AP_CLAIM_IF_ANALYZER.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_BILAT_CD_IND](AP_CLAIM_IF_BILAT_CD_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_BILTRL_DISCNT](AP_CLAIM_IF_BILTRL_DISCNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_CC_MCC_IND](AP_CLAIM_IF_CC_MCC_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_CLAIM_EDIT](AP_CLAIM_IF_CLAIM_EDIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_CLM_EDIT_DESC](AP_CLAIM_IF_CLM_EDIT_DESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_CLSD_BPSY_CD](AP_CLAIM_IF_CLSD_BPSY_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_CODES](AP_CLAIM_IF_CODES.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DIAL_ADJ_RATE](AP_CLAIM_IF_DIAL_ADJ_RATE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DUP_DX_FLAG](AP_CLAIM_IF_DUP_DX_FLAG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DUP_SEC_DX](AP_CLAIM_IF_DUP_SEC_DX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_ADMIT_ROM](AP_CLAIM_IF_DX_ADMIT_ROM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_ADMIT_SOI](AP_CLAIM_IF_DX_ADMIT_SOI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_AF_DRG_FLG](AP_CLAIM_IF_DX_AF_DRG_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_AF_HAC_DRG](AP_CLAIM_IF_DX_AF_HAC_DRG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_AF_HAC_ROM](AP_CLAIM_IF_DX_AF_HAC_ROM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_AF_HAC_SOI](AP_CLAIM_IF_DX_AF_HAC_SOI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_COMP_IND](AP_CLAIM_IF_DX_COMP_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_EDIT](AP_CLAIM_IF_DX_EDIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_EDIT_DESC](AP_CLAIM_IF_DX_EDIT_DESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_EXCL_HAC](AP_CLAIM_IF_DX_EXCL_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_AJ_ROM](AP_CLAIM_IF_DX_HAC_AJ_ROM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_AJ_SOI](AP_CLAIM_IF_DX_HAC_AJ_SOI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_ASGN](AP_CLAIM_IF_DX_HAC_ASGN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_CAT](AP_CLAIM_IF_DX_HAC_CAT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_IND](AP_CLAIM_IF_DX_HAC_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_ROM_FL](AP_CLAIM_IF_DX_HAC_ROM_FL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_SOI_FL](AP_CLAIM_IF_DX_HAC_SOI_FL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_HAC_USAGE](AP_CLAIM_IF_DX_HAC_USAGE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_INVALID](AP_CLAIM_IF_DX_INVALID.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_POA_BYPASS](AP_CLAIM_IF_DX_POA_BYPASS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_POA_ERR_CD](AP_CLAIM_IF_DX_POA_ERR_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_POA_USED](AP_CLAIM_IF_DX_POA_USED.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_PSCA](AP_CLAIM_IF_DX_PSCA.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_SUG_SURG](AP_CLAIM_IF_DX_SUG_SURG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_USED](AP_CLAIM_IF_DX_USED.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_USED_DESC](AP_CLAIM_IF_DX_USED_DESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_DX_USED_HAC](AP_CLAIM_IF_DX_USED_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_FIN_MCC_FLAG](AP_CLAIM_IF_FIN_MCC_FLAG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB3_NARRAY](AP_CLAIM_IF_GOB3_NARRAY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB3_ROM](AP_CLAIM_IF_GOB3_ROM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB3_ROM_IND](AP_CLAIM_IF_GOB3_ROM_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB3_SOI](AP_CLAIM_IF_GOB3_SOI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB3_SOI_IND](AP_CLAIM_IF_GOB3_SOI_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB4_NARRAY](AP_CLAIM_IF_GOB4_NARRAY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB4_ROM_IND](AP_CLAIM_IF_GOB4_ROM_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GOB4_SOI_IND](AP_CLAIM_IF_GOB4_SOI_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_APG_CAT](AP_CLAIM_IF_GRP_APG_CAT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_APG_CONS](AP_CLAIM_IF_GRP_APG_CONS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_APG_PACK](AP_CLAIM_IF_GRP_APG_PACK.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_APG_TYPE](AP_CLAIM_IF_GRP_APG_TYPE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_DX_HAC](AP_CLAIM_IF_GRP_DX_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_LNITM_VIS](AP_CLAIM_IF_GRP_LNITM_VIS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_PX_HAC](AP_CLAIM_IF_GRP_PX_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_RFV_DXEDD](AP_CLAIM_IF_GRP_RFV_DXEDD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_RFV_DXEDT](AP_CLAIM_IF_GRP_RFV_DXEDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_RFV_DXUSD](AP_CLAIM_IF_GRP_RFV_DXUSD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_RFV_DXUSE](AP_CLAIM_IF_GRP_RFV_DXUSE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_GRP_UNASGN_FL](AP_CLAIM_IF_GRP_UNASGN_FL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_HOSP_ACQ_CNDF](AP_CLAIM_IF_HOSP_ACQ_CNDF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_HOSP_ACQ_COND](AP_CLAIM_IF_HOSP_ACQ_COND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO](AP_CLAIM_IF_INFO.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO_2](AP_CLAIM_IF_INFO_2.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO_3](AP_CLAIM_IF_INFO_3.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO_4](AP_CLAIM_IF_INFO_4.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO_5](AP_CLAIM_IF_INFO_5.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INFO_MOE](AP_CLAIM_IF_INFO_MOE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INIT_MCC_FLAG](AP_CLAIM_IF_INIT_MCC_FLAG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_INVLD_PX_EDT](AP_CLAIM_IF_INVLD_PX_EDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_LNITM_ACT_FLG](AP_CLAIM_IF_LNITM_ACT_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_LN_340B_DSCNT](AP_CLAIM_IF_LN_340B_DSCNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_LN_PRVENT_SVC](AP_CLAIM_IF_LN_PRVENT_SVC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MCE_ERR_CODE](AP_CLAIM_IF_MCE_ERR_CODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MCE_ERR_COUNT](AP_CLAIM_IF_MCE_ERR_COUNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MED_SEC_PYR](AP_CLAIM_IF_MED_SEC_PYR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MED_VIS_DXSSF](AP_CLAIM_IF_MED_VIS_DXSSF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MODALITY_FACT](AP_CLAIM_IF_MODALITY_FACT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MODALTY_SEP](AP_CLAIM_IF_MODALTY_SEP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_MULT_PX_DSCNT](AP_CLAIM_IF_MULT_PX_DSCNT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_NDC_REIMB_IND](AP_CLAIM_IF_NDC_REIMB_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_NDC_REIMB_SEP](AP_CLAIM_IF_NDC_REIMB_SEP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_NEVER_PAY_FLG](AP_CLAIM_IF_NEVER_PAY_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_NONCVRD_CHGS](AP_CLAIM_IF_NONCVRD_CHGS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_NON_COVD_EDIT](AP_CLAIM_IF_NON_COVD_EDIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OLD_DIAL_PAY](AP_CLAIM_IF_OLD_DIAL_PAY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OLD_METHOD_SP](AP_CLAIM_IF_OLD_METHOD_SP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ONSET_FACTOR](AP_CLAIM_IF_ONSET_FACTOR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_ONSET_FACT_SP](AP_CLAIM_IF_ONSET_FACT_SP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OPR_ROOM_IND](AP_CLAIM_IF_OPR_ROOM_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_DX](AP_CLAIM_IF_OUT_DX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_ECODE](AP_CLAIM_IF_OUT_ECODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_ECODE_POA](AP_CLAIM_IF_OUT_ECODE_POA.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_ICDPX_DT](AP_CLAIM_IF_OUT_ICDPX_DT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_NDC](AP_CLAIM_IF_OUT_NDC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_NDC_UNITS](AP_CLAIM_IF_OUT_NDC_UNITS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_OCC_CODE](AP_CLAIM_IF_OUT_OCC_CODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_OCC_DATE](AP_CLAIM_IF_OUT_OCC_DATE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_OCC_SFD](AP_CLAIM_IF_OUT_OCC_SFD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_OCC_SPAN](AP_CLAIM_IF_OUT_OCC_SPAN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_OCC_STD](AP_CLAIM_IF_OUT_OCC_STD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_POA](AP_CLAIM_IF_OUT_POA.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_PX](AP_CLAIM_IF_OUT_PX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_RFV_DX](AP_CLAIM_IF_OUT_RFV_DX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SUMM_CODE](AP_CLAIM_IF_OUT_SUMM_CODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SUMM_PRC](AP_CLAIM_IF_OUT_SUMM_PRC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SUMM_SVC](AP_CLAIM_IF_OUT_SUMM_SVC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_CHRGS](AP_CLAIM_IF_OUT_SVC_CHRGS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_DATE](AP_CLAIM_IF_OUT_SVC_DATE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_HCPCS](AP_CLAIM_IF_OUT_SVC_HCPCS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_MODS](AP_CLAIM_IF_OUT_SVC_MODS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_PT](AP_CLAIM_IF_OUT_SVC_PT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_REV](AP_CLAIM_IF_OUT_SVC_REV.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_TO_DT](AP_CLAIM_IF_OUT_SVC_TO_DT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_SVC_UNITS](AP_CLAIM_IF_OUT_SVC_UNITS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_VAL_AMT](AP_CLAIM_IF_OUT_VAL_AMT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_OUT_VAL_CODE](AP_CLAIM_IF_OUT_VAL_CODE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PAT_RATE](AP_CLAIM_IF_PAT_RATE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PAT_RATE_SEP](AP_CLAIM_IF_PAT_RATE_SEP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PAYMENT_SEP](AP_CLAIM_IF_PAYMENT_SEP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_POA_FLG_ERR](AP_CLAIM_IF_POA_FLG_ERR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_POB2_METHOD](AP_CLAIM_IF_POB2_METHOD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_ADDON_PMT](AP_CLAIM_IF_PRC_ADDON_PMT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_ADJ_EXTWT](AP_CLAIM_IF_PRC_ADJ_EXTWT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_ADJ_FLAG](AP_CLAIM_IF_PRC_ADJ_FLAG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_ADJ_WGHT](AP_CLAIM_IF_PRC_ADJ_WGHT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_AD_DX_EDT](AP_CLAIM_IF_PRC_AD_DX_EDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_APG_TYPE](AP_CLAIM_IF_PRC_APG_TYPE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_ASC_CVRD](AP_CLAIM_IF_PRC_ASC_CVRD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_EXT_WGHT](AP_CLAIM_IF_PRC_EXT_WGHT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_PMT_CONS](AP_CLAIM_IF_PRC_PMT_CONS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_PMT_MTHD](AP_CLAIM_IF_PRC_PMT_MTHD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRC_PMT_PACK](AP_CLAIM_IF_PRC_PMT_PACK.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRED_OUTL_MAP](AP_CLAIM_IF_PRED_OUTL_MAP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PRIN_DX_ERRS](AP_CLAIM_IF_PRIN_DX_ERRS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AFF_ROM_FL](AP_CLAIM_IF_PX_AFF_ROM_FL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AFF_SOI_FL](AP_CLAIM_IF_PX_AFF_SOI_FL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AF_DRG_FLG](AP_CLAIM_IF_PX_AF_DRG_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AF_HAC_DRG](AP_CLAIM_IF_PX_AF_HAC_DRG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AF_HAC_ROM](AP_CLAIM_IF_PX_AF_HAC_ROM.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_AF_HAC_SOI](AP_CLAIM_IF_PX_AF_HAC_SOI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_EDIT](AP_CLAIM_IF_PX_EDIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_EDIT_DESC](AP_CLAIM_IF_PX_EDIT_DESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_EXCL_GRP](AP_CLAIM_IF_PX_EXCL_GRP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_HAC_ASGN](AP_CLAIM_IF_PX_HAC_ASGN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_HAC_USE](AP_CLAIM_IF_PX_HAC_USE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_INCONW_LOS](AP_CLAIM_IF_PX_INCONW_LOS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_OP_RM_FLG](AP_CLAIM_IF_PX_OP_RM_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_SEQ](AP_CLAIM_IF_PX_SEQ.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_USE](AP_CLAIM_IF_PX_USE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_USED_DESC](AP_CLAIM_IF_PX_USED_DESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_PX_USED_HAC](AP_CLAIM_IF_PX_USED_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_QUAL_RED_FACT](AP_CLAIM_IF_QUAL_RED_FACT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_REPT_ANCLLRY](AP_CLAIM_IF_REPT_ANCLLRY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SEC_DX_SEQ](AP_CLAIM_IF_SEC_DX_SEQ.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SEX_CONFL_EDT](AP_CLAIM_IF_SEX_CONFL_EDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_STNDALN_FLG](AP_CLAIM_IF_STNDALN_FLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SUPPRESS_HAC](AP_CLAIM_IF_SUPPRESS_HAC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_APC](AP_CLAIM_IF_SVC_ACE_APC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_BMF](AP_CLAIM_IF_SVC_ACE_BMF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_CLN](AP_CLAIM_IF_SVC_ACE_CLN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_CMHCI](AP_CLAIM_IF_SVC_ACE_CMHCI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_DISC](AP_CLAIM_IF_SVC_ACE_DISC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_HPD](AP_CLAIM_IF_SVC_ACE_HPD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_MAXUN](AP_CLAIM_IF_SVC_ACE_MAXUN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_NO](AP_CLAIM_IF_SVC_ACE_NO.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_PAYUN](AP_CLAIM_IF_SVC_ACE_PAYUN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_PF](AP_CLAIM_IF_SVC_ACE_PF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_PMTST](AP_CLAIM_IF_SVC_ACE_PMTST.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_PVI](AP_CLAIM_IF_SVC_ACE_PVI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_ACE_PXERR](AP_CLAIM_IF_SVC_ACE_PXERR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_EAPG_PMT](AP_CLAIM_IF_SVC_EAPG_PMT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_FIN_HCPCS](AP_CLAIM_IF_SVC_FIN_HCPCS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_F_EAPG](AP_CLAIM_IF_SVC_F_EAPG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_F_EAPG_CT](AP_CLAIM_IF_SVC_F_EAPG_CT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_F_EAPG_TY](AP_CLAIM_IF_SVC_F_EAPG_TY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_F_EAPG_WT](AP_CLAIM_IF_SVC_F_EAPG_WT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GOB5_APG](AP_CLAIM_IF_SVC_GOB5_APG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_ACUIT](AP_CLAIM_IF_SVC_GRP_ACUIT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_AGDSC](AP_CLAIM_IF_SVC_GRP_AGDSC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_AGEDT](AP_CLAIM_IF_SVC_GRP_AGEDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_APC](AP_CLAIM_IF_SVC_GRP_APC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_APG](AP_CLAIM_IF_SVC_GRP_APG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_CIND](AP_CLAIM_IF_SVC_GRP_CIND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_CLNPX](AP_CLAIM_IF_SVC_GRP_CLNPX.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_DTFLG](AP_CLAIM_IF_SVC_GRP_DTFLG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_FEAPG](AP_CLAIM_IF_SVC_GRP_FEAPG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_HIPPS](AP_CLAIM_IF_SVC_GRP_HIPPS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD1](AP_CLAIM_IF_SVC_GRP_MOD1.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD1D](AP_CLAIM_IF_SVC_GRP_MOD1D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD2](AP_CLAIM_IF_SVC_GRP_MOD2.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD2D](AP_CLAIM_IF_SVC_GRP_MOD2D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD3](AP_CLAIM_IF_SVC_GRP_MOD3.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD3D](AP_CLAIM_IF_SVC_GRP_MOD3D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD4](AP_CLAIM_IF_SVC_GRP_MOD4.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD4D](AP_CLAIM_IF_SVC_GRP_MOD4D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD5](AP_CLAIM_IF_SVC_GRP_MOD5.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MOD5D](AP_CLAIM_IF_SVC_GRP_MOD5D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_MODJW](AP_CLAIM_IF_SVC_GRP_MODJW.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PIND](AP_CLAIM_IF_SVC_GRP_PIND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PKGDF](AP_CLAIM_IF_SVC_GRP_PKGDF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PMTST](AP_CLAIM_IF_SVC_GRP_PMTST.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PXED](AP_CLAIM_IF_SVC_GRP_PXED.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PXEDD](AP_CLAIM_IF_SVC_GRP_PXEDD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_PXER](AP_CLAIM_IF_SVC_GRP_PXER.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_RECUR](AP_CLAIM_IF_SVC_GRP_RECUR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_REL](AP_CLAIM_IF_SVC_GRP_REL.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_REL_D](AP_CLAIM_IF_SVC_GRP_REL_D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_REVE](AP_CLAIM_IF_SVC_GRP_REVE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_REVED](AP_CLAIM_IF_SVC_GRP_REVED.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_RT_CD](AP_CLAIM_IF_SVC_GRP_RT_CD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_RUG](AP_CLAIM_IF_SVC_GRP_RUG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_SAMEP](AP_CLAIM_IF_SVC_GRP_SAMEP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_SVCDD](AP_CLAIM_IF_SVC_GRP_SVCDD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_SVCDT](AP_CLAIM_IF_SVC_GRP_SVCDT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_VISMF](AP_CLAIM_IF_SVC_GRP_VISMF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_GRP_VISPW](AP_CLAIM_IF_SVC_GRP_VISPW.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_HIPPS_RUG](AP_CLAIM_IF_SVC_HIPPS_RUG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_LINE_IND](AP_CLAIM_IF_SVC_LINE_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_LN_IND_D](AP_CLAIM_IF_SVC_LN_IND_D.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_MCE_QOB](AP_CLAIM_IF_SVC_MCE_QOB.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_MCE_UNSCD](AP_CLAIM_IF_SVC_MCE_UNSCD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_METHD_IND](AP_CLAIM_IF_SVC_METHD_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_OA_VIS_TY](AP_CLAIM_IF_SVC_OA_VIS_TY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_OM_CAT](AP_CLAIM_IF_SVC_OM_CAT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_OUT_IND](AP_CLAIM_IF_SVC_OUT_IND.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PMT_PCT](AP_CLAIM_IF_SVC_PMT_PCT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_ALTP](AP_CLAIM_IF_SVC_PRC_ALTP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_APCWT](AP_CLAIM_IF_SVC_PRC_APCWT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_ASC](AP_CLAIM_IF_SVC_PRC_ASC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_COPAY](AP_CLAIM_IF_SVC_PRC_COPAY.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_CRR](AP_CLAIM_IF_SVC_PRC_CRR.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_CUTBA](AP_CLAIM_IF_SVC_PRC_CUTBA.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_DF](AP_CLAIM_IF_SVC_PRC_DF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_DMEMD](AP_CLAIM_IF_SVC_PRC_DMEMD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_FEESC](AP_CLAIM_IF_SVC_PRC_FEESC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_FSTYP](AP_CLAIM_IF_SVC_PRC_FSTYP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_LID](AP_CLAIM_IF_SVC_PRC_LID.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_LIOP](AP_CLAIM_IF_SVC_PRC_LIOP.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_LIPC](AP_CLAIM_IF_SVC_PRC_LIPC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_LN_RT](AP_CLAIM_IF_SVC_PRC_LN_RT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_MPDI](AP_CLAIM_IF_SVC_PRC_MPDI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_PMT](AP_CLAIM_IF_SVC_PRC_PMT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_PMTST](AP_CLAIM_IF_SVC_PRC_PMTST.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_PRICS](AP_CLAIM_IF_SVC_PRC_PRICS.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_PROCF](AP_CLAIM_IF_SVC_PRC_PROCF.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_PX_UN](AP_CLAIM_IF_SVC_PRC_PX_UN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_RATE](AP_CLAIM_IF_SVC_PRC_RATE.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_REIMB](AP_CLAIM_IF_SVC_PRC_REIMB.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_RETCD](AP_CLAIM_IF_SVC_PRC_RETCD.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_RSPC](AP_CLAIM_IF_SVC_PRC_RSPC.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_RUG](AP_CLAIM_IF_SVC_PRC_RUG.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_RUGRT](AP_CLAIM_IF_SVC_PRC_RUGRT.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_SPCLI](AP_CLAIM_IF_SVC_PRC_SPCLI.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_TOTLN](AP_CLAIM_IF_SVC_PRC_TOTLN.md) | `CLAIM_ID` | medium |
| [AP_CLAIM_IF_SVC_PRC_TOTOU](AP_CLAIM_IF_SVC_PRC_TOTOU.md) | `CLAIM_ID` | medium |

_… and 167 more (see `data/references.jsonl`)._

