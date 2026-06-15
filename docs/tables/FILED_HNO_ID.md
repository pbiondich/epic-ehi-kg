# FILED_HNO_ID

> This table extracts the Visit Narrative - Filed HNO (I EPT 18163) item, which stores the Notes (HNO) IDs of transcriptions which have a status of available (authenticated) and originated from a dictation in Hyperspace.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | Stores the line count. |
| 3 | `CONTACT_DATE` | DATETIME |  | Stores the contact date in the patient record that is associated with the transcription. |
| 4 | `FILED_HNO_ID` | VARCHAR | discont. | This item stores the note identifier for an available transcription. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

