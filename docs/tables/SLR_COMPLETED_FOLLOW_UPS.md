# SLR_COMPLETED_FOLLOW_UPS

> This table stores the completed follow-ups for a second-level review.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the review record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COMP_FOL_UP_C_NAME` | VARCHAR | org | The completed follow-up category ID for the second-level review. |
| 5 | `COMP_FOL_UP_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant that the follow-up was completed, stored as UTC Time. |
| 6 | `COMP_FOL_UP_USER_ID` | VARCHAR |  | The unique ID associated with the user record that completed this follow-up. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `COMP_FOL_UP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `COMP_FOL_UP_DEL_YN` | VARCHAR |  | Indicates whether the completed follow-up was deleted by the user that marked it complete ("Y") or not ("N" or "NULL"). |
| 9 | `COMP_FOL_UP_INST_LOCAL_DTTM` | DATETIME (Attached) |  | The instant that the follow-up was completed, stored as local (patient encounter) time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

