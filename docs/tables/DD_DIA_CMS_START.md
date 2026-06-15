# DD_DIA_CMS_START

> This table contains data elements submitted for CMS ESRD patient registration forms (CMS-2728).

**Overflow family:** [DD_DIA_CMS_START_2](DD_DIA_CMS_START_2.md)  
**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 86  
**Org-specific columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `FORM_IDENTIFIER` | VARCHAR |  | The CMS 2728 form identifier. |
| 3 | `DLYS_REG_FORM_TYPE_C_NAME` | VARCHAR | org | The CMS 2728 form type, such as initial registration or reentitlement. |
| 4 | `ADMISSION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `PAT_FIRST_NAME` | VARCHAR |  | The patient's first name. |
| 6 | `PAT_MIDDLE_INITIAL` | VARCHAR |  | The patient's middle initial. |
| 7 | `PAT_LAST_NAME` | VARCHAR |  | The patient's last name. |
| 8 | `DLYS_NAME_SUFFIX_C_NAME` | VARCHAR | org | The patient's name suffix. |
| 9 | `DLYS_PAT_SEX_C_NAME` | VARCHAR |  | The patient's sex assigned at birth. |
| 10 | `PAT_BIRTH_DATE` | DATETIME |  | The patient's date of birth. |
| 11 | `PAT_HICNUM` | VARCHAR |  | The patient's Medicare health insurance claim number. |
| 12 | `PAT_MBI_NUM` | VARCHAR |  | The patient's Medicare Beneficiary Identifier number. |
| 13 | `PAT_SSN` | VARCHAR |  | The patient's Social Security number. |
| 14 | `MAIL_ADDRESS_STREET_1` | VARCHAR |  | The first line of the street address of the patient's mailing address. |
| 15 | `MAIL_ADDRESS_STREET_2` | VARCHAR |  | The second line of the street address of the patient's mailing address. |
| 16 | `MAIL_ADDRESS_CITY` | VARCHAR |  | The city of the patient's mailing address. |
| 17 | `MAIL_ADDRESS_TAX_STATE_C_NAME` | VARCHAR | org | The state of the patient's mailing address. |
| 18 | `MAIL_ADDRESS_COUNTY_2_C_NAME` | VARCHAR | org | The county of the patient's mailing address. |
| 19 | `MAIL_ADDRESS_ZIP_EXT` | VARCHAR |  | The ZIP code extension of the patient's mailing address. |
| 20 | `PHONE_AREA_CODE` | NUMERIC |  | The area code of the patient's phone number. |
| 21 | `PHONE_NUMBER` | VARCHAR |  | The patient's phone number, minus the area code. |
| 22 | `DLYS_PAT_CNTRY_OF_ORG_C_NAME` | VARCHAR |  | The patient's country of origin. |
| 23 | `DLYS_PAT_ETHNICITY_C_NAME` | VARCHAR | org | The patient's ethnicity. |
| 24 | `PAT_TRIBE_CODE` | NUMERIC |  | This column has been replaced by DIA_PAT_TRIBE_C (RDI/28584) in table DD_DIA_CMS_START. To look up the deprecated column's value after the Clarity Compass upgrade, join column DD_DIA_CMS_START.DIA_PAT_TRIBE_C to table ZC_PAT_TRIBE column PAT_TRIBE_C and get the TITLE value. |
| 25 | `DLYS_ETH_SELF_REP_C_NAME` | VARCHAR |  | Whether the patient's race and ethnicity were self-reported. |
| 26 | `ESRD_MEDICARE_APPLY_YN` | VARCHAR |  | Whether the patient is applying for end stage renal disease Medicare coverage. |
| 27 | `PRIOR_DLYS_EMPY_STATUS_C_NAME` | VARCHAR |  | The patient's employment status six months prior to renal failure. |
| 28 | `CURRENT_DLYS_EMPY_STATUS_C_NAME` | VARCHAR |  | The patient's current employment status. |
| 29 | `PAT_HEIGHT` | NUMERIC |  | The patient's height. |
| 30 | `DLYS_HEIGHT_UNIT_C_NAME` | VARCHAR | org | The unit used for the patient's height. |
| 31 | `PAT_DRY_WEIGHT` | NUMERIC |  | The patient's dry weight. |
| 32 | `DLYS_WEIGHT_UNIT_C_NAME` | VARCHAR | org | The unit used for the patient's weight. |
| 33 | `DIA_CMS_GFR_METHOD_C_NAME` | VARCHAR | org | The method used to calculate the patient's glomerular filtration rate (GFR). |
| 34 | `PRIM_CAUSE_RENAL_FAIL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 35 | `EPO_RECEIVED_DIA_CMS_YNU_C_NAME` | VARCHAR | org | Whether the patient received exogenous erythropoietin (EPO) or equivalent prior to end stage renal disease therapy. |
| 36 | `EPO_DIA_CMS_DATE_RANGE_C_NAME` | VARCHAR |  | The time range in which exogenous erythropoietin (EPO) or equivalent was administered to the patient prior to end stage renal disease therapy. |
| 37 | `NEPH_CARE_RECV_DIA_CMS_YNU_C_NAME` | VARCHAR |  | Whether the patient was under nephrologist care before starting end stage renal disease therapy. |
| 38 | `NEPH_CARE_DIA_CMS_DATE_RANGE_C_NAME` | VARCHAR |  | The time range in which the patient was under nephrologist care prior to end stage renal disease therapy. |
| 39 | `DIET_CARE_RECV_DIA_CMS_YNU_C_NAME` | VARCHAR |  | Whether the patient was under kidney dietician care prior to end stage renal disease therapy. |
| 40 | `DIET_CARE_DIA_CMS_DATE_RANGE_C_NAME` | VARCHAR |  | The time range in which the patient was under kidney dietician care prior to end stage renal disease therapy. |
| 41 | `DIA_CMS_FIRST_ACCESS_C_NAME` | VARCHAR | org | The type of access used for the first outpatient dialysis treatment prior to end stage renal disease therapy. |
| 42 | `MATURE_AVF_PRESENT_YN` | VARCHAR |  | Whether the patient had a maturing arteriovenous fistula (AVF) present prior to end stage renal disease therapy. |
| 43 | `MATURE_AVG_PRESENT_YN` | VARCHAR |  | Whether the patient had a maturing arteriovenous graft (AVG) present prior to end stage renal disease therapy. |
| 44 | `DLYS_TRT_LOCATION_C_NAME` | VARCHAR | org | The primary setting in which the patient receives dialysis treatment, such as the patient's home, a dialysis treatment center, skilled nursing facility, or long-term care facility. |
| 45 | `DLYS_TRT_TYPE_C_NAME` | VARCHAR | org | The type of dialysis treatment the patient receives, e.g. hemodialysis or peritoneal dialysis. |
| 46 | `DIALYSIS_SESSIONS_PER_WEEK` | NUMERIC |  | The number of hemodialysis sessions per week prescribed for the patient. |
| 47 | `DIALYSIS_SESSION_LENGTH_HOURS` | NUMERIC |  | The duration, in hours, of hemodialysis sessions prescribed for the patient. |
| 48 | `CHRONIC_DIALYSIS_START_DATE` | DATETIME |  | The date the patient began a regular course of dialysis treatments. |
| 49 | `FACILITY_TREATMENT_START_DATE` | DATETIME |  | The date the patient began receiving dialysis treatments at the current facility. |
| 50 | `TXP_OPTIONS_PROVIDED_YN` | VARCHAR |  | Whether the patient has been informed of their options for receiving a kidney transplant. |
| 51 | `ATTENDING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 52 | `ATTENDING_PROV_REMARKS` | VARCHAR |  | Miscellaneous remarks entered by the patient's attending provider. |
| 53 | `LAB_ALBUMIN_VALUE` | NUMERIC |  | The patient's serum albumin lab value. |
| 54 | `LAB_ALBUMIN_DATE` | DATETIME |  | The patient's serum albumin lab collection date. |
| 55 | `LAB_ALBUMIN_LOWER_LIMIT` | NUMERIC |  | The patient's serum albumin lab lower limit value. |
| 56 | `LAB_ALBUMIN_METHOD_C_NAME` | VARCHAR | org | The patient's serum albumin lab method. |
| 57 | `LAB_CREATININE_VALUE` | NUMERIC |  | The patient's serum creatinine lab value. |
| 58 | `LAB_CREATININE_DATE` | DATETIME |  | The patient's serum creatinine lab collection date. |
| 59 | `LAB_HEMOGLOBIN_VALUE` | NUMERIC |  | The patient's hemoglobin lab value. |
| 60 | `LAB_HEMOGLOBIN_DATE` | DATETIME |  | The patient's hemoglobin lab collection date. |
| 61 | `LAB_HBA1C_VALUE` | NUMERIC |  | The patient's glycated hemoglobin (HbA1c) lab value that was collected within 45 days prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 62 | `LAB_HBA1C_DATE` | DATETIME |  | The patient's glycated hemoglobin (HbA1C) lab date that was collected within 45 days prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 63 | `LAB_LIPID_TC_VALUE` | NUMERIC |  | The patient's lipid profile total cholesterol lab value that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 64 | `LAB_LIPID_TC_DATE` | DATETIME |  | The patient's lipid profile total cholesterol lab date that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 65 | `LAB_LIPID_LDL_VALUE` | NUMERIC |  | The patient's lipid profile LDL cholesterol lab value that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 66 | `LAB_LIPID_LDL_DATE` | DATETIME |  | The patient's lipid profile LDL cholesterol lab date that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 67 | `LAB_LIPID_HDL_VALUE` | NUMERIC |  | The patient's lipid profile HDL cholesterol lab value that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 68 | `LAB_LIPID_HDL_DATE` | DATETIME |  | The patient's lipid profile HDL cholesterol lab date that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 69 | `LAB_LIPID_TRIGLYCERIDES_VALUE` | NUMERIC |  | The patient's lipid profile triglyceride lab value that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 70 | `LAB_LIPID_TRIGLYCERIDES_DATE` | DATETIME |  | The patient's lipid profile triglyceride lab date that was collected within one year prior to the first dialysis treatment or kidney transplant (whichever is more recent). |
| 71 | `TRAINING_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 72 | `TRAINING_START_DATE` | DATETIME |  | The start date for the patient's dialysis training. |
| 73 | `TRAINING_END_DATE` | DATETIME |  | The end date for the patient's dialysis training. |
| 74 | `TRAINING_DLYS_TRT_TYPE_C_NAME` | VARCHAR |  | The type of training given to a patient in preparation for dialysis treatment. |
| 75 | `DLYS_SELFCARE_STATUS_C_NAME` | VARCHAR |  | Whether the patient is expected to perform self-care at home or in-center after dialysis training. |
| 76 | `SELF_DIALYZE_YN` | VARCHAR |  | Whether the patient will self-dialyze after completing dialysis training. |
| 77 | `TRAINING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 78 | `MAIL_ADDRESS_ZIP` | VARCHAR |  | The ZIP code of the patient's mailing address. |
| 79 | `PAT_NO_SIGN_REASON_C_NAME` | VARCHAR |  | The dialysis patient unable to sign reasons category ID for the CMS Form 2728 abstraction. |
| 80 | `PAT_DEATH_DATE` | DATETIME |  | The date when a dialysis patient died. |
| 81 | `PRIOR_LAB_VALUES_C_NAME` | VARCHAR | org | The time period when labs were collected for CMS Form 2728 for the abstraction. |
| 82 | `LAB_CYSTATIN_C_VALUE` | NUMERIC |  | The patient's Cystatin C lab value. |
| 83 | `LAB_CYSTATIN_C_DATE` | DATETIME |  | The patient's Cystatin C lab collection date. |
| 84 | `FIRST_ACSS_CVC_USED_YN` | VARCHAR |  | Indicates whether one lumen of the central venous catheter was used and one needle was placed in an AVF or graft. 'Y' indicates that one lumen of the central venous catheter was used and one needle was placed in an AVF or graft. 'N' or NULL indicates that a central venous catheter is not present or was not used. |
| 85 | `FIRST_ACSS_PD_CATH_USED_YN` | VARCHAR |  | Indicates whether the peritoneal dialysis catheter was present during the patient's first chronic dialysis treatment. 'Y' indicates that the peritoneal dialysis catheter was present. 'N' or NULL indicates that a peritoneal dialysis catheter was not present. |
| 86 | `DIA_PAT_TRIBE_C_NAME` | VARCHAR | org | The dialysis patient tribe category ID for the registry data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

