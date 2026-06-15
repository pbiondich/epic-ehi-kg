# DXR_REVIEW_INFO

> This table holds information about users who have reviewed the document.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVIEW_USER_ID` | VARCHAR |  | This holds the ID of the user who reviewed this document. |
| 4 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVIEW_USER_DTTM` | DATETIME (UTC) |  | This item holds the instant that a review happened. |
| 6 | `REVIEW_ENC_CSN` | NUMERIC | FK→ | This item holds the CSN of an encounter where a review happened. This item will only be populated if the review happened within an encounter context. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

