# SLR_REVIEW

> This table stores type-agnostic review data for second-level reviews.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 15  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the second-level review. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `SLR_REVIEW_STATUS_C_NAME` | VARCHAR |  | The category ID of the step in the second-level review process that this second-level review is in. |
| 4 | `REVIEW_MEDICAL_CONTEXT_C_NAME` | VARCHAR |  | The category ID of the specific medical context of the second-level review that is being completed (e.g. level of care, medical necessity, discharge). |
| 5 | `POLICY_REGULATION_C_NAME` | VARCHAR | org | The category ID of the policy or regulation that was being followed when making this second-level review. |
| 6 | `DUE_DATE` | DATETIME |  | The due date for the review set by user creating the request. |
| 7 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID of the coverage associated with this second-level review. |
| 8 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `EXPECTED_LENGTH_OF_STAY` | INTEGER |  | The requesting user's expected amount of time the patient should remain in care. For length of stay and discharge reviews only. |
| 10 | `CURRENT_ACUTE_LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The acute level of care category ID for the second-level review at time of request. Used in acute level of care reviews only. |
| 11 | `CURRENT_POST_ACUTE_CLASS_C_NAME` | VARCHAR |  | The post-acute class category ID for the second-level review at time of request. Used in post-acute level of care reviews only. |
| 12 | `CURRENT_ACUITY_LEVEL_C_NAME` | VARCHAR | org | The acuity level category ID for the second-level review at time of request. Used in acuity reviews only. |
| 13 | `ADVISOR_USER_ID` | VARCHAR |  | The unique ID associated with the physician advisor's user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `ADVISOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `CURRENT_BASE_CLASS_C_NAME` | VARCHAR |  | The base patient class category ID for the second-level review at time of request. Used in patient class reviews only. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

