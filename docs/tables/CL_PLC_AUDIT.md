# CL_PLC_AUDIT

> This table extracts the audit data from a Patient Location (PLC) record.

**Primary key:** `LOCATION_EVNT_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOCATION_EVNT_ID` | NUMERIC | PK FK→ | The unique ID of the location event. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_EDIT_ID` | VARCHAR |  | Item stores the user who made a specific modification to a patient location record. |
| 4 | `USER_EDIT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `INST_OF_CHNG_TM` | DATETIME (Local) |  | Item tracks the instant a change was made to the patient location record. |
| 6 | `ITM_CHANGED` | INTEGER |  | Item that holds which patient location item was modified. |
| 7 | `OLD_VALUE` | VARCHAR |  | Old value of item to be modified. This is raw data, to get external data look at OLD_PLF_VALUE, OLD_STATUS_VALUE, OLD_EVENT_TYPE_VALUE, AND OLD_TIME_VALUE columns. |
| 8 | `NEW_VALUE` | VARCHAR |  | New value of item that was modified. This is raw data, to get external data look at NEW_PLF_VALUE, NEW_STATUS_VALUE, NEW_EVENT_TYPE_VALUE, AND NEW_TIME_VALUE columns. |
| 9 | `CHANGE_SOURCE_C_NAME` | VARCHAR | org | Action that describes how a patient location record was changed. |
| 10 | `OLD_PLF_VALUE_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 11 | `NEW_PLF_VALUE_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 12 | `OLD_STATUS_VALUE` | INTEGER |  | If ITM_CHANGED is 50, then this column stores the old value of the status that was changed. |
| 13 | `NEW_STATUS_VALUE` | INTEGER |  | If ITM_CHANGED is 50, then this column stores the new value of the status that was changed. |
| 14 | `OLD_EVENT_TYPE_VALUE` | INTEGER |  | If ITM_CHANGED is 70, then this column stores the old value of the event type that was changed. |
| 15 | `NEW_EVENT_TYPE_VALUE` | INTEGER |  | If ITM_CHANGED is 70, then this column stores the new value of the event type that was changed. |
| 16 | `OLD_TIME_VALUE` | DATETIME (Local) |  | If ITM_CHANGED is 221, 222, or 223, then this column stores the old value of the time that was changed. |
| 17 | `NEW_TIME_VALUE` | DATETIME (Local) |  | If ITM_CHANGED is 221, 222, or 223, then this column stores the new value of the time that was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LOCATION_EVNT_ID` | [CL_PLC](CL_PLC.md) | sole_pk | high |

