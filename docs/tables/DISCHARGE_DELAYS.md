# DISCHARGE_DELAYS

> Holds the discharge delays on a patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `DD_DELAY_C_NAME` | VARCHAR | org | Discharge delay |
| 7 | `DD_ADDED_AT_DDTM_DTTM` | DATETIME (UTC) |  | Instant discharge delay was added |
| 8 | `DD_RESOLVED_AT_DTTM` | DATETIME (UTC) |  | When the discharge delay was resolved |
| 9 | `DD_COMMENT` | VARCHAR |  | Holds the comment entered by users on a delay |
| 10 | `DD_STATUS_C_NAME` | VARCHAR |  | Holds the current status of a delay |
| 11 | `DD_IS_PRIMARY_YN` | VARCHAR |  | Indicates whether the delay is primary. Y indicates that the delay is primary. A null value indicates that the delay is not primary. An N will not be populated for this column. |
| 12 | `DD_ADDED_AT_DDTM_LOCAL_DTTM` | DATETIME (Local) |  | Local instant discharge delay was added |
| 13 | `DD_RESOLVED_AT_LOCAL_DTTM` | DATETIME (Local) |  | When the discharge delay was resolved in the local time zone |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

