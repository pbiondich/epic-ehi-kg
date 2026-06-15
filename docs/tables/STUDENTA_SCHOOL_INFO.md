# STUDENTA_SCHOOL_INFO

> Table containing the Studenta school info items in related group 82150.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCHOOL_LOCATION_C_NAME` | VARCHAR | org | The history of schools this patient attended. This data is received from Studenta. |
| 4 | `DEGREE_C_NAME` | VARCHAR | org | The history of degrees a patient had. This data is received from Studenta. |
| 5 | `START_GROUP_C_NAME` | VARCHAR | org | The history of start groups a patient was in. This data is received from Studenta. |
| 6 | `DEGREE_START_DATE` | DATETIME |  | The history of start dates of degrees a patient had. This data is received from Studenta. |
| 7 | `STDENTA_VAL_FRM_UTC_DTTM` | DATETIME (UTC) |  | The history of start dates for a patient's school information. This data is received from Studenta. |
| 8 | `STDENTA_VAL_TO_UTC_DTTM` | DATETIME (UTC) |  | The history of end dates for a patient's school information. This data is received from Studenta. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

