# CW_ABST_HD_ADEQUACY

> Hemodialysis adequacy information from abstractions with clinical hemodialysis or other dialysis treatment information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 20  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `HD_KTV_DATE` | DATETIME |  | The hemodialysis patient's treatment Kt/V collection date. |
| 3 | `HD_KTV_METHOD_C_NAME` | VARCHAR |  | The hemodialysis patient's treatment Kt/V calculation method. |
| 4 | `HD_PRE_BUN_VALUE` | INTEGER |  | The hemodialysis patient's pre-dialysis BUN lab value. |
| 5 | `HD_POST_BUN_VALUE` | INTEGER |  | The hemodialysis patient's post-dialysis BUN lab value. |
| 6 | `HD_PRE_WEIGHT_VALUE` | NUMERIC |  | The hemodialysis patient's pre-dialysis weight value. |
| 7 | `HD_PRE_WEIGHT_UNIT_C_NAME` | VARCHAR | org | The hemodialysis patient's pre-dialysis weight unit. |
| 8 | `HD_POST_WEIGHT_VALUE` | NUMERIC |  | The hemodialysis patient's post-dialysis weight value. |
| 9 | `HD_POST_WEIGHT_UNIT_C_NAME` | VARCHAR |  | The hemodialysis patient's post-dialysis weight unit. |
| 10 | `HD_BUN_DELIVERED_MINUTES` | INTEGER |  | The hemodialysis patient's delivered minutes for BUN hemodialysis session. |
| 11 | `HD_HEIGHT_VALUE` | NUMERIC |  | The hemodialysis patient's height value. |
| 12 | `HD_HEIGHT_UNIT_C_NAME` | VARCHAR | org | The hemodialysis patient's height unit. |
| 13 | `HD_CREATININE_LAB_VALUE` | NUMERIC |  | The hemodialysis patient's serum creatinine lab value. |
| 14 | `HD_CREATININE_LAB_DATE` | DATETIME |  | The hemodialysis patient's serum creatinine lab collection date. |
| 15 | `HD_NPCR_LAB_VALUE` | NUMERIC |  | The hemodialysis patient's normalized protein catabolic rate value. |
| 16 | `HD_NPCR_LAB_DATE` | DATETIME |  | The hemodialysis patient's normalized protein catabolic rate collection date. |
| 17 | `HD_TOTAL_SESSIONS` | INTEGER |  | The hemodialysis patient's total number of hemodialysis sessions in a reporting month. |
| 18 | `HD_TARGET_WEIGHT_ASSESSED_YN` | VARCHAR |  | Shows whether hemodialysis patient's post dialysis target weight assessment is done or not. |
| 19 | `HD_TARGET_WEIGHT_ASSESSED_DATE` | DATETIME |  | The hemodialysis patient's post-dialysis target weight assessment date. |
| 20 | `HD_KTV_VALUE` | NUMERIC |  | The hemodialysis patient's treatment Kt/V value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

