# OR_LOG_ANES_CONT

> The OR_LOG_ANES_CONT table contains OR management system log anesthesia contingencies.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log with anesthesia contingencies. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the anesthesia contingencies for this log. |
| 3 | `ANES_PREOP_CONT_C_NAME` | VARCHAR | org | The category value which indicates a pre-operative anesthesia contingency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

