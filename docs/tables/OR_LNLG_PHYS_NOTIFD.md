# OR_LNLG_PHYS_NOTIFD

> This table stores the date and time the physician was notified of equipment settings.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIFIED_TM` | DATETIME (Attached) |  | Time(s) physician was notified of equipment settings throughout the case. |
| 4 | `NOTIFIED_DT` | DATETIME |  | Date(s) physician was notified of equipment settings throughout the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

