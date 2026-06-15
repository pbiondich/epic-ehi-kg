# OTP_INFO_2

> This table contains order template information relating to admission, transfer, and discharge, as well as lab specimens and releasing information.

**Overflow of:** [OTP_INFO](OTP_INFO.md)  
**Primary key:** `OTP_ID`  
**Columns:** 62  
**Org-specific columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The order template ID. |
| 2 | `ADMIT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 3 | `ADMIT_SERVICE_C_NAME` | VARCHAR | org | The admission service. |
| 4 | `ADMIT_LVL_OF_CARE_C_NAME` | VARCHAR | org | The admission level of care. |
| 5 | `ADMIT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `ADMIT_LEN_STAY` | NUMERIC |  | The admission expected length of stay. |
| 7 | `ADMIT_DISCHG_DATE` | VARCHAR |  | The admission expected discharge date. |
| 8 | `ADMIT_RESIDENT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `ADMIT_INTERN_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `ADMIT_EXP_ADMIT_DT` | VARCHAR |  | The expected admission date. |
| 11 | `TRANS_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 12 | `TRANS_SVC_C_NAME` | VARCHAR |  | The transfer service. |
| 13 | `TRANS_LVL_OF_CARE_C_NAME` | VARCHAR |  | The transfer level of care. |
| 14 | `TRANS_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 15 | `TRANS_LEN_OF_STAY` | NUMERIC |  | The transfer expected length of stay. |
| 16 | `TRANS_DISCHRG_DATE` | VARCHAR |  | The transfer expected discharge date. |
| 17 | `TRANS_ATTND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `DISCHRG_EXPECT_DATE` | VARCHAR |  | The expected discharge date. |
| 19 | `DISCHRG_EXPECT_TM` | DATETIME (Local) |  | The expected discharge time. |
| 20 | `DISCHRG_DISP_C_NAME` | VARCHAR | org | The discharge disposition. |
| 21 | `DISCHRG_DEST_C_NAME` | VARCHAR | org | The discharge destination. |
| 22 | `SPECIMEN_TAKEN_DATE` | DATETIME |  | The date when a lab specimen was taken for this treatment plan order. |
| 23 | `SPECIMEN_TAKEN_TIME` | DATETIME (Local) |  | The time when a lab specimen was taken for this treatment plan order. |
| 24 | `RELEASING_USER_ID` | VARCHAR |  | The unique ID of the user who released this order template. |
| 25 | `RELEASING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `RELEASING_DTTM` | DATETIME (Local) |  | The instant (date and time) when this order template was released. |
| 27 | `DEFAULT_RELEASE_C_NAME` | VARCHAR |  | This is the release type for the Standing/Recurring treatment plan order (Manual or Auto). |
| 28 | `DEFAULT_INTERVAL_C_NAME` | VARCHAR | org | This is the release interval of the Standing/Recurring treatment plan order. |
| 29 | `ADMIT_COND_C_NAME` | VARCHAR | org | The admission condition. |
| 30 | `TRANS_COND_C_NAME` | VARCHAR |  | The transfer condition. |
| 31 | `REL_OFFSET` | NUMERIC |  | Stores the amount of time after the reference time in the treatment day that the order should start. See column REL_OFFSET_TYPE_C to see if this amount is specified in minutes or hours. |
| 32 | `REL_OFFSET_TYPE_C_NAME` | VARCHAR |  | Stores the type of the that is specified in the column REL_OFFSET (minutes vs. hours). |
| 33 | `ORIGINAL_DOSE` | VARCHAR |  | The original dose of an order before it was modified. |
| 34 | `ORIGINAL_UNITS_C_NAME` | VARCHAR | org | The dose units that correspond to the original dose of the order. |
| 35 | `PCT_OF_ORIG_DOSE` | NUMERIC |  | For dose-modified order templates, this item stores the percentage ratio of the current dose to the original dose. |
| 36 | `PAT_UPD_DT` | VARCHAR |  | The effective date of the patient update that should be generated from this order template. |
| 37 | `PAT_UPD_TM` | VARCHAR |  | The effective time of the patient update that should be generated from this order template. |
| 38 | `PAT_UPD_PAT_CLS_C_NAME` | VARCHAR | org | The patient class of the patient update that should be generated from this order template. |
| 39 | `PAT_UPD_SVC_C_NAME` | VARCHAR |  | The service of the patient update that should be generated from this order template. |
| 40 | `PAT_UPD_LOC_C_NAME` | VARCHAR |  | The level of care of the patient update that should be generated from this order template. |
| 41 | `PAT_UPD_ACCOM_CD_C_NAME` | VARCHAR | org | The accommodation code of the patient update that should be generated from this order template. |
| 42 | `PAT_UPD_ACCOM_RSN_C_NAME` | VARCHAR | org | The accommodation reason of the patient update that should be generated from this order template. |
| 43 | `PAT_UPD_RSN_C_NAME` | VARCHAR | org | The reason for change of the patient update that should be generated from this order template. |
| 44 | `ORIG_DOSE_VERIFY_ID` | VARCHAR |  | The ID of the user who last verified the original dose of the order. |
| 45 | `ORIG_DOSE_VERIFY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 46 | `ORIG_DOSE_VER_DTTM` | DATETIME (Local) |  | This item stores the instant that the original dose of the order was last verified. |
| 47 | `ORDERED_AS_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 48 | `OTP_AUC` | NUMERIC |  | Item to store the area under curve value for medications using this value in dose calculation. |
| 49 | `OTP_SEL_TARGETAUC_C_NAME` | VARCHAR | org | Selected type of the Target AUC in the order composer. |
| 50 | `PLANNED_DAY_OF_RNG` | INTEGER |  | This item stores which day in the treatment day's treatment range that this order was planned for. For example, if a treatment day is 3 days long and this order was signed with a start date of "S+1", then this item would store 1 because it was planned for one day after the start of the treatment. |
| 51 | `CRCL_FORMULA_ID` | NUMERIC |  | The creatinine clearance programming point that will be used for area under the curve calculations for an order whose dose calculation programming point does not specify a creatinine clearance programming point. |
| 52 | `CRCL_FORMULA_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 53 | `SELECTED_CRCL_SRC_C_NAME` | VARCHAR |  | Stores the selected source for creatinine clearance. |
| 54 | `CRCL_ORD_SPEC_VAL` | NUMERIC |  | Stores order specific creatinine clearance value. |
| 55 | `SELECTED_SCR_SRC_C_NAME` | VARCHAR |  | Stores the selected source for serum creatinine. |
| 56 | `SCR_ORD_SPEC_VAL` | NUMERIC |  | Stores order specific serum creatinine value. |
| 57 | `USE_AUC_DOSE_YN` | VARCHAR |  | Stores info whether system should automatically update dose for the order using AUC calculations |
| 58 | `RFL_DIF_PROB_YN` | VARCHAR |  | This column returns "Y" if the referral order is for a problem different from the problem being treated in the encounter where the order was placed. If the referral order is for the same problem then "N" or nothing is returned. This column can only be populated if an organization has the PAS license. |
| 59 | `HOSP_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 60 | `TRANSFER_REQUEST_TYPE_C_NAME` | VARCHAR | org | The type of transfer to request being ordered. |
| 61 | `ADT_PATIENT_CLASS_C_NAME` | VARCHAR |  | Patient class used for transfer request orders. |
| 62 | `SELECTED_CRCL_SEX_C_NAME` | VARCHAR | org | The selected patient sex for the purpose of creatinine clearance calculations. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [OTP_INFO](OTP_INFO.md).

