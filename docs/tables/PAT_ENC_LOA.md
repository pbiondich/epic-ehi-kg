# PAT_ENC_LOA

> This table contains the leave of absence start and end information for a patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `LOA_START_DTTM` | DATETIME (UTC) |  | The start instant for a leave of absence that occurred during the given encounter. |
| 7 | `LOA_START_EVENT_ID` | NUMERIC |  | The unique ID of the event that started the leave of absence. |
| 8 | `LOA_END_DTTM` | DATETIME (UTC) |  | The end instant for a leave of absence that occurred during the given encounter. |
| 9 | `LOA_END_EVENT_ID` | NUMERIC |  | The unique ID of the event that ended the leave of absence. |
| 10 | `LOA_START_LOCAL_DTTM` | DATETIME (Local) |  | The start instant for a leave of absence that occurred during the given encounter, in local time. |
| 11 | `LOA_END_LOCAL_DTTM` | DATETIME (Local) |  | The end instant for a leave of absence that occurred during the given encounter, in local time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

