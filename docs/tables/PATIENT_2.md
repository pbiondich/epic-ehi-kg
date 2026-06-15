# PATIENT_2

> This table supplements the PATIENT table. It contains basic information about patients.

**Overflow of:** [PATIENT](PATIENT.md)  
**Primary key:** `PAT_ID`  
**Columns:** 55  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `RECORD_TYPE_6_C_NAME` | VARCHAR |  | The type of patient (EPT) record that this row relates to. |
| 3 | `BIRTH_TM` | DATETIME (Local) |  | The date and time of the patient's birth in 24 hour format. |
| 4 | `DEATH_TM` | DATETIME (Local) |  | The date and time of the patient's death in 24 hour format. |
| 5 | `FAX` | VARCHAR |  | The patient's fax number. |
| 6 | `CITIZENSHIP_C_NAME` | VARCHAR | org | The patient's citizenship status information. |
| 7 | `MED_HX_NOTE_ID` | VARCHAR |  | This column contains a link to the General Use Notes (HNO) meds history note for this patient. |
| 8 | `IS_ADOPTED_YN` | VARCHAR |  | Capture if patient is adopted or not. |
| 9 | `BIRTH_HOSPITAL` | VARCHAR |  | Capture the name of the hospital where the patient was born or first seen after a non-hospital birth. |
| 10 | `ALRGY_UPD_INST` | DATETIME (Attached) |  | The PATIENT table extracts the last date on which the patient's allergy information was verified. For more granularity, this table extracts the instant (date and time) that this information was verified. |
| 11 | `BIRTH_CITY` | VARCHAR |  | The patient's city of birth. |
| 12 | `BIRTH_ST_C_NAME` | VARCHAR | org | The patient's state of birth. |
| 13 | `SCHOOL_C_NAME` | VARCHAR | org | School that the patient attends. |
| 14 | `REFERRAL_SOURCE_ID` | VARCHAR |  | The unique ID of the provider or other source that referred the patient to the facility. This is distinct from the encounter-specific referral source in PAT_ENC. |
| 15 | `REFERRAL_SOURCE_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 16 | `PAT_NAME_RECORD_ID` | VARCHAR |  | The networked item that points to the patient's name record (EAN). |
| 17 | `COMM_METHOD_C_ZC_COMM_METHOD_NAME` | VARCHAR | org | Column to hold the category value of Preferred Communication Method (I EPT 89) for the Patient_2 table. |
| 18 | `FOSTER_CHILD_YN` | VARCHAR |  | Indicates whether the patient is a foster child. |
| 19 | `CONF_PAT_REAL_NAME` | VARCHAR |  | The real name of a confidential patient. |
| 20 | `PAT_CONF_NM_REC_ID` | VARCHAR |  | The networked item pointing to the name record for the patient's confidential name. |
| 21 | `ACTIVE_IER_ID` | VARCHAR |  | Link to active Identity History (IER) record for this patient. |
| 22 | `OTH_CITY` | VARCHAR |  | Contains the city for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 23 | `OTH_ZIP` | VARCHAR |  | Contains the zip code for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 24 | `OTH_PHONE` | VARCHAR |  | Contains the phone number for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 25 | `OTH_EMAIL` | VARCHAR |  | Contains the email for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 26 | `OTH_CONTACT_PERSON` | VARCHAR |  | Contains the contact person for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 27 | `OTH_HOUSE_NUMBER` | VARCHAR |  | Contains the house number for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 28 | `OTH_DISTRICT_C_NAME` | VARCHAR | org | Contains the district for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 29 | `OTH_COUNTY_C_NAME` | VARCHAR | org | Contains the county for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 30 | `OTH_COUNTRY_C_NAME` | VARCHAR | org | Contains the country for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 31 | `OTH_START_DATE` | DATETIME |  | Contains the start date for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 32 | `OTH_END_DATE` | DATETIME |  | Contains the end date for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 33 | `DEF_ADDRESS_C_NAME` | VARCHAR |  | Stores the address that will be used by default by the pharmacy when determining where to mail prescriptions. This can be home, temporary, or prescription. |
| 34 | `OTH_STATE_C_NAME` | VARCHAR |  | Contains the state for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| 35 | `MAIDEN_NAME` | VARCHAR |  | The patient's maiden name. |
| 36 | `EMPR_CITY` | VARCHAR |  | The city of the patient's employer. |
| 37 | `EMPR_STATE_C_NAME` | VARCHAR |  | The category number for the state of the patient's employer. |
| 38 | `EMPR_ZIP` | VARCHAR |  | The ZIP code of the patient's employer. |
| 39 | `EMPR_COUNTRY_C_NAME` | VARCHAR |  | The category number for the country of the patient's employer. |
| 40 | `EMPR_PHONE` | VARCHAR |  | The phone number of the patient's employer. |
| 41 | `BILL_INSTRUCT_C_NAME` | VARCHAR | org | The category number for the Billing Instruction Code for the patient. |
| 42 | `PAT_ASSIST_C_NAME` | VARCHAR | org | The category number for the Patient Assistance Code. |
| 43 | `BILL_COMMENT` | VARCHAR |  | General comments regarding patient billing instruction |
| 44 | `CHART_ABSTD_YN` | VARCHAR |  | Indicates whether the chart was abstracted. |
| 45 | `MOTHER_HEIGHT` | NUMERIC |  | Height of the patient's mother. This is used for calculations in the Growth Charts activity. |
| 46 | `FATHER_HEIGHT` | NUMERIC |  | Height of the patient's father. This is used for calculations in the Growth Charts activity. |
| 47 | `PAT_VERIFICATION_ID` | NUMERIC |  | Verification record for this patient |
| 48 | `ALRGY_REV_STAT_C_NAME` | VARCHAR | org | This item stores the status of the review of allergies. |
| 49 | `ALRGY_REV_CMT` | VARCHAR |  | This item stores a comment associated with the review of allergies. |
| 50 | `REVERSE_NATL_ID` | VARCHAR |  | Used to store reverse National Identifier in an indexed item for patient search of partial National Identifier. |
| 51 | `ADV_DIR_REV_DT` | DATETIME |  | The date on which a user last reviewed the patient's advanced directive. |
| 52 | `ADV_DIR_REV_USER_ID` | VARCHAR |  | The user who last reviewed the patient's advanced directive. |
| 53 | `ADV_DIR_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 54 | `LIVING_ARRANGE_C_NAME` | VARCHAR | org | The patient's living arrangement. |
| 55 | `PED_COMMENT` | VARCHAR |  | Free-text pediatric comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PATIENT](PATIENT.md).

