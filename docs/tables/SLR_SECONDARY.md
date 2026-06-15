# SLR_SECONDARY

> This table stores secondary review data from second-level reviews.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the second-level review. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `SEC_GENERIC_DETERM_C_NAME` | VARCHAR |  | The category ID of the reviewer's determination. For "other" reviews only. |
| 4 | `SEC_NECESSITY_DETERM_C_NAME` | VARCHAR |  | The category ID of the reviewer's determination of how necessary a procedure is. For medical necessity reviews only. |
| 5 | `SEC_LOS_DETERM_C_NAME` | VARCHAR |  | The category ID of the reviewer's determination of the patient's length of stay. For length of stay reviews only. |
| 6 | `SEC_DISCHARGE_DETERM_C_NAME` | VARCHAR |  | The category ID of the reviewer's determination of the patient's readiness for discharge. For discharge reviews only. |
| 7 | `SEC_SUG_ACUTE_LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The category ID of the acute level of care suggested in the secondary review request. Used in acute level of care reviews only. |
| 8 | `SEC_SUG_POST_ACUTE_CLASS_C_NAME` | VARCHAR |  | The category ID of the post-acute class suggested in the secondary review request. Used in post-acute level of care reviews only. |
| 9 | `SEC_SUG_ACUITY_LEVEL_C_NAME` | VARCHAR | org | The category ID of the acuity level suggested in the secondary review request. Used in acuity level reviews only. |
| 10 | `SEC_REC_ACUTE_LEVEL_OF_CARE_C_NAME` | VARCHAR |  | The category ID of the patient's acute level of care recommended by the secondary reviewer. Used in acute level of care reviews only. |
| 11 | `SEC_REC_POST_ACUTE_CLASS_C_NAME` | VARCHAR |  | The category ID of the patient's post-acute class recommended by the secondary reviewer. Used in post-acute level of care reviews only. |
| 12 | `SEC_REC_ACUITY_LEVEL_C_NAME` | VARCHAR |  | The category ID of the patient's acuity level recommended by the secondary reviewer. Used in acuity level reviews only. |
| 13 | `SEC_SUG_BASE_CLASS_C_NAME` | VARCHAR |  | The category ID of the base patient class suggested in the secondary review request. Used in patient class reviews only. |
| 14 | `SEC_REC_BASE_CLASS_C_NAME` | VARCHAR |  | The category ID of the base patient class recommended by the secondary reviewer. Used in patient class reviews only. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

