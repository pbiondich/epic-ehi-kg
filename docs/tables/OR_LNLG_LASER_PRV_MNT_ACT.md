# OR_LNLG_LASER_PRV_MNT_ACT

> This table contains if the preventative maintenance is current for the laser safety checklist.

**Primary key:** `LASER_SAFETY_CHECKLIST_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LASER_SAFETY_CHECKLIST_ID` | VARCHAR | PK | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LSC_PREV_MAINTENANCE_ACTIVE_C_NAME` | VARCHAR | org | Stores whether the preventative maintenance is current during the laser safety evaluation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

