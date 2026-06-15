# HSP_PREADM_CONFRM

> This table contains information on a confirmed preadmission. Each record in this table is based on patient contact serial number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | FK→ | This column stores the unique identifier for the patient that was preadmission confirmed. |
| 2 | `LINE` | INTEGER | PK | The line number of the preadmission confirmed for the patient. |
| 3 | `PREADM_CONFRM_INST` | DATETIME (Local) |  | Instant when the preadmission was confirmed. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | This column stores the unique contact serial number for the encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

