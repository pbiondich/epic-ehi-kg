# NHSN_CLIP_ABSTNS

> The NHSN_CLIP_ABSTNS table contains information from Central Line Insertion Practices abstractions.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 39  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique ID for the CLIP event. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the associated patient record for the CLIP event. |
| 3 | `CUR_STAT_C_NAME` | VARCHAR | org | The current status category ID of the CLIP event. |
| 4 | `CUR_STAT_USER_ID` | VARCHAR |  | The internal ID of the user who set the current abstraction status for the CLIP event. |
| 5 | `CUR_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CUR_STAT_DTTM` | DATETIME (UTC) |  | The date and time when the current abstraction status was set for the CLIP event. |
| 7 | `CREATION_DATE` | DATETIME |  | The date when the CLIP event was created. |
| 8 | `NHSN_INSERTION_DATE` | DATETIME |  | The date when the central line was inserted for the CLIP event. |
| 9 | `NHSN_RECORDER_C_NAME` | VARCHAR |  | The recorder category ID for the CLIP event. |
| 10 | `NHSN_INSRTR_EMP_ID` | VARCHAR |  | The unique ID of the employee who inserted the central line for the CLIP event. |
| 11 | `NHSN_INSRTR_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `NHSN_INSERTER_JOB_C_NAME` | VARCHAR |  | The occupation category ID of the central line inserter for the CLIP event. |
| 13 | `NHSN_ON_PICC_TEAM_YN` | VARCHAR |  | Stores whether the central line inserter was a member of the PICC/IV team. |
| 14 | `NHSN_INSRTN_RSN_C_NAME` | VARCHAR |  | The reason category ID for the central line insertion for the CLIP event. |
| 15 | `NHSN_GUIDEWIRE_YN` | VARCHAR |  | Indicates whether the central line was exchanged over a guidewire for the CLIP event. This column is only populated if NHSN_INSRTN_RSN_C has a value of 3 - Suspected central line-associated infection. |
| 16 | `NHSN_HAND_HYGIENE_YN` | VARCHAR |  | Indicates whether hand hygiene was performed prior to the central line insertion for the CLIP event. |
| 17 | `NHSN_WORE_MASK_YN` | VARCHAR |  | Indicates whether a sterile mask was worn for the central line insertion for the CLIP event. |
| 18 | `NHSN_WORE_GOWN_YN` | VARCHAR |  | Indicates whether a sterile gown was worn for the central line insertion for the CLIP event. |
| 19 | `NHSN_USED_DRAPE_YN` | VARCHAR |  | Indicates whether a sterile drape was used for the central line insertion for the CLIP event. |
| 20 | `NHSN_WORE_GLOVES_YN` | VARCHAR |  | Indicates whether sterile gloves were worn for the central line insertion for the CLIP event. |
| 21 | `NHSN_WORE_CAP_YN` | VARCHAR |  | Indicates whether a sterile cap was worn for the central line insertion for the CLIP event. |
| 22 | `NHSN_PREP_CHG_YN` | VARCHAR |  | Indicates whether chlorhexidine gluconate was used as a skin prep agent for the central line insertion for the CLIP event. |
| 23 | `NHSN_PREP_IODINE_YN` | VARCHAR |  | Indicates whether povidone iodine was used as a skin prep agent for the central line insertion for the CLIP event. |
| 24 | `NHSN_PREP_ALCOHOL_YN` | VARCHAR |  | Indicates whether alcohol was used as a skin prep agent for the central line insertion for the CLIP event. |
| 25 | `NHSN_PREP_OTHER_YN` | VARCHAR |  | Indicates whether any other agent (aside from chlorhexidine gluconate, povidone iodine, or alcohol) was used as a skin prep agent for the central line insertion for the CLIP event. |
| 26 | `NHSN_CHG_CONTRAIND_C_NAME` | VARCHAR |  | The CHG contraindication category ID for the central line insertion for the CLIP event. This column is only populated if NHSN_PREP_CHG_YN has a value of N. |
| 27 | `NHSN_PREP_DRY_YN` | VARCHAR |  | Indicates whether the skin prep agent used was dry at the time of central line insertion for the CLIP event. |
| 28 | `NHSN_INSRTN_SITE_C_NAME` | VARCHAR |  | The insertion site category ID for the central line insertion for the CLIP event. |
| 29 | `NHSN_COATED_CATH_YN` | VARCHAR |  | Indicates whether an antimicrobial coated catheter was used for this central line insertion for the CLIP event. |
| 30 | `NHSN_CL_CATH_TYPE_C_NAME` | VARCHAR |  | The catheter type category ID for the central line insertion for the CLIP event. |
| 31 | `NHSN_CL_SUCCESS_YN` | VARCHAR |  | Indicates whether the central line insertion was successful for the CLIP event. |
| 32 | `NHSN_OTHER_JOB` | VARCHAR |  | The occupation of the person inserting a central line for the CLIP event. This column is only populated if NHSN_INSERTER_JOB_C has a value of 10 - Other. |
| 33 | `NHSN_OTHER_RSN` | VARCHAR |  | The reason for a central line for the CLIP event. This column is only populated if NHSN_INSRTN_RSN_C has a value of 4 - Other. |
| 34 | `NHSN_OTHER_PREP` | VARCHAR |  | The skin prep agent used for a central line for the CLIP event. This column is only populated if NHSN_PREP_OTHER_YN has a value of Y. |
| 35 | `NHSN_OTHER_CL_TYPE` | VARCHAR |  | The catheter type used during a central line insertion for the CLIP event. This column is only populated if NHSN_CL_CATH_TYPE_C has a value of 7 - Other. |
| 36 | `NHSN_CHG_AGE_YN` | VARCHAR |  | Indicates whether the patient was less than 2 months old when the central line was inserted for the CLIP event. This column is only populated if NHSN_CHG_CONTRAIND_C has a value of 1 - Yes. |
| 37 | `NHSN_CHG_ALLERGY_YN` | VARCHAR |  | Indicates whether the patient has an allergy to chlorhexidine gluconate for the CLIP event. This column is only populated if NHSN_CHG_CONTRAIND_C has a value of 1 - Yes. |
| 38 | `NHSN_CHG_SAFETY_YN` | VARCHAR |  | Indicates whether facility restrictions or safety concerns for chlorhexidine gluconate use in premature infants precludes its use for the CLIP event. This column is only populated if NHSN_CHG_CONTRAIND_C has a value of 1 - Yes. |
| 39 | `ASSOCIATED_LOC_NHSN_DEF_ID_CMS_MU_NAME` | VARCHAR |  | The name of the CMS Meaningful Use record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

