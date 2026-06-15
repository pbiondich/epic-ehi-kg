# OR_LOG_DIAG_CODES

> The OR_LOG_DIAG_CODES table contains OR management system log diagnosis codes.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log of the surgery that the diagnosis refers to. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the diagnosis in the surgical log. |
| 3 | `DX_CODES_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DIAG_ASSOC_YN` | VARCHAR |  | A yes/no flag indicating whether the diagnosis is associated in the surgical log. |
| 5 | `DIAGNOSIS_PROC_ID` | VARCHAR |  | The unique ID of the diagnosis attached to the procedure in the log. |
| 6 | `DIAGNOSIS_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 7 | `DIAGNOSIS_PANEL` | INTEGER |  | The number of the panel for the procedure. |
| 8 | `PRIMARY_DX_YN` | VARCHAR |  | Yes/No flag indicating whether or not this diagnosis is the primary diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

