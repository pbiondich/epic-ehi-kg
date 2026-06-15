# OR_IMP_FDANOTIF

> The OR_IMP_FDANOTIF table contains OR management system implant FDA notifications.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the FDA notification information for the implant. |
| 3 | `FDA_NOTIFY_DATE` | DATETIME |  | The date the FDA was notified regarding the implant. |
| 4 | `FDA_NOTIF_RSN_C_NAME` | VARCHAR | org | The reason the FDA was notified. |
| 5 | `FDA_NOTIF_COMMENTS` | VARCHAR |  | The comments attached to the FDA notification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

