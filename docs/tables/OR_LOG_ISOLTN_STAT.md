# OR_LOG_ISOLTN_STAT

> The OR_LOG_ISOLTN_STAT table contains OR management system log patient isolation status.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log that the isolation status refers to. |
| 2 | `LINE` | INTEGER | PK | The line number of the isolation status in the surgical log. |
| 3 | `ISOLATION_STAT_C_NAME` | VARCHAR | org | The category value that refers to the isolation statuses of the infection in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

