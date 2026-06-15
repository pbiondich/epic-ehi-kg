# OR_LNLG_ANES_RTIMS

> Stores the anesthesia staff responsible times.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_STF_START_TIME` | DATETIME (Local) |  | The time at which the anesthesia staff member became responsible for the case with the assigned role. |
| 4 | `ANES_STF_END_TIME` | DATETIME (Local) |  | The time at which the anesthesia staff member ceased being responsible for the case with the assigned role. |
| 5 | `ANES_STF_TOTAL_TIME` | INTEGER |  | The total time, in seconds, that the anesthesia staff member was responsible for the case with the assigned role. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

