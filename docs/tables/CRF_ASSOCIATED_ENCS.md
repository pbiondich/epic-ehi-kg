# CRF_ASSOCIATED_ENCS

> Table of Encounter Event IDs associated with a Claim Reference Data collection.

**Primary key:** `REF_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REF_DATA_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Reference Data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENC_EVENT_IDENT` | VARCHAR |  | An Encounter Event ID associated with the Claim Reference Data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REF_DATA_ID` | [CLAIM_REFERENCE_DATA](CLAIM_REFERENCE_DATA.md) | sole_pk | high |

