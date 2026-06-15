# PATIENT_PREF_TIME

> The PATIENT_PREF_TIME table contains information of the patient's preferred appointment times during the day.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The ID of the patient with the preferred appointment time. |
| 2 | `LINE` | INTEGER | PK | The line number of the preferred appointment time of the patient. |
| 3 | `PREF_TIME_BEGIN` | DATETIME (Local) |  | The patient's preferred begin time of the day for appointments. Note: There is no corresponding datatype to Time in enterprise reporting. To work around this, concatenate a default date (01/01/1900) in front of the time. |
| 4 | `PREF_TIME_END` | DATETIME (Local) |  | The patient's preferred end time of the day for appointments. Note: There is no corresponding datatype to Time in enterprise reporting. To work around this, concatenate a default date (01/01/1900) in front of the time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

