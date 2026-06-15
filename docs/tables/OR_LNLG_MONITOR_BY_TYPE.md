# OR_LNLG_MONITOR_BY_TYPE

> The OR_LNLG_MONITOR_BY_TYPE table contains information about the providers or staff who monitored the piece of equipment while it was on.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MONITORED_BY_TYPE_C_NAME` | VARCHAR | org | Staff type of the staff responsible for monitoring the piece of equipment while it was on. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

