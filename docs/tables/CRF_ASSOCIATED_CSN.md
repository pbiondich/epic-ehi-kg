# CRF_ASSOCIATED_CSN

> CRF table for information related to the patient CSN's.

**Primary key:** `REF_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REF_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_DATA_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This stores the patient contact serial numbers associated with the CRF. This is the counterpart on a shared instance of the encounter event ID's on a payer platform instance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REF_DATA_ID` | [CLAIM_REFERENCE_DATA](CLAIM_REFERENCE_DATA.md) | sole_pk | high |
| `REF_DATA_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

