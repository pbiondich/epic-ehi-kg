# PAT_RELATIONSHIPS

> Demographic information for patient contacts.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 37  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_REL_NAME` | VARCHAR |  | The name of the patient's contact. |
| 4 | `PAT_REL_CITY` | VARCHAR |  | Contact's city of residence |
| 5 | `PAT_REL_ZIP` | VARCHAR |  | The ZIP code of the patient's contact. |
| 6 | `PAT_REL_COUNTY_C_NAME` | VARCHAR | org | Contact's county of residence |
| 7 | `PAT_REL_COUNTRY_C_NAME` | VARCHAR | org | Contact's country of residence |
| 8 | `PAT_REL_HOME_PHONE` | VARCHAR |  | Contact's home phone |
| 9 | `PAT_REL_WORK_PHONE` | VARCHAR |  | Contact's work phone |
| 10 | `PAT_REL_MOBILE_PHNE` | VARCHAR |  | Contact's mobile phone |
| 11 | `PAT_REL_LGL_GUAR_YN` | VARCHAR |  | Whether this contact is the patient's legal guardian |
| 12 | `PAT_REL_REC_LINK_ID` | VARCHAR |  | Links this contact to a patient record |
| 13 | `PAT_REL_RELATION_C_NAME` | VARCHAR | org | Contact's relation to patient |
| 14 | `PAT_REL_PRIM_PH_C_NAME` | VARCHAR |  | Which of the contact's phone numbers should be considered primary |
| 15 | `PAT_REL_GEN_STR_1` | VARCHAR |  | Customer labeled string item |
| 16 | `PAT_REL_GEN_STR_2` | VARCHAR |  | Customer labeled string item |
| 17 | `PAT_REL_GEN_STR_3` | VARCHAR |  | Customer labeled string item |
| 18 | `PAT_REL_GEN_STR_4` | VARCHAR |  | Customer labeled string item |
| 19 | `PAT_REL_GEN_CAT_1_C_NAME` | VARCHAR | org | Customer labeled category item |
| 20 | `PAT_REL_GEN_CAT_2_C_NAME` | VARCHAR | org | Customer labeled category item |
| 21 | `PAT_REL_GEN_CAT_3_C_NAME` | VARCHAR | org | Customer labeled category item |
| 22 | `PAT_REL_GEN_CAT_4_C_NAME` | VARCHAR | org | Customer labeled category item |
| 23 | `PAT_REL_HOUSE_NUM` | VARCHAR |  | Contact's House Number |
| 24 | `PAT_REL_DISTRICT_C_NAME` | VARCHAR | org | The district category ID for the patient's contact. |
| 25 | `PAT_REL_HEARING_YN` | VARCHAR |  | Capture if patient's relative has hearing impairment |
| 26 | `PAT_REL_VISUALLY_YN` | VARCHAR |  | Capture if patient's relative has visual impairment |
| 27 | `PAT_REL_IMP_NEEDS_C_NAME` | VARCHAR | org | Capture the patient's emergency contact's special needs for hearing and visual impairment. |
| 28 | `PAT_REL_SPOKEN_C_NAME` | VARCHAR | org | Capture the patient's emergency contact's spoken language. |
| 29 | `PAT_REL_WRITTEN_C_NAME` | VARCHAR |  | Capture the patient's emergency contact's written language. |
| 30 | `PAT_REL_PREF_LANG_C_NAME` | VARCHAR |  | Capture the patient's emergency contact's preferred language. |
| 31 | `PAT_REL_INTERPRET_YN` | VARCHAR |  | Capture if the patient's emergency contact needs an interpreter. |
| 32 | `PAT_REL_SPL_NEEDS_C_NAME` | VARCHAR | org | Capture the patient's emergency contact's special needs. |
| 33 | `PAT_REL_NOTIFY_YN` | VARCHAR |  | Capture if the patient's emergency contact should be notified on patient's admission. |
| 34 | `PAT_LEGAL_REL_C_NAME` | VARCHAR | org | Specifies the category for the legal relationship |
| 35 | `PAT_REL_ACT_AGNT_YN` | VARCHAR |  | Specifies if the health care agent is active or not |
| 36 | `PAT_REL_EMAIL` | VARCHAR |  | Primary email address of the patient's emergency contact. |
| 37 | `PAT_REL_RLA_ID` | NUMERIC |  | Links this patient contact to the associated Patient Relationships (RLA) patient relationship record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

