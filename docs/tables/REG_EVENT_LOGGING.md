# REG_EVENT_LOGGING

> This table holds information related to event logging in Registration.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REG_EVENT_LOG_C_NAME` | VARCHAR | org | Reg Event. This holds the type of Reg event, like Patient Creation, HAR Creation etc. |
| 4 | `REG_EVENT_TIME_DTTM` | DATETIME (Local) |  | Date/time when the Reg Event occurred. |
| 5 | `REG_EVNT_JUMP_FRM_C_NAME` | VARCHAR | org | The user's activity before the Reg Event occurred. |
| 6 | `REG_EVNT_CNCT_DAT` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

