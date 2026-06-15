# OR_LNLG_XRAY_SHLD_APP

> The OR_LNLG_XRAY_SHLD_APP table contains information about the shielding applied to the patient and staff during X-Rays for the procedure.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `XRAY_SHIELD_APPL_C_NAME` | VARCHAR | org | The category ID for the x-ray shielding applied. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

