# OR_LOG_SPECNEED

> The OR_LOG_SPECNEED table contains OR management system log special needs.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the special needs entered for the log. |
| 3 | `SPECIAL_NEEDS` | VARCHAR |  | The special needs entered for the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

