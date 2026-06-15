# UNOS_INFO

> This table contains the core information reported to the United Network for Organ Sharing (UNOS) for each registry record. This table also contains information that can be used to monitor the UNOS reporting process and obtain related statistics.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 91

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `UNOS_REC_KEY` | VARCHAR |  | The unique record key given to the form by UNOS. |
| 3 | `UNOS_ORGAN_C_NAME` | VARCHAR |  | The type of organ transplanted. |
| 4 | `UNOS_PAT_FIRST_NAME` | VARCHAR |  | The patient's first name. |
| 5 | `UNOS_PAT_LAST_NAME` | VARCHAR |  | The patient's last name. |
| 6 | `UNOS_PAT_MIDDLE_INI` | VARCHAR |  | The patient's middle initial. |
| 7 | `UNOS_HIC` | VARCHAR |  | The patient's Health Insurance Commission Number. |
| 8 | `UNOS_DOB_DT` | DATETIME |  | The patient's date of birth. |
| 9 | `UNOS_SEX_C_NAME` | VARCHAR |  | The category number for the UNOS-imported sex assigned at birth. This is the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 10 | `UNOS_PAT_KEY` | INTEGER |  | The transplant center ID issued to the patient by UNOS. |
| 11 | `UNOS_TXP_DT` | DATETIME |  | The date of the patient's transplant operation. |
| 12 | `UNOS_RCPT_CTR_CODE` | VARCHAR |  | The code used by UNOS to identify the facility at which the transplant operation took place. |
| 13 | `UNOS_RCPT_CTR_TYPE` | VARCHAR |  | The type of facility at which the transplant operation took place. |
| 14 | `UNOS_FOL_CTR_CODE` | VARCHAR |  | The code used by UNOS to identify the facility responsible for the patient's follow-up care. |
| 15 | `UNOS_FOL_CTR_TYPE` | VARCHAR |  | The type of facility responsible for the patient's follow-up care. |
| 16 | `UNOS_DONORID` | VARCHAR |  | The transplant center ID issued to the donor by UNOS. |
| 17 | `UNOS_DONOR_TYPE_C_NAME` | VARCHAR |  | The type of donor: living or deceased. |
| 18 | `UNOS_TRR_KEY` | INTEGER |  | The patient's Transplant Recipient Registration ID. |
| 19 | `UNOS_FORM_STATUS_C_NAME` | VARCHAR |  | The form status of the follow-up form sent to UNOS. It should be one of these values: ID Value 1 Amnesty 2 Expected 3 Returned 4 Received 5 Suspended 6 Validated |
| 20 | `UNOS_ADD_DT` | DATETIME |  | The date on which the UNOS follow-up form was created. |
| 21 | `UNOS_CHANGE_DT` | DATETIME |  | The date on which the UNOS follow-up form was changed. |
| 22 | `UNOS_FOL_PROV_NUM` | VARCHAR |  | The NPI of the provider responsible for the patient's follow-up care. |
| 23 | `UNOS_GRAFT_STATUS_C_NAME` | VARCHAR |  | The graft's status: functioning or failed. |
| 24 | `UNOS_GRAFT_FAIL_DT` | DATETIME |  | The date of the graft's failure. |
| 25 | `UNOS_FOL_UP_CODE_C_NAME` | VARCHAR |  | The follow-up code assigned to the encounter. Follow-up code indicates the period of time on which a form is reporting. |
| 26 | `UNOS_TXP_DSCH_DT` | DATETIME |  | The date on which the patient was discharged after the transplant operation. |
| 27 | `PHYS_NAME` | VARCHAR |  | The name of the physician who last saw the patient. |
| 28 | `NPI` | VARCHAR |  | The NPI of the physician who last saw the patient. |
| 29 | `UNOS_HEIGHT` | NUMERIC |  | The patient's height in centimeters. |
| 30 | `UNOS_HEIGHT_STAT_C_NAME` | VARCHAR |  | The code specifying why the patient's height is empty. |
| 31 | `UNOS_WEIGHT` | NUMERIC |  | The patient's weight in kilograms. |
| 32 | `UNOS_WEIGHT_STAT_C_NAME` | VARCHAR |  | The code specifying why the patient's weight is empty. |
| 33 | `PAT_STATUS_DT` | DATETIME |  | The date for the most recent of the following events: patient last seen, organ retransplanted, or patient's death. |
| 34 | `PAT_STATUS_C_NAME` | VARCHAR |  | The patient's status: living, dead, or retransplanted. |
| 35 | `UNOS_FUNC_STATUS_C_NAME` | VARCHAR |  | The patient's functional status as reported to UNOS. |
| 36 | `UNOS_PHYSICAL_CAP_C_NAME` | VARCHAR |  | The patient's physical capacity as reported to UNOS. |
| 37 | `UNOS_WORK_C_NAME` | VARCHAR |  | Indicates whether the patient is working for income. |
| 38 | `UNOS_WORK_REASON_C_NAME` | VARCHAR |  | The reason why the patient is not working. |
| 39 | `UNOS_WORK_LEVEL_C_NAME` | VARCHAR |  | The level at which the patient is working, full time or part time, and why. |
| 40 | `UNOS_ACAD_PROG_C_NAME` | VARCHAR |  | The patient's academic progress. |
| 41 | `UNOS_ACAD_LEVEL_C_NAME` | VARCHAR |  | The patient's academic activity level. |
| 42 | `UNOS_INSUR_PRI_C_NAME` | VARCHAR |  | The patient's primary type of insurance during the follow-up period. |
| 43 | `UNOS_INSUR_FRGN_C_NAME` | VARCHAR |  | The foreign government responsible for the patient's primary insurance. |
| 44 | `UNOS_COGNITIV_DEV_C_NAME` | VARCHAR |  | The patient's cognitive development level. |
| 45 | `UNOS_MOTOR_DEV_C_NAME` | VARCHAR |  | The patient's motor development level. |
| 46 | `UNOS_VITALS_DT` | DATETIME |  | The date on which the patient's height and weight were measured. This field is specified for pediatric patients. |
| 47 | `UNOS_STATE_C_NAME` | VARCHAR |  | The patient's state of permanent residency. |
| 48 | `UNOS_ZIP` | VARCHAR |  | The patient's ZIP Code. |
| 49 | `VOID_REASON` | VARCHAR |  | The reason for voiding the record. |
| 50 | `UNOS_PREV_SURNAME` | VARCHAR |  | Any surnames used by the patient, other than the surname recorded in the Name item. |
| 51 | `UNOS_PAT_IN_ZIP_C_NAME` | VARCHAR |  | Indicates whether the patient is waiting in their permanent ZIP code. |
| 52 | `UNOS_CITIZEN_C_NAME` | VARCHAR |  | The candidate's citizenship status. |
| 53 | `UNOS_ENTRY_USA_DT` | NUMERIC |  | If the candidate is a Non-Resident Alien, the year the candidate entered the United States. |
| 54 | `UNOS_EDU_LEVEL_C_NAME` | VARCHAR |  | The candidate's highest level of education. |
| 55 | `UNOS_SEC_PAY_C_NAME` | VARCHAR |  | The candidate's secondary source of payment. |
| 56 | `UNOS_OTIS_REGID` | VARCHAR |  | The candidate's registry ID in OTIS, as supplied by UNOS. |
| 57 | `UNOS_LIST_ADD_DT` | DATETIME |  | The date the candidate was listed or added to the waitlist. |
| 58 | `UNOS_TXP_ADMIT_DT` | DATETIME |  | The date the recipient was admitted to the transplant center. If the patient was admitted to the hospital before it was determined a transplant was needed, the date it was determined the patient needed a transplant. |
| 59 | `UNOS_TRSFR_PROV_NUM` | VARCHAR |  | UNOS transfer provider number. This information is downloaded from UNOS. |
| 60 | `UNOS_TRANSFER_DT` | DATETIME |  | Transfer date. This information is downloaded from UNOS. |
| 61 | `HOME_ADDRESS` | VARCHAR |  | The patient's street address. |
| 62 | `HOME_CITY` | VARCHAR |  | The patient's home city. |
| 63 | `HOME_PHONE` | VARCHAR |  | The patient's home phone number. |
| 64 | `WORK_PHONE` | VARCHAR |  | The patient's work phone number. |
| 65 | `EMAIL` | VARCHAR |  | The patient's e-mail address. |
| 66 | `UNOS_MARITAL_ST_C_NAME` | VARCHAR |  | The patient's marital status. |
| 67 | `UNOS_LIV_DNR_TYP_C_NAME` | VARCHAR |  | The relationship between the living donor and the recipient. |
| 68 | `UNOS_LIV_DNR_TYP_SP` | VARCHAR |  | Free text description of the relationship between the living donor and the recipient. |
| 69 | `DNR_INSURANCE_ST_C_NAME` | VARCHAR |  | Indicates whether the donor had health insurance at the time of donation. |
| 70 | `DNR_RECIPIENT_LNAME` | VARCHAR |  | The recipient's last name in the living donor form. |
| 71 | `DNR_RECIPIENT_FNAME` | VARCHAR |  | The recipient's first name in the living donor form. |
| 72 | `DNR_RECOV_CNTR_CODE` | VARCHAR |  | The donor recovery facility center code. |
| 73 | `DNR_RECOV_CNTR_TYPE` | VARCHAR |  | The donor recovery facility center type. |
| 74 | `DNR_WRKUP_CNTR_CODE` | VARCHAR |  | The donor workup facility center code. |
| 75 | `DNR_WRKUP_CNTR_TYPE` | VARCHAR |  | The donor workup facility center type. |
| 76 | `ORG_RCV_TXP_SAME_YN` | VARCHAR |  | Indicates whether the organ recovery and transplant occurred at the same center. |
| 77 | `PRE_DONATN_HEIGHT` | NUMERIC |  | The living donor's height (in centimeters) prior to donation. |
| 78 | `PRE_DONATN_HT_ST_C_NAME` | VARCHAR |  | Specifies why the height of the living donor prior to donation is not available. |
| 79 | `PRE_DONATN_WEIGHT` | NUMERIC |  | The living donor's weight (in kilograms) prior to donation. |
| 80 | `PRE_DONATN_WT_ST_C_NAME` | VARCHAR |  | Specifies why the weight of the living donor prior to donation is not available. |
| 81 | `UNOS_DNR_STATUS_C_NAME` | VARCHAR |  | The status of the donor. |
| 82 | `UNOS_DNR_ST_COLL` | VARCHAR |  | The attempts to collect donor status if unable to contact donor. |
| 83 | `UNOS_LIV_DNR_ST_C_NAME` | VARCHAR |  | The most recent donor status. |
| 84 | `UNOS_LF_SUPPORT_YN` | VARCHAR |  | Indicates whether the candidate was on life support. |
| 85 | `UNOS_LF_SPT_VENT_YN` | VARCHAR |  | Indicates whether the candidate was on continuous invasive ventilation. |
| 86 | `UNOS_LF_SPT_LVR_YN` | VARCHAR |  | Indicates whether the candidate had an artificial liver. |
| 87 | `UNOS_LF_SPT_OTH_YN` | VARCHAR |  | Indicates whether the candidate was on other types of life support. |
| 88 | `UNOS_LF_SPT_OTH_SP` | VARCHAR |  | Free text description of the type of life support. |
| 89 | `UNOS_PA_PRIM_INS_C_NAME` | VARCHAR |  | UNOS pancreas primary source of payment |
| 90 | `UNOS_PA_FRN_GOV_C_NAME` | VARCHAR |  | UNOS pancreas foreign government, specify |
| 91 | `UNOS_ETHNICITY_C_NAME` | VARCHAR |  | The patient's ethnicity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

