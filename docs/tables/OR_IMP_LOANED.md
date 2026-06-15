# OR_IMP_LOANED

> The OR_IMP_LOANED table contains OR management system implant loan information.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the loan information for the implant. |
| 3 | `LOANED_DATE` | DATETIME |  | The date that the implant was loaned. |
| 4 | `LOANED_TO` | VARCHAR |  | Who the implant was loaned to. |
| 5 | `LOAN_NOTIF_DATE` | DATETIME |  | The date the manufacturer was notified of the loan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

