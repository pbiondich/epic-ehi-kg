# OR_LOG_NURSE_NOTES

> Use OR_LOG_NURS_NOTES table instead of this. The OR_LOG_NURSE_NOTES table contains OR management system log nursing notes in free-text. This table will be discontinued in future.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the nursing notes refer to. |
| 2 | `LINE` | INTEGER | PK | The line number of the nursing notes in the surgical log. |
| 3 | `NURSING_NOTES` | VARCHAR |  | The free text nursing notes in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

