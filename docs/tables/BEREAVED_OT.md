# BEREAVED_OT

> This table contains information about your bereaved records. These include contact dates and times, name history, and instant of edit and entry. The records included in this table are Bereavement Contact (LHB) records.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the bereavement contact record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique contact serial number (CSN) of the bereavement contact contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `CONTACT_NUM` | INTEGER |  | The serial number of a contact on the bereavement contact record. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `INSTANT_OF_ENT_DTTM` | DATETIME (Local) |  | The instant of entry when a record is edited |
| 8 | `UPDATE_USER_ID` | VARCHAR |  | The user who updated this bereaved record. |
| 9 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `UPDATE_INSTANT_DTTM` | DATETIME (Local) |  | The instant of the update to the bereaved record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

