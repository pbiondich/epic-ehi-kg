# PAT_ENC_STAT_HX

> This is the ADT encounter status history. It will track changes to the patient's encounter status (I EPT 10115) and confirmation status (I EPT 18852). The user who made the change, time the change occurred, the new encounter status, and the new confirmation status are recorded. A reason for the change may be provided if the change was triggered through ADT Event Management.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `UPDATE_TIME` | DATETIME (Local) |  | Instant the encounter status was updated |
| 7 | `UPDATED_ENC_STAT_C_NAME` | VARCHAR |  | Patient encounter status after update |
| 8 | `UPDATED_CONF_STAT_C_NAME` | VARCHAR |  | Confirmation status after the update |
| 9 | `UPDATE_EVENT_ID` | NUMERIC |  | The unique ID of the Leave of Absence Event that triggered the update to the encounter's status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

