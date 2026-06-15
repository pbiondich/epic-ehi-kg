# BEREAVE_FOL_STATUS

> This table contains information about your bereaved follow-up record's status. These include planned and completed dates, record status, user ID, and user comment. The records included in this table are Bereavement Follow-Up (LHC) records.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the bereavement follow-up record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date, in decimal format, where the integer portion represents the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | Contact number |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | Stores the Community ID (CID) of the instance that owns this contact |
| 7 | `FOLLOW_UP_PLANNED_DT` | DATETIME |  | Planned date for bereavement follow-up. |
| 8 | `FOLLOW_UP_COMP_DT` | DATETIME |  | Completion date for bereavement follow-up. |
| 9 | `FOLLOW_UP_COMP_DTTM` | DATETIME (Local) |  | Instant bereavement follow-up filed. |
| 10 | `FOLLOW_UP_USER_ID` | VARCHAR |  | User entering bereavement follow-up. |
| 11 | `FOLLOW_UP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `FOLLOW_UP_STAT_C_NAME` | VARCHAR |  | Status of bereavement follow-up. |
| 13 | `FOLLOW_UP_CONT_CMT` | VARCHAR |  | Comment related to follow-up contact. |
| 14 | `INSTANT_OF_ENT_DTTM` | DATETIME (Local) |  | Stores the instant of entry when a record is edited |
| 15 | `FOLLOW_UP_RISK_C_NAME` | VARCHAR |  | Risk level related to follow-up contact. |
| 16 | `FOL_UP_LET_LST_PRNT_DTTM` | DATETIME (Local) |  | The instant the follow-up letter was last printed. |
| 17 | `FOLLOW_UP_OWNER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

