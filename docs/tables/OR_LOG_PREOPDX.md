# OR_LOG_PREOPDX

> The OR_LOG_PREOPDX table contains OR management system log preop diagnoses.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the pre-op diagnosis information for the log. |
| 3 | `PRE_OP_DIAG` | VARCHAR |  | The pre-op diagnosis of the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

