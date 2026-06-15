# CATARACT_PLANNING_LENSES

> This table contains information about the lens selected to have ready for cataract surgery.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | This column stores the unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OPH_CAT_LENS_TYPE_C_NAME` | VARCHAR | org | Stores the type of lens planned for use in cataract surgery |
| 4 | `OPH_CAT_LENS_MODEL` | VARCHAR |  | Stores the selected model of intraocular lens. |
| 5 | `OPH_CAT_LENS_POWER` | VARCHAR |  | Stores the selected lens power for the intraocular lens |
| 6 | `OPH_CAT_LENS_AXIS` | VARCHAR |  | Stores the axis for a intraocular lens |
| 7 | `OPH_CAT_LENS_SUP_ID` | VARCHAR |  | Stores the selected supply record for the intraocular lens |
| 8 | `OPH_CAT_LENS_SUP_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 9 | `OPH_CAT_LENS_CMTS` | VARCHAR |  | Stores comments related to the intraocular lens selection |
| 10 | `OPH_CAT_SPECORD_YN` | VARCHAR |  | Note on whether the lens is a special order lens |
| 11 | `OPH_LENSSEL_TARGET` | NUMERIC |  | Target refraction number for the selected lens |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

