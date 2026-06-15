# HSP_ADMIT_DIAG

> The HSP_ADMIT_DIAG table contains information on admission diagnoses. This table is based on patient contact serial number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number of the admission diagnosis for the patient. |
| 2 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 3 | `ADMIT_DIAG_TEXT` | VARCHAR |  | Free text admission diagnosis for the patient. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

