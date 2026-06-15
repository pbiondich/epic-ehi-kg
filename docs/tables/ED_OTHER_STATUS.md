# ED_OTHER_STATUS

> The ED_OTHER_STATUS table contains information about ED patients' "other" status. One row in this table corresponds to one ED "other" status change. If a patient's ED "other" status is changed five times in a single encounter, this table will contain five rows for that encounter.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID associated with the Inpatient Data Store record for this row. This column is frequently used to link to PAT_ENC_HSP.INPATIENT_DATA_ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this status. Multiple pieces of information can be associated with this record. |
| 3 | `ED_OTHR_STATUS_C_NAME` | VARCHAR | org | The category number of the ED other status for the ED encounter. This can include statuses like "Bed Assigned" or "Transportation Called." |
| 4 | `OTHR_STATUS_TIME` | DATETIME (Local) |  | The date and time when the ED other status was set. This can include statuses like "Bed Assigned" or "Transportation Called." |
| 5 | `OTHR_STATUS_USER_ID` | VARCHAR |  | The unique ID of the user who is associated with this status change. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `OTHR_STATUS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). This column is frequently used to link to PAT_ENC_HSP.PAT_ENC_CSN_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

