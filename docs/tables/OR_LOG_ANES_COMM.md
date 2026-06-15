# OR_LOG_ANES_COMM

> The OR_LOG_ANES_COMM table contains OR management system log anesthesia comments.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log of the anesthesia comments. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the anesthesia comment for this surgical log. |
| 3 | `ANESTH_COMMENTS` | VARCHAR |  | The free text anesthesia comments for the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

