# OR_LOG_COMMENTS

> The OR_LOG_COMMENTS table contains OR management system log comments.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log referred to by the log comments |
| 2 | `LINE` | INTEGER | PK | The line number of the case notes in the surgical log. |
| 3 | `CASE_NOTES` | VARCHAR |  | The free text general notes about the surgery in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

