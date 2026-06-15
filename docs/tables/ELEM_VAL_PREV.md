# ELEM_VAL_PREV

> Contains information about previous values and comments for a SmartData element value.

**Primary key:** `HLV_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREV_INSTANT_DTTM` | DATETIME (Local) |  | Instant of edit of previous smartdata element value or comment |
| 4 | `PREV_USERS` | VARCHAR |  | previous user to set value or comment |
| 5 | `PREV_SRC_NOTE_ID` | VARCHAR |  | The unique ID of the note that the previous value is attached to. |
| 6 | `PREV_NOTE_STATUS_C_NAME` | VARCHAR | org | The status of the previous note. |
| 7 | `PREV_UTC_DTTM` | DATETIME (UTC) |  | The previous UTC instants at which this SDE was documented |
| 8 | `PREV_VALUE_INVLD_YN` | VARCHAR |  | Indicate a previous value to be invalid. |
| 9 | `PREV_SET_BY_C_NAME` | VARCHAR |  | How the previous value was set |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

