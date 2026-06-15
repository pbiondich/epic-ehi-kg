# OR_LOG_ADDENDA

> The OR_LOG_ADDENDA table contains OR management system log addenda.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the addendum is attached to. |
| 2 | `LINE` | INTEGER | PK | The line number of addendum in the surgical log. |
| 3 | `ADDENDA_ID` | VARCHAR |  | The unique ID of the addendum. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

