# OR_LOG_PROC_RQST

> The OR_LOG_PROC_RQST table contains OR management system log procedure requests.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of procedure request in the log. |
| 3 | `PROCEDURE_REQUEST` | VARCHAR |  | The free text procedure request for the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

