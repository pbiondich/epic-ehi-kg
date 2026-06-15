# HSP_PREADM_TEST

> The HSP_PREADM_TEST table contains information on preadmission testing. Each record in this table is based on PAT_ENC_CSN_ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient with this preadmission test. |
| 2 | `LINE` | INTEGER | PK | The line number of the preadmission test for the patient. |
| 3 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `PREADM_TST_STAT_C_NAME` | VARCHAR | org | The category value corresponding to the status of the preadmission test for the patient. |
| 5 | `PROC_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 6 | `PREADM_APPT_NOTE` | VARCHAR |  | Free text note associated with preadmission test appointment for the patient. |
| 7 | `PREADM_TST_PRI_C_NAME` | VARCHAR | org | The priority category of the preadmission test for the patient. |
| 8 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

