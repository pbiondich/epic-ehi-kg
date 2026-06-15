# HAR_ALL

> Generic table that contains every hospital account record regardless of its type. It also contains the patient record that is associated with the hospital account.

**Primary key:** `ACCT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `PAT_ID` | VARCHAR | FK→ | This column stores the unique identifier for the patient associated with this hospital account. |
| 3 | `PRIM_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number associated with the primary patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PRIM_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

