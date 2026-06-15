# COD_RECORD_INFO

> This table stores information about Clinical Documentation Improvement (CDI) reviews.

**Primary key:** `CODING_RECORD_ID`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the coding record. |
| 2 | `RECORD_NAME` | VARCHAR |  | The name of the patient associated with the coding record at the time the coding record was created. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status of the coding record (hidden, soft-deleted, etc.). |
| 4 | `COD_RCD_TYPE_C_NAME` | VARCHAR |  | The record type of the coding record. |
| 5 | `RECORD_CREATION_DT` | DATETIME |  | The creation date of the coding record. |
| 6 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account which is linked to the coding record. |
| 7 | `CDI_STATUS_C_NAME` | VARCHAR | org | The current clinical documentation improvement (CDI) status of the account. |
| 8 | `CDI_ASGN_USER_ID` | VARCHAR |  | This item stores the clinical documentation improvement (CDI) user currently assigned to this account. |
| 9 | `CDI_ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `CDI_STATUS_COMMENT` | VARCHAR |  | The comment associated with the current clinical documentation improvement (CDI) status. |
| 11 | `RA_CDI_PAT_ID` | VARCHAR | FK→ | The patient that this COD record is for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `RA_CDI_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

