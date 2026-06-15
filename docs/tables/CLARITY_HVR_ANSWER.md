# CLARITY_HVR_ANSWER

> This table stores the answer record (HQA) IDs that are associated with the verification records.

**Primary key:** `VERIFY_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERIFY_ID` | NUMERIC | PK FK→ | The unique ID of the verification record |
| 2 | `LINE` | INTEGER | PK | This column holds the line number corresponding to the line of the answer. Each answer associated with the verification record will be stored on a separate line. |
| 3 | `VERIFY_ANS_ID` | VARCHAR |  | The unique ID of the verification answer record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERIFY_ID` | [CLARITY_HVR](CLARITY_HVR.md) | sole_pk | high |

