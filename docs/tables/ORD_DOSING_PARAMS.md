# ORD_DOSING_PARAMS

> This table contains dosing parameters.

**Overflow family:** [ORD_DOSING_PARAMS_2](ORD_DOSING_PARAMS_2.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 14  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `ORD_DOSING_WEIGHT` | NUMERIC |  | Weight used for dosing. Always stored in kilograms. |
| 3 | `ORD_DW_REC_DTTM` | DATETIME (Local) |  | The instant at which the weight was recorded. |
| 4 | `ORD_WT_SOURCE_C_NAME` | VARCHAR | org | This column contains the source of the patient weight used for dosing patient-controlled analgesia (PCA) medication. |
| 5 | `ORD_WT_COMMENTS` | VARCHAR |  | Generated comment for dosing weight. |
| 6 | `ORD_DOSING_HEIGHT` | NUMERIC |  | This column contains the patient height used for dosing PCA medication. The value stored is in inches for all orders after weight-based dosing was turned on, or starting in Spring 2008, whichever came first. Values are stored in centimeters for treatment plan orders made prior to that. |
| 7 | `ORD_HT_REC_DTTM` | DATETIME (Local) |  | The instant at which the height was recorded. |
| 8 | `ORD_HT_SOURCE_C_NAME` | VARCHAR | org | This column contains the source of the patient height used for dosing patient-controlled analgesia (PCA) medication. |
| 9 | `ORD_HT_COMMENTS` | VARCHAR |  | Generated comment for dosing height. |
| 10 | `ORD_DOSING_BSA` | NUMERIC |  | The body surface area used for dosing. |
| 11 | `ORD_BSA_SRC_C_NAME` | VARCHAR | org | This column contains the source of the body surface area used for dosing patient-controlled analgesia (PCA) medication. |
| 12 | `ORD_BSA_CALC_DTL` | VARCHAR |  | The dosing body surface area calculation details with weight, height and recorded instants. |
| 13 | `ORD_BSA_COMMENTS` | VARCHAR |  | Generated comment for dosing body surface area. |
| 14 | `PAT_REPORTED_WEIGHT_SOURCE_C_NAME` | VARCHAR |  | Indicates the source of a patient-reported dosing weight value, such as reported by a smart device or manually entered by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

