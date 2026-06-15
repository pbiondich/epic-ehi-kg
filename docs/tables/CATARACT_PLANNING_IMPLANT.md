# CATARACT_PLANNING_IMPLANT

> This table contains information about the lens that was implanted as part of cataract surgery.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | This column stores the unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OPH_CAT_LENS_TYPE_C_NAME` | VARCHAR | org | Implanted lens type for cataract surgery |
| 4 | `OPH_LENS_IMP_MODEL` | VARCHAR |  | Implanted lens model |
| 5 | `OPH_LENS_IMP_POWER` | VARCHAR |  | Implanted lens power |
| 6 | `OPH_LENS_IMP_AXIS` | VARCHAR |  | Implanted lens axis |
| 7 | `OPH_LENS_IMP_CMT` | VARCHAR |  | Comments for the implanted intraocular lens |
| 8 | `OPH_LENS_IMP_SUP_ID` | VARCHAR |  | Stores the supply record entered into the implanted lens portion of cataract planning. |
| 9 | `OPH_LENS_IMP_SUP_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

