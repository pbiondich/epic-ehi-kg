# PAT_ENC_DELIVRY_HX

> The PAT_ENC_DELIVRY_HX table contains information on inpatient ADT-related labor & delivery status history.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | FK→ | The unique ID for the patient whose labor & delivery history this is. |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | The patient encounter contact date in internal format. |
| 3 | `LINE` | INTEGER | PK | The line count field for the maternal delivery history related group. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The contact serial number for the patient encounter. |
| 5 | `CONTACT_DATE` | DATETIME |  | The patient encounter contact date in external format. |
| 6 | `DLVR_HX_STAT_C_NAME` | VARCHAR |  | The labor & delivery history status (no released values). |
| 7 | `DLVR_HX_DATETIME` | DATETIME (Local) |  | The date and time a patient's labor and delivery status changed. |
| 8 | `DLVR_HX_NOTES` | VARCHAR |  | The labor & delivery history notes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

