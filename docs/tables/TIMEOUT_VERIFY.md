# TIMEOUT_VERIFY

> This table stores the verification information for the timeout.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `VERIFY_USER_ID` | VARCHAR |  | Stores the IDs of the staff members who verified the timeout. |
| 7 | `VERIFY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `VERIFY_PERF_IN_DTTM` | DATETIME (UTC) |  | Stores the instant the timeout was performed at. |
| 9 | `VERIFY_RECORD_DTTM` | DATETIME (UTC) |  | Stores the instant the timeout verification took place. |
| 10 | `VERIF_DEVICE_C_NAME` | VARCHAR | org | The device used by the provider to perform the verification. |
| 11 | `VERIF_SECOND_DEV_C_NAME` | VARCHAR |  | The second device, if any, used by the provider to perform the verification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

