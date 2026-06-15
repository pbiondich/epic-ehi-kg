# PRIMUS_SCHOOL_INFO

> Table containing the Primus school info items in related group 82130.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCHOOL_NAME_C_NAME` | VARCHAR | org | The history of schools this patient attended. This data is received from Primus. |
| 4 | `EDUCATION_STATUS_C_NAME` | VARCHAR | org | The history of a patient's education status. This data is received from Primus. |
| 5 | `CLASS_C_NAME` | VARCHAR | org | The history of grades a patient was in. This data is received from Primus. |
| 6 | `CLASS_GROUP_C_NAME` | VARCHAR | org | The history of class groups a patient was in. This data is received from Primus. |
| 7 | `PRIMUS_VAL_FRM_UTC_DTTM` | DATETIME (UTC) |  | The history of start dates for related group School Name (I EPT 82130). This data is received from Primus. |
| 8 | `PRIMUS_VAL_TO_UTC_DTTM` | DATETIME (UTC) |  | The history of end dates for related group School Name (I EPT 82130). This data is received from Primus. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

