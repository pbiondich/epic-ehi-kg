# RESERVATION_INFORMATION

> Admission planning reservation information.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `RESRC_TYPE_ID_TANK_NAME` | VARCHAR |  | The name of the tank record. |
| 8 | `RESRC_SUBTYPE_C_NAME` | VARCHAR | org | Type of stay for patient's reservation at the hospital. |
| 9 | `SCHED_ARRIVAL_DATE` | DATETIME |  | Scheduled arrival date for the patient's hospital stay reservation. |
| 10 | `SCHED_ARRIVAL_TIME_C_NAME` | VARCHAR | org | Scheduled arrival time for the patient's hospital stay reservation. |
| 11 | `SCHED_DEPARTURE_DATE` | DATETIME |  | Scheduled departure date for the patient's hospital stay reservation. |
| 12 | `SCHED_DEPARTURE_TIME_C_NAME` | VARCHAR |  | Scheduled departure time for the patient's hospital stay reservation. |
| 13 | `RESV_INDFNT_YN` | VARCHAR |  | Determine if this reservation is an indefinite stay. |
| 14 | `RESV_CONFRM_YN` | VARCHAR |  | If this reservation has been confirmed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

