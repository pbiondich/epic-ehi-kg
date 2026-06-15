# ISLET_INF_PRTL_PRS

> Portal pressure changes during islet infusion.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PORTAL_PRESSURE` | NUMERIC |  | The portal pressure in mm Hg for islet cells infused into the portal vein. |
| 4 | `PORT_PRESS_TIMELINE` | NUMERIC |  | The portal pressure timeline in minutes. |
| 5 | `PROC_STATUS_C_NAME` | VARCHAR | org | Procedure status indicating the stage of islet transplant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

