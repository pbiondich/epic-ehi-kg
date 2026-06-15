# PATIENT_VIDEO_VISIT

> This table contains the video visit related data for a patient that is stored at the patient level.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_LVL_VIDEO_VISIT_ID` | NUMERIC |  | Stores the video visit record ID for a patient level visit. |
| 4 | `PAT_LVL_VIDEO_VISIT_TYP_C_NAME` | VARCHAR |  | Stores the type of video visit record for patient level video visits. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

