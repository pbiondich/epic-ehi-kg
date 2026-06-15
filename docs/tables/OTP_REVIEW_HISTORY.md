# OTP_REVIEW_HISTORY

> This table contains the review history for a given patient order template. The review history consists of the review action, the reviewing user, and the instant of review.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORD_REVIEW_STATUS_C_NAME` | VARCHAR |  | The review status category ID of an order in the treatment plan manager. An order can be unreviewed, reviewed, or changed since it was last reviewed. |
| 4 | `ORD_REV_UPDT_USR_ID` | VARCHAR |  | The unique ID of the user who changed the review status for the patient order template record. |
| 5 | `ORD_REV_UPDT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ORD_REVIEW_UPDT_TM` | DATETIME (Local) |  | The date and time the review status stored in the related line in the patient order template was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

