# OR_LNLG_LASER_STF_ATTENTV

> This table contains if the staff were attentive while the laser was in use for the laser safety checklist.

**Primary key:** `LASER_SAFETY_CHECKLIST_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LASER_SAFETY_CHECKLIST_ID` | VARCHAR | PK | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LSC_STAFF_ATTENTIVE_C_NAME` | VARCHAR | org | Used to document if the staff were attentive when the laser was in use. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

