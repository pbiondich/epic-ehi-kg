# CATARACT_PLANNING_GOALS

> This table contains information about the goals for cataract surgery.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | This column stores the unique identifier for the episode record. |
| 2 | `OPH_CAT_PREREF_DT` | DATETIME |  | Preoperative date of refraction information |
| 3 | `OPH_PRE_REF_SPH` | VARCHAR |  | Stores the preoperative refraction for sphere power. |
| 4 | `OPH_PRE_REF_CYL` | VARCHAR |  | Preoperative refraction cylinder |
| 5 | `OPH_PRE_REF_AXIS` | VARCHAR |  | Preoperative refraction axis |
| 6 | `OPH_CAT_PRE_ADD` | VARCHAR |  | Preoperative refraction add power |
| 7 | `OPH_PREREF_VA` | VARCHAR |  | Preoperative visual acuity |
| 8 | `OPH_CAT_POST_DT` | DATETIME |  | Postoperative refraction date |
| 9 | `OPH_CAT_POST_SPHERE` | VARCHAR |  | Postoperative refraction sphere |
| 10 | `OPH_CAT_POST_CYL` | VARCHAR |  | Postoperative refraction cylinder |
| 11 | `OPH_CAT_POST_AXIS` | VARCHAR |  | Postoperative refraction axis |
| 12 | `OPH_CAT_POST_ADD` | VARCHAR |  | Postoperative refraction add |
| 13 | `OPH_CAT_POST_VA` | VARCHAR |  | Postoperative refraction visual acuity |
| 14 | `OPH_CAT_GOAL_DIST_C_NAME` | VARCHAR |  | Goals for cataract surgery distance target |
| 15 | `OPH_CAT_TARREF_NUM` | VARCHAR |  | Target refraction for cataract surgery |
| 16 | `OPH_PUPIL_SIZE` | NUMERIC |  | The dilated pupil size for the patient that is used as reference when planning cataract surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

