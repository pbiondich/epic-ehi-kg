# CATARACT_PLANNING_INFO

> This table contains cataract surgery information about the status of the surgery.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | This column stores the unique identifier for the episode record. |
| 2 | `OPH_SURG_STATUS_C_NAME` | VARCHAR |  | Stores the status of the surgery |
| 3 | `OPH_SURG_LINK_ID` | VARCHAR |  | Link to the case for the ophthalmology surgery |
| 4 | `OPH_SURG_HX_DATE` | DATETIME |  | Stores the date of the surgery if done historically and not linked to a case. |
| 5 | `OPH_SURG_HX_SURGEON` | VARCHAR |  | Stores the surgeon name for a historical surgery not linked to a case. |
| 6 | `OPH_SURG_HX_LOC` | VARCHAR |  | Stores the description of the location where a surgery was performed if done historically and not linked to a case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

