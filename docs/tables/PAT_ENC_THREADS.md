# PAT_ENC_THREADS

> This table contains information regarding a telephone encounter and any related messages.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `THREAD_ID` | NUMERIC | FK→ | The unique ID of the thread for a telephone encounter that was sent to another user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

