# OR_IMP_COMMENTS

> The OR_IMP_COMMENTS table contains OR management system implant comments.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the comment information for the implant. |
| 3 | `COMMENTS_MULT` | VARCHAR |  | One line of comments stored for the implant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

