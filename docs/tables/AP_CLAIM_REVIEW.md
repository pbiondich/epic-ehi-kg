# AP_CLAIM_REVIEW

> The AP_CLAIM_REVIEW table contains a row for each review on a claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AP_CLAIM_REVIEW_TYPE_C_NAME` | VARCHAR | org | The review type category ID for the review on the claim. |
| 4 | `ATTACH_COMMENT` | VARCHAR |  | The comment associated with a review when it is attached to a claim. |
| 5 | `AP_CLAIM_REVIEW_STATUS_C_NAME` | VARCHAR |  | The review status category ID for the review on the claim. |
| 6 | `ATTACH_DTTM` | DATETIME (Local) |  | The date and time the associated review was attached to the claim. |
| 7 | `COMPLETION_COMMENT` | VARCHAR |  | The comment entered by the user who completed the associated review. |
| 8 | `COMPLETION_DTTM` | DATETIME (Local) |  | The completion date and time for the associated review. |
| 9 | `REJECTION_EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 10 | `ADDED_MANUALLY_YN` | VARCHAR |  | Indicates whether this review was added manually by an end user. 'Y' indicates that the review was added manually. 'N' or NULL indicate that the review was added by the system. |
| 11 | `REVIEW_STATUS_REASON_C_NAME` | VARCHAR |  | The review status reason category ID for the review on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

