# SLR_P2P

> This table stores peer-to-peer review data for second-level reviews.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the second-level review. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `P2P_OUTCOME_C_NAME` | VARCHAR |  | The category ID of the outcome of the phone call between this organization's physician and the payer. For peer-to-peer reviews only. |
| 4 | `P2P_APPOINTMENT_PHONE` | VARCHAR |  | The phone number the physician or case manager should call to schedule an appointment. For peer-to-peer reviews only. |
| 5 | `P2P_PAYER_REVIEWER_NAME` | VARCHAR |  | The name of the person that this organization's physician will be speaking to. For peer-to-peer reviews only. |
| 6 | `P2P_AUTH_ACUTE_LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The category ID of the acute level of care authorized by the payer for the encounter specified in the peer-to-peer review. Used in acute level of care reviews only. |
| 7 | `P2P_AUTH_POST_ACUTE_CLASS_C_NAME` | VARCHAR |  | The category ID of the post-acute class authorized by the payer for the encounter specified in the peer-to-peer review. Used in post-acute level of care reviews only. |
| 8 | `P2P_AUTH_ACUITY_LEVEL_C_NAME` | VARCHAR | org | The category ID of the acuity level authorized by the payer for the encounter specified in the peer-to-peer review. Used in acuity level reviews only. |
| 9 | `P2P_AUTH_BASE_CLASS_C_NAME` | VARCHAR |  | The category ID of the base patient-class authorized by the payer for the encounter specified in the peer-to-peer review. Used in patient class reviews only. |
| 10 | `P2P_ACTUAL_CALL_DATE` | DATETIME |  | The date when the peer-to-peer call for the peer-to-peer review actually occurred. |
| 11 | `P2P_ACTUAL_CALL_INSTANT_DTTM` | DATETIME (Attached) |  | The instant when the peer-to-peer call for the peer-to-peer review actually occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

