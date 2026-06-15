# TPL_DOSING_PARAMS

> The dosing parameters and edit history of the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 39  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to a set of dosing parameters for the treatment plan in this row. |
| 3 | `TPL_DOSING_WEIGHT` | NUMERIC |  | The dosing weight for the treatment plan in this row. |
| 4 | `DOSING_WEIGHT_INST` | DATETIME (Local) |  | The date/time in external format when the dosing weight was recorded for the treatment plan in this row. |
| 5 | `TPL_DW_SOURCE_C_NAME` | VARCHAR | org | The source of the treatment plan weight for the treatment plan in this row. |
| 6 | `TPL_DW_COMMENTS` | VARCHAR |  | The dosing weight comments for the treatment plan in this row. |
| 7 | `TPL_WT_ALERT_LEVEL` | NUMERIC |  | The dosing weight alert threshold percentage for the treatment plan in this row. |
| 8 | `TPL_DOSING_HEIGHT` | NUMERIC |  | The dosing height in centimeters for the treatment plan in this row. |
| 9 | `TPL_DOSING_HT_INST` | DATETIME (Local) |  | The date/time in external format when the dosing height was recorded for the treatment plan in this row. |
| 10 | `TPL_HT_SOURCE_C_NAME` | VARCHAR | org | The dosing height source for the treatment plan in this row. |
| 11 | `TPL_HT_COMMENTS` | VARCHAR |  | The dosing height comments for the treatment plan in this row. |
| 12 | `TPL_DOSING_BSA` | NUMERIC |  | The dosing body surface area (BSA) for the treatment plan in this row. |
| 13 | `TPL_BSA_SRC_C_NAME` | VARCHAR | org | The source of the dosing body surface area for the treatment plan in this row. |
| 14 | `TPL_BSA_CALC_DESC` | VARCHAR |  | The dosing body surface area calculation source and details for the treatment plan in this row. |
| 15 | `TPL_BSA_COMMENTS` | VARCHAR |  | The dosing body surface area comments for the treatment plan in this row. |
| 16 | `TPL_BSA_ALERT_LEVEL` | NUMERIC |  | The dosing body surface area alert threshold percentage for the treatment plan in this row. |
| 17 | `TPL_TARGET_AUC` | NUMERIC |  | The target area under the curve (AUC) for medication orders in the treatment plan in this row. |
| 18 | `TPL_DPARAM_USER_ID` | VARCHAR |  | The user who updated the dosing parameters for the treatment plan in this row. |
| 19 | `TPL_DPARAM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `TPL_DP_UPD_INST` | DATETIME (Local) |  | The date/time in external format when this line of the dosing parameters was updated for the treatment plan in this row. |
| 21 | `TPL_DOC_WEIGHT` | NUMERIC |  | The last documented weight in kilograms for the treatment plan in this row. |
| 22 | `TPL_DOC_WT_INST` | DATETIME (Local) |  | The date/time in external format when the documented weight was recorded for the treatment plan in this row. |
| 23 | `TPL_DOC_HEIGHT` | NUMERIC |  | The last documented height in centimeters for the treatment plan in this row. |
| 24 | `TPL_DOC_HT_INST` | DATETIME (Local) |  | The date/time in external format when the documented height was recorded for the treatment plan in this row. |
| 25 | `TPL_DOC_BSA` | NUMERIC |  | The body surface area (BSA) in meters squared corresponding to the documented weight and height for the treatment plan in this row. |
| 26 | `TPL_DOC_BSA_CALC` | VARCHAR |  | The description of how the body surface area was calculated from the documented weight and height for the treatment plan in this row. |
| 27 | `TPL_IDEAL_WEIGHT` | NUMERIC |  | The ideal weight based on the documented height for the treatment plan in this row. |
| 28 | `TPL_IDEAL_BSA` | NUMERIC |  | The body surface area (m2) based on the ideal weight and recorded height for the treatment plan in this row. |
| 29 | `TPL_IDL_BSA_CALC` | VARCHAR |  | The description of how the body surface area was calculated from the ideal weight and recorded height for the treatment plan in this row. |
| 30 | `TPL_ADJ_WEIGHT` | NUMERIC |  | The adjusted weight based on the ideal weight and recorded height for the treatment plan in this row. |
| 31 | `TPL_ADJ_BSA` | NUMERIC |  | The body surface area (m2) based on adjusted weight and recorded height for the treatment plan in this row. |
| 32 | `TPL_ADJ_BSA_CALC` | VARCHAR |  | The description of how the body surface area was calculated from the adjusted weight and recorded height for the treatment plan in this row. |
| 33 | `ADJ_WT_CORR_FACTOR` | NUMERIC |  | This item contains the correction factor to use for adjusted weight calculations in this treatment plan. |
| 34 | `CRCL_FORMULA_LPP_ID` | NUMERIC |  | The unique ID of the programming point that will be used by medications setup to calculate area under the curve (AUC) doses by using the treatment plan level creatinine clearance formula. |
| 35 | `CRCL_FORMULA_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 36 | `BSA_FORMULA_ID` | NUMERIC |  | Body surface area formula to use when calculating body surface area (BSA) in treatment plan orders. |
| 37 | `BSA_FORMULA_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 38 | `WEIGHT_NOT_SELECTED_YN` | VARCHAR |  | Indicates whether a dosing option has been selected ('N' or NULL) or not selected ('Y') for this treatment plan. |
| 39 | `PAT_REPORTED_WEIGHT_SOURCE_C_NAME` | VARCHAR |  | Indicates the source of a patient-reported dosing weight value, such as reported by a smart device or manually entered by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

