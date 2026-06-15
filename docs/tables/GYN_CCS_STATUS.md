# GYN_CCS_STATUS

> This table contains the cervical cancer screening tracking status for patients.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GYN_CCS_STATUS_C_NAME` | VARCHAR | org | The patient's cervical cancer screening tracking status. |
| 4 | `GYN_CCS_UPD_USER_ID` | VARCHAR |  | The user that updated the patient's tracking status. |
| 5 | `GYN_CCS_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `GYN_CCS_UPD_DTTM` | DATETIME (UTC) |  | The instant that the tracking status is updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

