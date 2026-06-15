# COMMUNITY_RESRC_REVIEW_HX

> This table contains the history of review for community resources for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CBO_HX_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | A history of each instant the user reviewed the community resources. |
| 4 | `CBO_HX_REVIEW_USER_ID` | VARCHAR |  | A history of which user reviewed the community resources. |
| 5 | `CBO_HX_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CBO_HX_REVIEW_PAT_ENC_CSN_ID` | NUMERIC | FK→ | A history of which CSN the community resource was reviewed on. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CBO_HX_REVIEW_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

