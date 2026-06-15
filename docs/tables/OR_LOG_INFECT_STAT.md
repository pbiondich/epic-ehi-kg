# OR_LOG_INFECT_STAT

> The OR_LOG_INFECT_STAT table contains OR management system log patient infection status.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log that the infection status refers to. |
| 2 | `LINE` | INTEGER | PK | The line number of the infection status in the surgical log. |
| 3 | `INFECTION_STAT_C_NAME` | VARCHAR | org | The category value which refers to the status of the infections that arose during the surgery in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

