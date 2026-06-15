# CLAIM_INFO3

> This table contains claims information from Claim Information (CLM) records for Hospital and Professional Billing.

**Primary key:** `CLAIM_ID`  
**Columns:** 92  
**Org-specific columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Info record. |
| 2 | `KIDMED_IMMUNI_C_NAME` | VARCHAR | org | The last immunization date for the KidMed visit. |
| 3 | `KIDMED_SUSPECTED_YN` | VARCHAR |  | Whether there are suspected conditions, for the KidMed visit. |
| 4 | `KIDMED_R1_PROV_FST` | VARCHAR |  | The referred-to provider's last name for the first referral for the KidMed visit. |
| 5 | `KIDMED_R1_PROV_LAST` | VARCHAR |  | The referred-to provider's first name for the first referral for the KidMed visit. |
| 6 | `KIDMED_R1_PROV_PH` | VARCHAR |  | The referred-to provider's phone number for the first referral for the KidMed visit. |
| 7 | `KIDMED_R1_APPT_DT` | DATETIME |  | The appointment date for the first referral for the KidMed visit. |
| 8 | `KIDMED_R1_REASON` | VARCHAR |  | The appointment reason for the first referral for the KidMed visit. |
| 9 | `KIDMED_R1_TYPE_C_NAME` | VARCHAR | org | The appointment type for the first referral for the KidMed visit. |
| 10 | `KIDMED_R2_PROV_FST` | VARCHAR |  | The referred-to provider's last name for the second referral for the KidMed visit. |
| 11 | `KIDMED_R2_PROV_LAST` | VARCHAR |  | The referred-to provider's first name for the second referral for the KidMed visit. |
| 12 | `KIDMED_R2_PROV_PH` | VARCHAR |  | The referred-to provider's phone number for the second referral for the KidMed visit. |
| 13 | `KIDMED_R2_APPT_DT` | DATETIME |  | The appointment date for the second referral for the KidMed visit. |
| 14 | `KIDMED_R2_REASON` | VARCHAR |  | The appointment reason for the second referral for the KidMed visit. |
| 15 | `KIDMED_R2_TYPE_C_NAME` | VARCHAR |  | The appointment type for the second referral for the KidMed visit. |
| 16 | `KIDMED_R3_PROV_FST` | VARCHAR |  | The referred-to provider's last name for the third referral for the KidMed visit. |
| 17 | `KIDMED_R3_PROV_LAST` | VARCHAR |  | The referred-to provider's first name for the third referral for the KidMed visit. |
| 18 | `KIDMED_R3_PROV_PH` | VARCHAR |  | The referred-to provider's phone number for the third referral for the KidMed visit. |
| 19 | `KIDMED_R3_APPT_DT` | DATETIME |  | The appointment date for the third referral for the KidMed visit. |
| 20 | `KIDMED_R3_REASON` | VARCHAR |  | The appointment reason for the third referral for the KidMed visit. |
| 21 | `KIDMED_R3_TYPE_C_NAME` | VARCHAR |  | The appointment type for the third referral for the KidMed visit. |
| 22 | `SPARCS_START_DATETIME` | DATETIME (Local) |  | The start date and time of the patient's presence in the operating room. |
| 23 | `SPARCS_END_DATETIME` | DATETIME (Local) |  | The end date and time of the patient's presence in the operating room. |
| 24 | `SPARCS_ANESTHESIA_C_NAME` | VARCHAR | org | Type of anesthesia administered during the stay. |
| 25 | `SPARCS_EXEMPT_UI_C_NAME` | VARCHAR | org | The code which identifies a discharge from a unit within the facility that is exempt from Diagnosis Related Group (DRG) reimbursement. |
| 26 | `AMBL_PICK_CNTRY_C_NAME` | VARCHAR | org | Stores the ambulance pick-up location address country. |
| 27 | `AMBL_DROP_CNTRY_C_NAME` | VARCHAR |  | Stores the ambulance drop-off location address country. |
| 28 | `CLIENT_IND_C_NAME` | VARCHAR | org | Whether the patient is a new or existing client. |
| 29 | `INCOME_AMT` | NUMERIC |  | The patient's annual income. |
| 30 | `NUM_PEOPLE_SUPPORTD` | INTEGER |  | This item is used to store the number of people financially supported by the patient. |
| 31 | `ML_PRIM_BRTH_CTRL_C_NAME` | VARCHAR | org | This item is used to store the primary method of male birth control being used by the patient. |
| 32 | `PRACTITNR_LVL_CD_C_NAME` | VARCHAR | org | This item is used to store the medical practitioner level code of the practitioner that's seeing the patient. |
| 33 | `PAYMENT_C_NAME` | VARCHAR | org | This item is used to store whether the patient made a full, partial, or no payment for the visit. |
| 34 | `FAM_PLANNG_ELIG_DT` | DATETIME |  | The date the patient became eligible for family planning insurance. |
| 35 | `INSURANCE_TYPE_C_NAME` | VARCHAR | org | The family planning insurance type used by the patient. |
| 36 | `WK_COMP_EMPR_ID` | VARCHAR |  | The ID of the employer record for this Workers' Comp claim. |
| 37 | `WK_COMP_EMPR_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 38 | `CLINICAL_TRIAL_NUM` | VARCHAR |  | The National Clinical Trial (NCT) number. |
| 39 | `RESUB_REASON_C_NAME` | VARCHAR | org | Record the reason for the claim resubmission. |
| 40 | `CVR_LST_CT_TEST_C_NAME` | VARCHAR | org | Whether there was a last chlamydia test, for contraceptive vaginal ring (CVR). |
| 41 | `CVR_LST_CT_TEST_DT` | DATETIME |  | Date of the last chlamydia test, for contraceptive vaginal ring (CVR). |
| 42 | `CVR_LST_PAP_TEST_C_NAME` | VARCHAR | org | Whether there was a last pap test, for contraceptive vaginal ring (CVR). |
| 43 | `CVR_LST_PAP_TEST_DT` | DATETIME |  | Date of the last pap test, for contraceptive vaginal ring (CVR). |
| 44 | `CVR_INS_ENRL_ASST_C_NAME` | VARCHAR | org | How the patient enrolled in assistance, for contraceptive vaginal ring (CVR). |
| 45 | `CVR_PREG_INT_SCR_C_NAME` | VARCHAR | org | Whether the patient plans to have a pregnancy intention screening, for contraceptive vaginal ring (CVR). |
| 46 | `DME_LAST_CERT_DT` | DATETIME |  | Last certification date for the durable medical equipment (DME). |
| 47 | `HDH_EXAM_CODE_C_NAME` | VARCHAR |  | The exam code for Health and Developmental History. |
| 48 | `OVRIDE_OHIP_MASTER_NUM` | VARCHAR |  | The override master number for Ontario Health Insurance Plan (OHIP). |
| 49 | `OVRIDE_DON_REC_OHIP_NUM` | VARCHAR |  | The recipient's Ontario Health Insurance Plan (OHIP) number for donor claims. |
| 50 | `WK_COMP_EMPR_CITY` | VARCHAR |  | Employer city for an accident claim. |
| 51 | `WK_COMP_STATE_C_NAME` | VARCHAR | org | Employer state for an accident claim. |
| 52 | `WK_COMP_EMPR_ZIP` | VARCHAR |  | Employer zip for an accident claim. |
| 53 | `WK_COMP_CNTRY_C_NAME` | VARCHAR |  | Employer country for an accident claim. |
| 54 | `WK_COMP_EMPR_PHONE` | VARCHAR |  | Employer phone number for an accident claim. |
| 55 | `PAT_ROLE_IN_ACCIDENT_C_NAME` | VARCHAR | org | The patient's role for an automobile accident claim. |
| 56 | `DRIVER_NAME` | VARCHAR |  | Driver's name, for an auto accident. |
| 57 | `DRIVER_CITY` | VARCHAR |  | Driver's city, for an auto accident. |
| 58 | `DRIVER_STATE_C_NAME` | VARCHAR |  | Driver's state, for an auto accident. |
| 59 | `DRIVER_ZIP` | VARCHAR |  | Driver's ZIP code, for an auto accident. |
| 60 | `DRIVER_COUNTRY_C_NAME` | VARCHAR |  | Driver's country, for an auto accident. |
| 61 | `DRIVER_PHONE` | VARCHAR |  | Driver's phone number, for an auto accident. |
| 62 | `VEHICLE_REG_NUM` | VARCHAR |  | The vehicle registration number of the car involved in an auto accident. |
| 63 | `PAY_TO_CODE_C_NAME` | VARCHAR | org | Override for the Alberta Health Services (AHS) pay-to code. |
| 64 | `PAY_TO_PHN` | NUMERIC |  | The Alberta Health Services (AHS) pay-to patient health number. |
| 65 | `OTHER_PAYEE_ACCT_ID` | NUMERIC |  | This item stores the other payee guarantor account number for AHS. |
| 66 | `AMBULANCE_PICK_CD_C_NAME` | VARCHAR | org | Emergency Medical Services (EMS) code for the ambulance pick-up location, for Alberta Blue Cross. |
| 67 | `AMBULANCE_DROP_CD_C_NAME` | VARCHAR | org | Emergency Medical Services (EMS) code for the ambulance drop-off location, for Alberta Blue Cross. |
| 68 | `PRIOR_INV_NUM` | VARCHAR |  | The previous invoice number for Alberta Health Services (AHS) professional claims. |
| 69 | `INJURY_REASON_C_NAME` | VARCHAR | org | The cause of the injury. |
| 70 | `INJURY_ACTIVITY_C_NAME` | VARCHAR | org | The main activity of the injured person, or the type of situation the injured person was in, at the time of injury. |
| 71 | `INJURY_MECHANISM_C_NAME` | VARCHAR | org | The activity, contact, or influence that caused the injury to occur. |
| 72 | `INJURY_SEVERITY_C_NAME` | VARCHAR | org | How seriously the patient appears to be injured. |
| 73 | `TXPORT_MEANS_C_NAME` | VARCHAR | org | Indicates the type of transportation being used by the injured person at the time of the traffic accident. |
| 74 | `INJURY_MUNICIP_C_NAME` | VARCHAR | org | The municipality where the injury took place. |
| 75 | `ACCIDENT_LONGITUDE` | VARCHAR |  | The longitude of where the auto accident took place. |
| 76 | `ACCIDENT_LATITUDE` | VARCHAR |  | The latitude of where the auto accident took place. |
| 77 | `CNTRPARTY_VEHICLE_C_NAME` | VARCHAR | org | The type of vehicle which caused the auto accident. |
| 78 | `TRAFFIC_SITUATION_C_NAME` | VARCHAR | org | Indicates the accident-causing traffic situation. |
| 79 | `USED_PROTECTION_C_NAME` | VARCHAR |  | Indicates whether the injured person used protection, such as a helmet or seat belt, at the time of the injury. |
| 80 | `PRODUCT_USED_C_NAME` | VARCHAR | org | Indicates the machinery or equipment being used at the time of the work-related injury. |
| 81 | `PLAYGROUND_TYPE_C_NAME` | VARCHAR | org | Type of playground the accident occurred on. |
| 82 | `INJURY_PRODUCT_TYPE_C_NAME` | VARCHAR | org | Type of product involved in the injury. |
| 83 | `PRODUCT_NAME` | VARCHAR |  | Name of the product involved in the injury. |
| 84 | `PRODUCT_DEFECTIVE_C_NAME` | VARCHAR |  | Whether the product that led to injury was defective. |
| 85 | `PRODUCT_DESC` | VARCHAR |  | A description of the product involved in the injury. |
| 86 | `EMPR_IND_C_NAME` | VARCHAR | org | Indicates the industry of the injured person’s employer. |
| 87 | `ACCIDENT_COUNTRY_C_NAME` | VARCHAR |  | Country where the accident occurred. |
| 88 | `ACCIDENT_DISTRICT_C_NAME` | VARCHAR | org | District where the accident occurred. |
| 89 | `ACDNT_HOUSE_NUMBER` | VARCHAR |  | House number where the accident occurred. |
| 90 | `FIRST_DEPT_REFERRED_TO` | VARCHAR |  | Referral 1: referred-to department name |
| 91 | `SECOND_DEPT_REFERRED_TO` | VARCHAR |  | Referral 2: referred-to department name |
| 92 | `WK_COMP_EMPR_ID_CMT` | VARCHAR |  | Enter the employer responsible for this workers' compensation claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

