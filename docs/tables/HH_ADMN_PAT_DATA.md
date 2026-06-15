# HH_ADMN_PAT_DATA

> Contains Home Health Admin task data for individual patient contacts.

**Primary key:** `EMP_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EMP_ID` | VARCHAR | PK | The unique identifier of the administration record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATIENT_ID` | VARCHAR |  | Unique identifier for the patient. Links to table PATIENT. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. Links to table PAT_ENC. |
| 5 | `COMMENTS` | VARCHAR |  | Entry in the Admin task Comments field for the contact. |
| 6 | `START_TIME` | DATETIME (Local) |  | Visit start time for encounter-based admin data. |
| 7 | `END_TIME` | DATETIME (Local) |  | Visit end time for encounter-based admin data. |
| 8 | `DRIVING_START_TIME` | DATETIME (Local) |  | Driving start time for encounter-based admin data. |
| 9 | `DRIVING_END_TIME` | DATETIME (Local) |  | Driving end time for encounter-based admin data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

