# PATIENT_MISC_COMMENTS

> Contains various attached comments for patient items. This table should not be extracted unless there are attached comments on EPT 128, 135, 140, 150, 165, 840, 6100, or 34208. If those items do contain comments, this table should be extracted for EHI compliance.

**Primary key:** `PAT_ID`  
**Columns:** 9  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `RELIGION_C_CMT` | VARCHAR | org | Column to extract comments for EPT-150 Religion. |
| 3 | `ETHNIC_GROUP_C_CMT` | VARCHAR | org | Column to extract comments from EPT-135 Ethnic Group. |
| 4 | `LIVING_ARRANGE_C_CMT` | VARCHAR | org | Column to extract comments from EPT-128 Living Arrangement |
| 5 | `MARITAL_STAT_C_CMT` | VARCHAR | org | Column to extract the comments for EPT-140 Marital Status. |
| 6 | `RELIGIOUS_AFFIL_ID_CMT` | VARCHAR |  | Column to extract the comment from EPT-165 Religious Affiliation. |
| 7 | `IS_ADVANCED_DIR_C_CMT` | VARCHAR |  | Comment to extract comments from EPT-6100 Advance Directives. |
| 8 | `DEATH_INFO_SOURCE_C_CMT` | VARCHAR | org | Column to extract comment from EPT-34208 Death Information Source. |
| 9 | `IS_INTERP_NEED_C_CMT` | VARCHAR |  | Column to extract comments from EPT-840 Needs Interpreter?. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

