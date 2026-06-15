# SAVED_LETTER_HNO

> This table stores Health Information Management (HIM)-specific information about printed letters.

**Primary key:** `NOTE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note record for this row. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

