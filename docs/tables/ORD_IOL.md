# ORD_IOL

> Calculated IOL data for cataract surgery.

**Primary key:** `FINDING_ID`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `CALC_IOL_MODEL` | VARCHAR |  | The model for a calculated IOL |
| 3 | `CALC_IOL_FORMULA` | VARCHAR |  | The formula used for a calculated IOL |
| 4 | `CALC_IOL_POWER` | VARCHAR |  | The lens power for a calculated IOL |
| 5 | `CALC_IOL_REFRACTION` | VARCHAR |  | The resultant refraction of a particular lens calculation |
| 6 | `CALC_IOL_LAT_C_NAME` | VARCHAR |  | The eye for which a lens was calculated |
| 7 | `CALC_IOL_MANUFACTUR` | VARCHAR |  | The manufacturer for a calculated IOL |
| 8 | `CALC_IOL_TORIC_MOD` | VARCHAR |  | The toric model for a calculated IOL |
| 9 | `CALC_IOL_CORNEA_POW` | VARCHAR |  | The cornea power for a calculated IOL |
| 10 | `CALC_IOL_CYL_POW` | VARCHAR |  | The IOL cylinder power for a calculated IOL |
| 11 | `CALC_IOL_SIA` | VARCHAR |  | The anticipated surgically induced astigmatism for a calculated IOL |
| 12 | `CALC_IOL_AXIS` | VARCHAR |  | The implant axis for a calculated IOL |
| 13 | `CALC_IOL_INCISION` | VARCHAR |  | The incision location for a calculated IOL |
| 14 | `CALC_IOL_AST` | VARCHAR |  | The calculated residual astigmatism for a calculated IOL |
| 15 | `CALC_IOL_AST_AXIS` | VARCHAR |  | The calculated residual astigmatism axis for a calculated IOL |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

