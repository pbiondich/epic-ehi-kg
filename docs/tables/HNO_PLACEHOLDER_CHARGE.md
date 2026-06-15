# HNO_PLACEHOLDER_CHARGE

> Contains items related to Create Placeholder Charge action.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHG_CREATED_YN` | VARCHAR |  | This item stores the flag that indicates whether a placeholder charge was created or not. |
| 4 | `CHG_ACTION_USER_ID` | VARCHAR |  | This item stores the user that submitted the action Create Placeholder Charge. |
| 5 | `CHG_ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHG_ACTION_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when the action Create Placeholder Charge was submitted. |
| 7 | `CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 8 | `CHG_FAIL_REASON_C_NAME` | VARCHAR |  | This item stores the fail reasons for not creating placeholder charges. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

