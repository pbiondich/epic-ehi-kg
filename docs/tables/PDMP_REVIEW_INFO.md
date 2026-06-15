# PDMP_REVIEW_INFO

> This item holds information on PDMP (Prescription Drug Monitoring Program) review.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVIEW_USER_ID` | VARCHAR |  | This holds the ID of the user who reviewed the PDMP. |
| 4 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVIEW_USER_UTC_DTTM` | DATETIME (UTC) |  | This item holds the instant that the PDMP was reviewed. |
| 6 | `REVIEW_ENC_CSN` | NUMERIC | FK→ | This item holds the CSN of the encounter where the review occurred. It may be null if the PDMP was not reviewed within an encounter context. |
| 7 | `REVIEW_TYPE_C_NAME` | VARCHAR |  | This item indicates whether there was data to review or if the user was unable to retrieve PDMP data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REVIEW_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

