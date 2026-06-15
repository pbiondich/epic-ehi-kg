# OR_LOG_PNDS_INT

> The OR_LOG_PNDS_INT table contains OR management system log PNDS intervention information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log that the PNDS interventions refer to. |
| 2 | `LINE` | INTEGER | PK | The line number of the PNDS interventions in the log. |
| 3 | `PNDS_INTERVENT_ID` | VARCHAR |  | The unique ID of the PNDS intervention. |
| 4 | `PNDS_INTERVENT_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |
| 5 | `PNDS_INT_USED_YN` | VARCHAR |  | Yes/no flag indicating whether or not this intervention was used. |
| 6 | `PNDS_INT_NOTES` | VARCHAR |  | Free text comments about the intervention. |
| 7 | `PNDS_INT_ADDED_YN` | VARCHAR |  | Yes/no flag indicating whether or not this intervention was added by a user. |
| 8 | `PNDS_INT_OUT_ID` | VARCHAR |  | The unique ID of the PNDS outcome associated with this intervention. |
| 9 | `PNDS_INT_OUT_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

