# HSP_DEATH_STATUS

> The HSP_DEATH_STATUS table contains information on the death status of inpatients.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The ID of the patient with this legal status. |
| 2 | `LINE` | INTEGER | PK | The line number of the legal status for the patient. |
| 3 | `DEATH_LEGAL_STAT_C_NAME` | VARCHAR | org | The category value corresponding to the legal status for the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

