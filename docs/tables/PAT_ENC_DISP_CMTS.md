# PAT_ENC_DISP_CMTS

> This table contains the disposition comments for a patient's ED visit.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with these Disposition comments. |
| 2 | `LINE` | INTEGER | PK | The line number of the Disposition comment. |
| 3 | `ED_DISPOSITION_NTS` | VARCHAR |  | The Disposition comments for the patient. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

