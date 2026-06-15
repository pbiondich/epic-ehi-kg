# CLAIM_INFO2

> This table contains claims information from claim information (CLM) records for both Hospital and Professional Billing.

**Primary key:** `CLAIM_ID`  
**Columns:** 115  
**Org-specific columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique ID for the claim information record. |
| 2 | `CVR_NUM_TIMES_PREG` | INTEGER |  | Number of pregnancies, for contraceptive vaginal ring (CVR). |
| 3 | `CVR_NUM_BIRTHS` | INTEGER |  | Number of births, for contraceptive vaginal ring (CVR). |
| 4 | `NUM_LIVING_CHILDREN` | INTEGER |  | Number of living children, for contraceptive vaginal ring (CVR). |
| 5 | `CVR_VISIT_TYPE_C_NAME` | VARCHAR | org | Contraceptive vaginal ring (CVR) visit type. |
| 6 | `CVR_PRV_COUN_EDU_C_NAME` | VARCHAR | org | Provider of counseling and educational services for contraceptive vaginal ring (CVR). |
| 7 | `CVR_CONTRA_BEFORE_C_NAME` | VARCHAR | org | Contraceptive method, before visit for contraceptive vaginal ring (CVR). |
| 8 | `CVR_CONTRA_AFTER_C_NAME` | VARCHAR |  | Contraceptive method, after visit for contraceptive vaginal ring (CVR). |
| 9 | `CVR_REASON_CO_C_NAME` | VARCHAR | org | Reason for using no contraceptive method, for contraceptive vaginal ring (CVR). |
| 10 | `CVR_INT_CODE` | INTEGER |  | Internal use code, for contraceptive vaginal ring (CVR). |
| 11 | `CVR_STATUS_C_NAME` | VARCHAR | org | Contraceptive vaginal ring (CVR) status. |
| 12 | `TPR_INS_CODE_C_NAME` | VARCHAR | org | The Third Party Resource Insurance Code from Medicare. |
| 13 | `BLOOD_FURNISHED` | INTEGER |  | Pints of blood furnished. |
| 14 | `BLOOD_REPLACED` | INTEGER |  | Pints of blood replaced. |
| 15 | `BLOOD_NOT_REPLACED` | INTEGER |  | Pints of blood not replaced. |
| 16 | `BLOOD_DEDUCTIBLE` | INTEGER |  | The number of pints of blood that are deductible. |
| 17 | `PSROUR_APRV_IND_C_NAME` | VARCHAR |  | Professional Standards Review Organization Utilization Review (PSRO/UR) approval indicator. |
| 18 | `PSROUR_APRV_FROM_DT` | DATETIME |  | Professional Standards Review Organization Utilization Review (PSRO/UR) approval date. |
| 19 | `PSROUR_APRV_TO_DT` | DATETIME |  | Professional Standards Review Organization Utilization Review (PSRO/UR) approval expiry date. |
| 20 | `NUM_OF_GRACE_DAYS` | INTEGER |  | Number of grace days. |
| 21 | `TREAT_AUTH_CODE` | VARCHAR |  | Treatment authorization code. |
| 22 | `PART_A_EXHAUST_DT` | DATETIME |  | The date a patient's Medicare Part A benefits are exhausted. |
| 23 | `PAT_HEIGHT` | VARCHAR |  | Patient height in inches. |
| 24 | `PAT_WEIGHT` | VARCHAR |  | Patient weight in ounces. |
| 25 | `BIRTH_WEIGHT_WT` | NUMERIC |  | The patient's birth weight. |
| 26 | `SYSTOLIC_BP` | INTEGER |  | Blood pressure - systolic. |
| 27 | `DIASTOLIC_BP` | INTEGER |  | Blood pressure - diastolic. |
| 28 | `PAT_VISIT_TYPE_C_NAME` | VARCHAR | org | The patient's visit type for the State of California Child Health and Disability Prevention (CDHP) visit. |
| 29 | `PAT_SCREEN_TYPE_C_NAME` | VARCHAR | org | The type of screening performed during the State of California Child Health and Disability Prevention (CDHP) visit. |
| 30 | `WIC_STATUS_C_NAME` | VARCHAR |  | The patient's status in the Women, Infants, and Children (WIC) program. |
| 31 | `PAT_SCRN_PARTIAL_C_NAME` | VARCHAR |  | Indicates whether the State of California Child Health and Disability Prevention (CDHP) visit was a partial screening, or a recheck for an earlier screening. |
| 32 | `PAT_PRIOR_SCREEN_DT` | DATETIME |  | Date of prior screening. |
| 33 | `HEAD_START_YN` | VARCHAR |  | Indicate whether this patient has been referred by a Head Start or a State Preschool program for this State of California Child Health and Disability Prevention (CDHP) visit. |
| 34 | `HEAD_START_NUMBER` | VARCHAR |  | The 5 digit Head Start Grantee number, or the 11 digit State Preschool Project number for the program which referred the patient for this State of California Child Health and Disability Prevention (CHDP) visit. |
| 35 | `FOSTER_CHILD_YN` | VARCHAR |  | Indicates whether the patient is a foster child in the State of California Child Health and Disability Prevention (CHDP) program. |
| 36 | `TOBACCO_PASSIV_YN` | VARCHAR |  | Indicates whether tobacco exposure has occurred. |
| 37 | `TOBACCO_USAGE_YN` | VARCHAR |  | Indicated tobacco usage. |
| 38 | `TOBACCO_CNSL_YN` | VARCHAR |  | Indicates whether tobacco counseling was given. |
| 39 | `PAT_NEXT_VISIT_DT` | DATETIME |  | Next visit date. |
| 40 | `DENTAL_REFERRAL_YN` | VARCHAR |  | Dental referral. |
| 41 | `BLOOD_LEAD_REF_YN` | VARCHAR |  | Blood lead referrals. |
| 42 | `CONTRACEPTIVE_C_NAME` | VARCHAR | org | Contraceptive method the patient is using. |
| 43 | `CMN_ATTCH_TRNS_CD_C_NAME` | VARCHAR |  | Attachment transmission code for the External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 44 | `CMN_PUMP_NUM_C_NAME` | VARCHAR |  | Pump type - question 1 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 45 | `CMN_ADMIN_ROUT_C_NAME` | VARCHAR |  | Administration route - question 4 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 46 | `CMN_ADMIN_METH_C_NAME` | VARCHAR |  | Administration method - question 5 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 47 | `CMN_CANCER_PAIN_C_NAME` | VARCHAR |  | Whether the patient's pain cannot be managed by oral/transdermal narcotics - question 7 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 48 | `ASSUMED_CARE_DT` | DATETIME |  | The assumed care date of the claim. |
| 49 | `RELINQ_CARE_DT` | DATETIME |  | The date care was relinquished. |
| 50 | `DISCHARGE_HOUR_TM` | DATETIME (Local) |  | The time the patient was discharged from inpatient care. |
| 51 | `BILL_CLASS_C_NAME` | VARCHAR |  | The second digit for the UB bill type. |
| 52 | `PRINCIPAL_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 53 | `PRINCIPLE_PX_DESC` | VARCHAR |  | Principal International Classification of Diseases (ICD) procedure description. |
| 54 | `PRINCIPLE_PX_DT` | DATETIME |  | Principal International Classification of Diseases (ICD) procedure date. |
| 55 | `PRINCIPAL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 56 | `MEDICAID_CRN` | VARCHAR |  | The Medicaid Claim Rejection Number if this claim was rejected by Medicaid (used by some states). |
| 57 | `MEDICAID_RA` | VARCHAR |  | The Medicaid Remittance Advice cycle number in which this claim appeared if it was rejected by Medicaid (used by some states). |
| 58 | `MEDICAID_LT_CLM_CD` | VARCHAR |  | The exception code for the claim if the claim is being submitted to Medicaid after the normal filing time limit (used by some states). |
| 59 | `HEMATOCRIT_CT` | NUMERIC |  | The patient's hematocrit reading, between 18 and 72. |
| 60 | `HEMOGLOBIN_COUNT` | NUMERIC |  | The patient's hemoglobin reading to the nearest 0.1 gram, between 6.0 and 24.0. |
| 61 | `BLOOD_PRESSURE` | VARCHAR |  | Blood pressure. |
| 62 | `LAST_TREATMENT_DT` | DATETIME |  | The last treatment date. |
| 63 | `LMTD_RETURN_DT` | DATETIME |  | The date of limited return for Workers' Comp. |
| 64 | `COMP_XRAYS_YN` | VARCHAR |  | Indicate if comparative x-rays were taken for the amputation. |
| 65 | `AMPUTATION` | VARCHAR |  | Indicate what amputation was present. |
| 66 | `STUMP_CONDITION_C_NAME` | VARCHAR |  | The condition of the amputation stump. |
| 67 | `DISCHRG_CURED_DT` | DATETIME |  | The date the patient was discharged as cured. |
| 68 | `STOPPED_TREAT_DT` | DATETIME |  | The date the patient stopped treatment without an order. |
| 69 | `REFUSED_TREAT_DT` | DATETIME |  | The date the patient refused treatment. |
| 70 | `PROGNOSIS` | VARCHAR |  | The prognosis for the injury. |
| 71 | `FURTHER_TREATMENT_C_NAME` | VARCHAR |  | The likelihood of further treatment. |
| 72 | `TREATMENT_DESC` | VARCHAR |  | The description of the further treatment that should be given to the patient. |
| 73 | `HEALING_END_YN` | VARCHAR |  | Indicate if the healing period has ended. |
| 74 | `DISABLED_BODY_PART` | VARCHAR |  | The part of the body that was affected. |
| 75 | `BODY_PART_DISABLD_C_NAME` | VARCHAR | org | The affected body part. |
| 76 | `MIN_PERM_DISABILITY` | VARCHAR |  | The minimum permanent disability expected if healing has not ended. |
| 77 | `PERCENT_DISABILITY` | INTEGER |  | The percentage of disability. |
| 78 | `SURGERY_PERF_YN` | VARCHAR |  | Indicate if surgery was performed as a result of the injury. |
| 79 | `SURGERY_TYPE` | VARCHAR |  | The type of surgery performed. |
| 80 | `PREVIOUS_DISABILITY` | VARCHAR |  | The previous disability before the injury. |
| 81 | `CMN_INIT_CERT_DT` | DATETIME |  | Initial certification date for the External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 82 | `CMN_REV_CERT_DT` | DATETIME |  | Revised certification date for the External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 83 | `CMN_NUM_MONTH` | INTEGER |  | Estimated length of need, in months, for the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 84 | `CMN_HCPCS_CODE` | VARCHAR |  | Healthcare Common Procedure Coding System (HCPCS) code - question 2 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 85 | `CMN_NON_SPEC_CODE` | VARCHAR |  | Drug name for non-specific drug codes - question 3 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 86 | `CMN_DRG_INF_DUR` | INTEGER |  | Total duration of infusion, in hours, per 24-hour period - question 6 on the 09.02 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 87 | `CMN_ROUTE_0903_C_NAME` | VARCHAR | org | Administration route - question 3 on the 09.03 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 88 | `CMN_METHOD_0903_C_NAME` | VARCHAR | org | Administration method - question 4 on the 09.03 External Infusion Pump Certificate of Medical Necessity (CMN) form. |
| 89 | `PLACE_OF_INJURY_C_NAME` | VARCHAR | org | Place of injury. |
| 90 | `CITY` | VARCHAR |  | City in which the accident happened. |
| 91 | `ZIP` | VARCHAR |  | Zip code of the place where the accident happened. |
| 92 | `INFORMANT` | VARCHAR |  | Informant of the accident. |
| 93 | `ACCOMP_PERSON` | VARCHAR |  | The person the patient was accompanied by. |
| 94 | `POLICE_NOTIFIER` | VARCHAR |  | The person the police were notified by. |
| 95 | `ACC_COUNTY_C_NAME` | VARCHAR | org | Accident county. |
| 96 | `OUT_CLM_YN` | VARCHAR |  | Used to track charges and claims outside of the system. |
| 97 | `TPL_STATUS_C_NAME` | VARCHAR | org | The third party liability status. |
| 98 | `WCAB_NUM` | VARCHAR |  | The number assigned by the appeals board. |
| 99 | `CUMU_TRAUMA_YN` | VARCHAR |  | Indicates whether the claim is a cumulative trauma. |
| 100 | `AUTO_ACDNT_NUMBER` | VARCHAR |  | Auto Accident Claim Number. |
| 101 | `E_CODE_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 102 | `OTHER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 103 | `OPERATING_PHYSIC_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 104 | `ATTEND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 105 | `AUTH_NUM` | VARCHAR |  | Authorization Number: Used on claims for identifying patient referrals and affected reimbursements. |
| 106 | `UB92_TOB_OVERRIDE` | VARCHAR |  | Override for the type of bill, a numeric code that provides encounter information to payers. |
| 107 | `AMBULANCE_PICK_CITY` | VARCHAR |  | Stores the city of the ambulance pick-up location. |
| 108 | `AMBULANCE_PICK_ST_C_NAME` | VARCHAR | org | Stores the state of the ambulance pick-up location. |
| 109 | `AMBULANCE_PICK_ZIP` | VARCHAR |  | Stores the ZIP code of the ambulance pick-up location. |
| 110 | `AMBULANCE_DROP_CITY` | VARCHAR |  | Stores the city of the ambulance drop-off location. |
| 111 | `AMBULANCE_DROP_ST_C_NAME` | VARCHAR |  | Stores the state of the ambulance drop-off location. |
| 112 | `AMBULANCE_DROP_ZIP` | VARCHAR |  | Stores the ZIP code of the ambulance drop-off location. |
| 113 | `AMBULANCE_DROP_NM` | VARCHAR |  | Stores the last name or organization name of the ambulance drop-off location. |
| 114 | `AMBULANCE_PAT_CNT` | NUMERIC |  | Stores number of patients in the ambulance. |
| 115 | `WC_JURSD_STATE_C_NAME` | VARCHAR |  | Workers' Comp insurance's state of jurisdiction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

