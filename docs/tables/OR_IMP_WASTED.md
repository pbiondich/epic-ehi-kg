# OR_IMP_WASTED

> The OR_IMP_WASTED table contains OR management system implant waste information.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the waste information for the implant. |
| 3 | `WASTED_DATE` | DATETIME |  | The date that the implant was wasted. |
| 4 | `WASTE_LOG_ID` | VARCHAR |  | The unique ID of the log in which the implant was wasted. |
| 5 | `WASTE_NOTIFY_DATE` | DATETIME |  | The date the manufacturer was notified that the implant was wasted. |
| 6 | `REASON_WASTED_C_NAME` | VARCHAR | org | The category value of the reason the implant was wasted. |
| 7 | `WASTED_TIME` | DATETIME (Local) |  | The exact time an implant was marked as wasted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

