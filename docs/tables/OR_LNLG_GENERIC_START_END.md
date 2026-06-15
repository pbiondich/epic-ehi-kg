# OR_LNLG_GENERIC_START_END

> The OR_LNLG_GENERIC_START_END table contains generic start date/time and end date/time information for related group line data (ORM) records.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_UTC_DTTM` | DATETIME (UTC) |  | The date and time at which the use of something during a procedure started. |
| 4 | `END_UTC_DTTM` | DATETIME (UTC) |  | The date and time at which the use of something during a procedure ended. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

