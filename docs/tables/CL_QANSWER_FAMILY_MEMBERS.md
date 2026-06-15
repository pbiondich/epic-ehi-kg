# CL_QANSWER_FAMILY_MEMBERS

> This table stores information about the patient's family members that they entered when filling out their family history.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAM_MEM` | VARCHAR |  | The unique identifier of the patient's family member with regards to their family history. |
| 4 | `MSG_CALLER_REL_C_NAME` | VARCHAR | org | The family status relationship category ID for the patient. |
| 5 | `FAM_MEM_NAME_OR_ALIAS` | VARCHAR |  | Patient-created identifier to help the patient differentiate between their family members when filling out their family history. |
| 6 | `FAM_MEM_REMOVE_YN` | VARCHAR |  | Tracks if the associated family member (HQA related group 600) has been requested to be removed from the patient's family history by the user. |
| 7 | `FAM_STAT_STATUS_C_NAME` | VARCHAR |  | Stores family member status. |
| 8 | `FAM_MEM_FATHER_IDENT` | VARCHAR |  | stores id of family member's father |
| 9 | `FAM_MEM_MOTHER_IDENT` | VARCHAR |  | stores id of family member's mother |
| 10 | `FAM_STAT_SEX_C_NAME` | VARCHAR |  | Stores family member sex |
| 11 | `FAM_STAT_GENDER_IDENTITY_C_NAME` | VARCHAR | org | The gender identity of a relative in the patient's family history. |
| 12 | `FAM_MEM_DOB_DATE` | DATETIME |  | The date of birth of a relative in the patient's family history. |
| 13 | `FAM_MEM_DOB_END_DATE` | DATETIME |  | If the relative's date of birth is a "fuzzy" range, holds the end date of the range. |
| 14 | `FAM_MEM_DEATH_AGE` | VARCHAR |  | The age at death of a relative in the patient's family history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

