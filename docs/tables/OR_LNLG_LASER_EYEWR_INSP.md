# OR_LNLG_LASER_EYEWR_INSP

> This table contains if the laser eyeware was inspected and cleaned for the laser safety checklist.

**Primary key:** `LASER_SAFETY_CHECKLIST_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LASER_SAFETY_CHECKLIST_ID` | VARCHAR | PK | The unique identifier for the line record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LSC_EYEWARE_INSPECTED_C_NAME` | VARCHAR | org | Used to document that the laser eyeware have been inspected and cleaned. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

