# ABN_FOLLOW_UP

> This table stores the data related to the follow up done on an Advanced Beneficiary Notice (ABN).

**Primary key:** `NOTE_CSN_ID`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 2 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 3 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CONTACT_NUM` | VARCHAR |  | The number of this contact. |
| 6 | `ABN_FLUP_USER_ID` | VARCHAR |  | Stores the user who did the follow up on this ABN |
| 7 | `ABN_FLUP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ABN_FOLLOW_UP_INST_DTTM` | DATETIME (Local) |  | Stores the instant at which the follow up was done. |
| 9 | `ABN_FLUP_STATUS_C_NAME` | VARCHAR | org | Stores the status of the Advance Beneficiary Notice (ABN) follow-up. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

