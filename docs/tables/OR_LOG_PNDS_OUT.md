# OR_LOG_PNDS_OUT

> The OR_LOG_PNDS_OUT table contains OR management system log PNDS outcome information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log that the PNDS outcomes refer to. |
| 2 | `LINE` | INTEGER | PK | The line number of the PNDS outcome in the log. |
| 3 | `PNDS_OUTCOME_ID` | VARCHAR |  | The unique ID of the PNDS outcome. |
| 4 | `PNDS_OUTCOME_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |
| 5 | `PNDS_OUT_ACHVD_YN` | VARCHAR |  | Yes/no flag indicating whether or not this outcome was achieved. |
| 6 | `PNDS_OUT_NOTES` | VARCHAR |  | Free text comments about the outcome. |
| 7 | `PNDS_OUT_ADDED_YN` | VARCHAR |  | Yes/no flag indicating whether or not this outcome was added by a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

