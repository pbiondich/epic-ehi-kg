# LOA_UPDATES

> This stores Leave of Absence updates that occur after the event started.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOA_UPD_DATE` | DATETIME |  | When there's a change to leave of absence reason, this records the date that it occurred. |
| 4 | `LOA_UPD_TM` | DATETIME (Local) |  | When there's a change to leave of absence reason, this records the time that it occurred. |
| 5 | `LOA_UPD_RSN_C_NAME` | VARCHAR | org | When there's a change to leave of absence reason, this records the reason that it changed to. |
| 6 | `LOA_UPD_EDIT_DTTM` | DATETIME (Local) |  | When there's a change to leave of absence reason, this records the instant that the user made the update. |
| 7 | `LOA_UPD_USER_ID` | VARCHAR |  | When there's a change to leave of absence reason, this records the user that made the update. |
| 8 | `LOA_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

