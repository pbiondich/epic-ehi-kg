# FAMILY_HX_STATUS

> Family status relationship table. Contains the relationship to the patient and the name of the family member, as well as the source of this information.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `FAM_STAT_REL_C_NAME` | VARCHAR | org | The family status relationship category number for the relationship between the patient and their family member. |
| 5 | `FAM_STAT_STATUS_C_NAME` | VARCHAR |  | The family status category number for the family member, such as 1 for "alive" and 2 for "deceased". |
| 6 | `FAM_STAT_DEATH_AGE` | VARCHAR |  | Age of family member at their death. |
| 7 | `FAM_STAT_COMMENT` | VARCHAR |  | This item contains the free text comments associated with a patient's family member status in medical history. |
| 8 | `FAM_STAT_NAME` | VARCHAR |  | The name of family member. |
| 9 | `FAM_STAT_SRC_C_NAME` | VARCHAR | org | The family status source category number for the source of corresponding family status information. |
| 10 | `HX_LNK_ENC_CSN` | NUMERIC | FK→ | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| 11 | `FAM_STAT_DOB_DT` | DATETIME |  | This is used to calculate the age of a relative. This is either the date of birth (approximate or exact) or part of a range. If it is a range, then this column will be the beginning date and FAM_STAT_DOB_END_DT will store the end date. This range of dates is used to define an age range. |
| 12 | `FAM_STAT_ID` | INTEGER |  | The Unique ID for the family member. |
| 13 | `FAM_STAT_FATHER_ID` | INTEGER |  | Unique ID for the Father |
| 14 | `FAM_STAT_MOTHER_ID` | INTEGER |  | Unique ID for the mother. |
| 15 | `FAM_STAT_DOB_END_DT` | DATETIME |  | If an age range is entered for a family member, then the range is stored as two dates. This column holds the end date and FAM_STAT_DOB_DT holds the beginning date. |
| 16 | `FAM_STAT_TWIN` | INTEGER |  | This item tracks twin relationships among members of the patient's family. Two family members who are twins (or three who are triplets, etc.) will have the same value on their lines of this item. A value of 0 indicates that the family member is a twin of the patient. |
| 17 | `FAM_STAT_IDENT_TWIN` | INTEGER |  | This item tracks identical twin relationships among members of the patient's family. Two family members who are identical twins (or three who are identical triplets, etc.) will have the same value on their lines of this item. A value of 0 indicates that the family member is an identical twin of the patient. |
| 18 | `FAM_STAT_COD_C_NAME` | VARCHAR | org | The cause of death of a family member of the patient. |
| 19 | `FAM_STAT_SEX_C_NAME` | VARCHAR |  | This item stores the sex of a family member of the patient. |
| 20 | `FAM_STAT_GENDER_IDENTITY_C_NAME` | VARCHAR | org | Gender identity for a family member. |
| 21 | `FAM_STAT_REL_ID` | NUMERIC |  | This item stores the unique ID of the patient relationship record. The patient relationship record contains information about how the person is related to the patient. |
| 22 | `FAM_STAT_ADOPT_C_NAME` | VARCHAR |  | Adoption status of a particular family member. |
| 23 | `FAM_STAT_ADPT_PAR_1` | INTEGER |  | The ID of a relative's adoptive parent. We allow two adoptive parents. The other adoptive parent ID is stored in I EPT 20359. |
| 24 | `FAM_STAT_ADPT_PAR_2` | INTEGER |  | The ID of a relative's adoptive parent. We allow two adoptive parents. The other adoptive parent ID is stored in I EPT 20358. |
| 25 | `FAM_STAT_PREG_EPISODE_ID` | NUMERIC |  | This item stores a link to the patient's pregnancy information in Obstetric history. |
| 26 | `FAM_STAT_DELIV_EPISODE_ID` | NUMERIC |  | This item stores a link to the patient's delivery information for Obstetric History. |
| 27 | `FAM_HX_FERT_STAT_C_NAME` | VARCHAR |  | This field contains the category value representing a patient's relative's fertility status. |
| 28 | `FAM_HX_FERT_NOTE` | VARCHAR |  | This field is a free text item holding notes pertaining to a particular relative's fertility status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HX_LNK_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

