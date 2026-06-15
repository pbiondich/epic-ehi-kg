# SECOND_LEVEL_REVIEWS

> The SECOND_LEVEL_REVIEWS table is the primary table for secondary review and peer-to-peer review information. Each row contains basic information about second-level review records, including the review type and format type.

**Primary key:** `REVIEW_ID`  
**Columns:** 14  
**Joined by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK | The unique identifier for the second-level review. |
| 2 | `SLR_WORKFLOW_CONTEXT_C_NAME` | VARCHAR |  | The category ID of the functional area that this review was created in. |
| 3 | `PAT_ID` | VARCHAR | FK→ | ID of the associated patient that the record was created for. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `REFERRAL_ID` | NUMERIC | FK→ | The unique ID of the associated referral. |
| 6 | `SLR_REVIEW_TYPE_C_NAME` | VARCHAR |  | The category ID of the overall type of review this second-level review holds (secondary or peer-to-peer). |
| 7 | `SLR_FORMAT_TYPE_C_NAME` | VARCHAR |  | The category ID of the second-level review's message format (stand-alone review or review request). |
| 8 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The category ID for the second-level review record status (e.g., hidden or soft-deleted). |
| 9 | `LAST_EDIT_REVIEW_CSN_ID` | NUMERIC |  | The CSN of the most recent contact for this review. |
| 10 | `FIRST_SENT_REVIEW_CSN_ID` | NUMERIC |  | The CSN for the contact where this review was first sent. |
| 11 | `REV_COMPLETE_REVIEW_CSN_ID` | NUMERIC |  | The CSN for the contact where this review was completed by the reviewer. |
| 12 | `ADDL_NOTE_ID` | VARCHAR |  | The unique ID of the note for the additional comments related to the review. |
| 13 | `IN_BASKET_MSG_ID` | VARCHAR |  | The unique ID of the In Basket Message sent containing the second-level review request. |
| 14 | `REVIEW_COMPLETED_LOCAL_DTTM` | DATETIME (Attached) |  | The local (patient encounter) date and time when the second-level review was marked as completed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (11)

| From | Column | Confidence |
|------|--------|------------|
| [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | `REVIEW_ID` | high |
| [SLR_ASSOCIATED_REVIEW](SLR_ASSOCIATED_REVIEW.md) | `REVIEW_ID` | high |
| [SLR_AUDIT](SLR_AUDIT.md) | `REVIEW_ID` | high |
| [SLR_COMPLETED_FOLLOW_UPS](SLR_COMPLETED_FOLLOW_UPS.md) | `REVIEW_ID` | high |
| [SLR_FOLLOW_UP_CMT_TEXT](SLR_FOLLOW_UP_CMT_TEXT.md) | `REVIEW_ID` | high |
| [SLR_P2P](SLR_P2P.md) | `REVIEW_ID` | high |
| [SLR_RATIONALE_TEXT](SLR_RATIONALE_TEXT.md) | `REVIEW_ID` | high |
| [SLR_REQUEST_COMMENT_TEXT](SLR_REQUEST_COMMENT_TEXT.md) | `REVIEW_ID` | high |
| [SLR_REVIEW](SLR_REVIEW.md) | `REVIEW_ID` | high |
| [SLR_REVIEW_COMMENT_TEXT](SLR_REVIEW_COMMENT_TEXT.md) | `REVIEW_ID` | high |
| [SLR_SECONDARY](SLR_SECONDARY.md) | `REVIEW_ID` | high |

