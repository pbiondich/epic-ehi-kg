# OR_LOG_PNDS_DIA

> The OR_LOG_PNDS_DIA table contains OR management system log PNDS diagnosis information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log that the PNDS diagnoses refer to. |
| 2 | `LINE` | INTEGER | PK | The line number of the PNDS diagnosis in the log. |
| 3 | `PNDS_DIAGNOSIS_ID` | VARCHAR |  | The unique ID of the PNDS diagnosis. |
| 4 | `PNDS_DIAGNOSIS_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |
| 5 | `PNDS_DIA_PRES_YN` | VARCHAR |  | Yes/no flag indicating whether or not this diagnosis was present. |
| 6 | `PNDS_DIA_NOTES` | VARCHAR |  | Free text comments about the diagnosis. |
| 7 | `PNDS_DIA_ADDED_YN` | VARCHAR |  | Yes/no flag indicating whether or not this diagnosis was added by a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

