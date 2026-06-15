# GYN_CCS_FOLLOWUP_REPL

> This table should not be queried directly. It is used by the GYN_CCS_FOLLOWUP view and will ultimately be deprecated. This table contains the cervical cancer screening follow-up actions for patients.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GYN_FOLLOWUP_C_NAME` | VARCHAR | org | Follow-up action that has been set for the patient. |
| 4 | `GYN_FOLLOWUP_USER_ID` | VARCHAR |  | The user that entered the follow-up action. |
| 5 | `GYN_FOLLOWUP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `GYN_FOLLOWUP_DTTM` | DATETIME (UTC) |  | The instant that the follow-up action is entered. |
| 7 | `GYN_FOLLOWUP_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `GYN_FOLLOWUP_DUE_DATE` | DATETIME |  | Stores the due date for the related Cervical Cancer Screening follow-up actions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

