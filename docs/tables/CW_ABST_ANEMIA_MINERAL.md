# CW_ABST_ANEMIA_MINERAL

> Anemia management and mineral metabolism information from abstractions with clinical information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 46  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `HEMOGLOBIN_LAB_VALUE` | NUMERIC |  | The dialysis patient's hemoglobin lab value. |
| 3 | `HEMOGLOBIN_LAB_DATE` | DATETIME |  | The hemoglobin lab collection date of a dialysis patient. |
| 4 | `TSAT_LAB_VALUE` | INTEGER |  | The iron saturation percentage value of a dialysis patient. |
| 5 | `TSAT_LAB_DATE` | DATETIME |  | The iron saturation lab collection date of a dialysis patient. |
| 6 | `RETICULOCYTE_HGB_LAB_VALUE` | INTEGER |  | The reticulocyte hemoglobin lab value of a dialysis patient. |
| 7 | `RETICULOCYTE_HGB_LAB_DATE` | DATETIME |  | The reticulocyte hemoglobin lab collection date of a dialysis patient. |
| 8 | `FERRITIN_LAB_VALUE` | INTEGER |  | The serum ferritin lab value of a dialysis patient. |
| 9 | `FERRITIN_LAB_DATE` | DATETIME |  | The serum ferritin lab collection date of a dialysis patient. |
| 10 | `ESA_IS_ADMIN_YN` | VARCHAR |  | Shows whether dialysis Erythropoiesis Stimulating Agent is administered or not. |
| 11 | `ESA_ADMIN_DATE` | DATETIME |  | The dialysis patient's Erythropoiesis Stimulating Agent administration date. |
| 12 | `ESA_MONTHLY_DOSE` | NUMERIC |  | The dialysis patient's Erythropoiesis Stimulating Agent monthly dose value. |
| 13 | `ESA_DOSE_UNIT_C_NAME` | VARCHAR | org | The dialysis patient's Erythropoiesis Stimulating Agent monthly dose unit. |
| 14 | `ESA_AGENT_C_NAME` | VARCHAR | org | The Erythropoiesis Stimulating Agent information that is prescribed to dialysis patient. |
| 15 | `ESA_ROUTE_C_NAME` | VARCHAR | org | The dialysis patient's Erythropoiesis Stimulating Agent route information. |
| 16 | `ESA_OTHER_AGENT` | VARCHAR |  | The name of the dialysis patient's Erythropoiesis Stimulating Agent if it is not in the list of common agents. |
| 17 | `ESA_OTHER_DOSE` | VARCHAR |  | The dialysis patient's Erythropoiesis Stimulating Agent monthly dose unit if it is not in the list of common units. |
| 18 | `IV_IRON_IS_ADMIN_YN` | VARCHAR |  | Shows whether dialysis IV iron is administered or not. |
| 19 | `IV_IRON_ADMIN_DATE` | DATETIME |  | The dialysis patient's IV iron administration date. |
| 20 | `IV_IRON_AGENT_C_NAME` | VARCHAR | org | The IV iron name that is administered to a dialysis patient |
| 21 | `IV_IRON_OTHER_AGENT` | VARCHAR |  | The name of the dialysis patient's administered IV iron if it is not in the list of common agents. |
| 22 | `IV_IRON_MONTHLY_DOSE` | NUMERIC |  | The dialysis patient's IV iron dose. |
| 23 | `IV_IRON_UNIT_C_NAME` | VARCHAR | org | The dialysis patient's IV iron dose unit. |
| 24 | `IV_IRON_OTHER_UNIT` | VARCHAR |  | The dialysis patient's IV iron dose unit if it is not in the list of common units. |
| 25 | `ORAL_IRON_IS_PRESC_YN` | VARCHAR |  | Shows whether dialysis oral iron is prescribed or not. |
| 26 | `ORAL_IRON_PRESC_DATE` | DATETIME |  | The dialysis patient's oral iron prescription date. |
| 27 | `ORAL_IRON_AGENT_C_NAME` | VARCHAR | org | The dialysis patient's oral iron agent. |
| 28 | `ORAL_IRON_OTHER_AGENT` | VARCHAR |  | The dialysis patient's oral iron agent if it is not in the common agents list. |
| 29 | `ORAL_IRON_MONTHLY_DOSE` | NUMERIC |  | The dialysis patient's oral iron dose value. |
| 30 | `ORAL_IRON_UNIT_C_NAME` | VARCHAR |  | The dialysis patient's oral iron dose unit. |
| 31 | `ORAL_IRON_OTHER_UNIT` | VARCHAR |  | The dialysis patient's oral iron dose unit if it is not in the list of common units. |
| 32 | `CORRECTED_CALCIUM_LAB_VALUE` | NUMERIC |  | The dialysis patient's corrected serum calcium lab value. |
| 33 | `CORRECTED_CALCIUM_LAB_DATE` | DATETIME |  | The dialysis patient's corrected serum calcium lab collection date. |
| 34 | `ALBUMIN_LAB_VALUE` | NUMERIC |  | The dialysis patient's serum albumin lab value. |
| 35 | `ALBUMIN_LAB_DATE` | DATETIME |  | The dialysis patient's serum albumin lab collection date. |
| 36 | `ALBUMIN_LAB_METHOD_C_NAME` | VARCHAR | org | The method used to perform the dialysis patient's serum albumin lab test. |
| 37 | `ALBUMIN_LAB_LOWER_LIMIT` | NUMERIC |  | The lower limit of the dialysis patient's serum albumin lab test. |
| 38 | `PHOSPHORUS_LAB_VALUE` | NUMERIC |  | The dialysis patient's serum phosphorus lab value. |
| 39 | `PHOSPHORUS_LAB_DATE` | DATETIME |  | The dialysis patient's serum phosphorus lab collection date. |
| 40 | `PHOSPHORUS_LAB_METHOD_C_NAME` | VARCHAR | org | The dialysis patient's serum phosphorus lab method. |
| 41 | `UNCORRECTED_CALCIUM_LAB_VALUE` | NUMERIC |  | The dialysis patient's uncorrected serum calcium lab value. |
| 42 | `UNCORRECTED_CALCIUM_LAB_DATE` | DATETIME |  | The dialysis patient's uncorrected serum calcium lab collection date. |
| 43 | `PTH_LAB_VALUE` | NUMERIC |  | The dialysis patient's parathyroid hormone lab value. |
| 44 | `PTH_LAB_DATE` | DATETIME |  | The dialysis patient's parathyroid hormone lab collection date. |
| 45 | `PTH_LAB_METHOD_C_NAME` | VARCHAR | org | The dialysis patient's parathyroid hormone lab method. |
| 46 | `PTH_LAB_UPPER_LIMIT` | NUMERIC |  | The upper limit of the dialysis patient's parathyroid hormone lab test. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

