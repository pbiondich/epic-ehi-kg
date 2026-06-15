# OR_LOG_SURG_NOTES

> Use OR_LOG_SURGN_NOTES table instead of this. The OR_LOG_SURG_NOTES table contains OR management system log surgeon notes in free-text. This table will be discontinued in future.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the surgeon notes refers to. |
| 2 | `LINE` | INTEGER | PK | The line number of the surgeon notes in the surgical log. |
| 3 | `SURGEON_NOTES` | VARCHAR |  | The free text surgeon notes in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

