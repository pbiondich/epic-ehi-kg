# OR_LOG_ANESNTXT

> The OR_LOG_ANESNTXT table contains OR management system log anesthesia notes.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the anesthesia notes information for the log. |
| 3 | `ANESTHESIA_NOTES` | VARCHAR |  | The anesthesia notes attached to the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

