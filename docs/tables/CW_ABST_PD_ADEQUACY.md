# CW_ABST_PD_ADEQUACY

> Peritoneal dialysis adequacy information from abstractions with clinical peritoneal dialysis or other dialysis information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `PD_KTV_VALUE` | NUMERIC |  | The patient's peritoneal dialysis treatment Kt/V value. |
| 3 | `PD_KTV_DATE` | DATETIME |  | The patient's peritoneal dialysis treatment Kt/V collection date. |
| 4 | `PD_KTV_METHOD_C_NAME` | VARCHAR |  | The peritoneal dialysis patient's treatment Kt/V calculation method. |
| 5 | `PD_BSA_METHOD_C_NAME` | VARCHAR |  | The peritoneal dialysis patient's body surface area calculation method. |
| 6 | `PD_RRF_ASSESSED_YN` | VARCHAR |  | Shows whether the peritoneal dialysis patient's residual renal function was assessed in calculating Kt/V or not. |
| 7 | `PD_URINE_VOLUME` | INTEGER |  | The peritoneal dialysis patient's urine volume value used in Kt/V calculation. |
| 8 | `PD_HEIGHT_VALUE` | NUMERIC |  | The peritoneal dialysis patient's height. |
| 9 | `PD_HEIGHT_UNIT_C_NAME` | VARCHAR | org | The peritoneal dialysis patient's height unit. |
| 10 | `PD_WEIGHT_VALUE` | NUMERIC |  | The peritoneal dialysis patient's weight. |
| 11 | `PD_WEIGHT_UNIT_C_NAME` | VARCHAR | org | The peritoneal dialysis patient's weight unit. |
| 12 | `PD_KTV_BSA_IS_CORRECTED_YN` | VARCHAR |  | Shows whether the peritoneal dialysis patient's creatinine clearance lab value uses corrected BSA or not. |
| 13 | `PD_KTV_CREATININE_VALUE` | NUMERIC |  | The peritoneal dialysis patient's serum creatinine lab value. |
| 14 | `PD_KTV_CREATININE_DATE` | DATETIME |  | The peritoneal dialysis patient's serum creatinine lab collection date. |
| 15 | `PD_KTV_NPCR_VALUE` | NUMERIC |  | The peritoneal dialysis patient's Normalized Protein Catabolic Rate (nPCR) value. |
| 16 | `PD_KTV_NPCR_DATE` | DATETIME |  | The peritoneal dialysis patient's Normalized Protein Catabolic Rate (nPCR) collection date. |
| 17 | `PD_KTV_CREATININE_CLEAR_VALUE` | NUMERIC |  | The peritoneal dialysis patient's creatinine clearance value. |
| 18 | `PD_KTV_CREATININE_CLEAR_UNIT_C_NAME` | VARCHAR | org | The peritoneal dialysis patient's creatinine clearance unit of measurement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

