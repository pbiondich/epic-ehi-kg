# TRG_REL_START_INFO

> Contains items related to having orders with relative start times in a treatment day.

**Primary key:** `REGIMEN_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The treatment day ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `REL_START_TIME` | DATETIME (Local) |  | The reference date and time for the treatment day. All of the orders in the day with relative start times are relative to this time. |
| 4 | `REL_ST_CHG_USER_ID` | VARCHAR |  | This unique ID of the user who changed the reference time of the treatment day. |
| 5 | `REL_ST_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `REL_ST_CHG_DTTM` | DATETIME (Local) |  | This is the date and time that the reference time of the treatment day was changed |
| 7 | `REL_ST_CHG_RSN_C_NAME` | VARCHAR | org | The reason category ID for the reason that the reference time of the treatment day was changed. Link to ZC_OVRD_REASON__OVRD_REASON_C to get the value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

