# OR_IMP_EXPLANT

> The OR_IMP_EXPLANT table contains OR management system explant information for implants.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the explant information for the implant. |
| 3 | `EXPLANTED_DATE` | DATETIME |  | The date the implant was explanted. |
| 4 | `EXPLANT_LOG_ID` | VARCHAR |  | The unique ID of the log in which the implant was explanted. |
| 5 | `EXPL_MANF_NOTF_DT` | DATETIME |  | The date the manufacturer was notified that the implant was explanted. |
| 6 | `EXPLANTED_TIME` | DATETIME (Local) |  | The time when implant was explanted. |
| 7 | `EXPLANT_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `NUM_EXPLANTED` | INTEGER |  | The number of items that were explanted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

