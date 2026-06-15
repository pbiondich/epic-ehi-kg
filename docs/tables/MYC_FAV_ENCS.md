# MYC_FAV_ENCS

> Stores the CSN of appointments that the MyChart user saved as a favorite so the data can be used to schedule again.

**Primary key:** `MYPT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYPT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the patient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAV_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the CSN of appointments that the MyChart user saved as a favorite. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAV_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

