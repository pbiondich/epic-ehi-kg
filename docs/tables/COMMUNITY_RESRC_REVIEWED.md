# COMMUNITY_RESRC_REVIEWED

> This table contains the last review information for community resources.

**Primary key:** `PAT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `CBO_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | Stores the most recent instant community resources were reviewed. |
| 3 | `CBO_REVIEW_USER_ID` | VARCHAR |  | Stores the most recent user who reviewed community resources. |
| 4 | `CBO_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CBO_REVIEW_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the most recent CSN of the encounter in which community resources were reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CBO_REVIEW_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

