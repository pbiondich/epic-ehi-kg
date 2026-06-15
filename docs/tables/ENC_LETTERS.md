# ENC_LETTERS

> Information about ADT Encounters Letters.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number of the letter within the encounter. This is the second column in the primary key and, in addition to the contact serial number, uniquely identifies a letter within an encounter. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID assigned to the patient record. |
| 4 | `LETTER_ID` | VARCHAR |  | Encounter Letter to print |
| 5 | `LETTER_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 6 | `UPDATE_INSTANT` | DATETIME (Local) |  | When the letter was last updated (added or printed) |
| 7 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

