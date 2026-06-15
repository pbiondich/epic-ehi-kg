# IMP_STENT_DIMENSIONS

> This table contains data for the dimensions of custom made abdominal aortic aneurysm stents.

**Primary key:** `IMPLANT_ID`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `AORTIC_NECK_LENGTH` | INTEGER |  | The length of the aortic neck for the custom made stent |
| 3 | `AORTIC_NECK_DIAM` | INTEGER |  | The diameter of the aortic neck for the custom made stent |
| 4 | `R_COMMON_ILIAC_DIAM` | INTEGER |  | The diameter of the right common iliac aneurysm for the custom made stent |
| 5 | `L_COMMON_ILIAC_DIAM` | INTEGER |  | The diameter of the left common iliac aneurysm for the custom made stent |
| 6 | `ILIAC_ANEURYSM_LOCATION_C_NAME` | VARCHAR | org | The location of the iliac aneurysm used for the custom made stent |
| 7 | `AORTA_NECK_ANGLE` | INTEGER |  | The angle of the aorta to the neck for the custom made stent |
| 8 | `NECK_AAA_ANGLE` | INTEGER |  | The angle of the neck to the abdominal aorta aneurysm for the custom made stent |
| 9 | `R_INTERNAL_ILIAC_DIAM` | INTEGER |  | The diameter of the right internal iliac aneurysm for the custom made stent |
| 10 | `L_INTERNAL_ILIAC_DIAM` | INTEGER |  | The diameter of the left internal iliac aneurysm for the custom made stent |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

