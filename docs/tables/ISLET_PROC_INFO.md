# ISLET_PROC_INFO

> Islet processing and testing information.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 31  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `PANC_PROC_TEAM_C_NAME` | VARCHAR | org | The relationship between the pancreas procurement team and the process/infusion team. |
| 3 | `ISLET_PROC_CENTER_C_NAME` | VARCHAR | org | Indicates the relationship between islet processing/testing center and transplant center |
| 4 | `PROC_CENTER_OTHER` | VARCHAR |  | The free text islet processing facility. |
| 5 | `COLL_TYPE_OTHER` | VARCHAR |  | Free text collagenase type. |
| 6 | `ISLET_PU_OTHER` | VARCHAR |  | Free text islet purification information. |
| 7 | `DEN_GRAD_METHOD_C_NAME` | VARCHAR | org | The density gradient method for islet purification. |
| 8 | `DEN_GRAD_METHOD_OTH` | VARCHAR |  | The free text density gradient method. |
| 9 | `ISLET_PRETRT_OTHER` | VARCHAR |  | Free text islet pretreatment. |
| 10 | `TIME_OF_EQUV_CNT_C_NAME` | VARCHAR | org | When the islet equivalent count occurred. |
| 11 | `TIME_EQUV_CNT_OTHER` | VARCHAR |  | Free text for when the islet equivalent count occurred. |
| 12 | `INFUSION_START_DTTM` | DATETIME (UTC) |  | The start time of the islet infusion. |
| 13 | `RESULT_GRAM_STAIN_C_NAME` | VARCHAR | org | The gram stain microbiology result. |
| 14 | `RESULT_AEROB_CULT_C_NAME` | VARCHAR |  | The aerobic culture microbiology result. |
| 15 | `RESULT_ANAER_CULT_C_NAME` | VARCHAR |  | The anaerobic culture microbiology result. |
| 16 | `RESULT_FUNG_CULT_C_NAME` | VARCHAR |  | The fungal culture microbiology result. |
| 17 | `RESULT_MYCOPLASMA_C_NAME` | VARCHAR |  | The mycoplasma microbiology result. |
| 18 | `ENDOTOXIN_UNIT_C_NAME` | VARCHAR | org | The unit for the total endotoxin in the final preparation. |
| 19 | `ISLET_VIAB_TEST_C_NAME` | VARCHAR | org | The islet viability test that was applied. |
| 20 | `VIAB_TEST_OTHER` | VARCHAR |  | Free text for the islet viability test used. |
| 21 | `STIMULATION_IDX` | VARCHAR |  | The stimulation index. |
| 22 | `PULM_USED_C_NAME` | VARCHAR |  | Whether pulmozyme was used during islet processing. |
| 23 | `INFUSION_TOTAL_TIME` | VARCHAR |  | The total duration of the islet infusion. |
| 24 | `CULTURE_PRETRT_DUR` | VARCHAR |  | The duration of culture pretreatment. |
| 25 | `ISOLATION_NUM` | VARCHAR |  | The isolation number. |
| 26 | `NUM_OF_ISLET_EQUV` | NUMERIC |  | The total number of islet equivalents (IEQ). |
| 27 | `PACKED_CELL_VOL` | NUMERIC |  | The packed cell volume in mL. |
| 28 | `TOTAL_ENDOTOXIN_U` | NUMERIC |  | The total number of endotoxin units in final preparation. |
| 29 | `VIAB_RESULTS` | NUMERIC |  | The percentage of viability results. |
| 30 | `ISOLATION_DATE` | DATETIME |  | The date of isolation. |
| 31 | `PANC_PROC_TEAM_INFO` | VARCHAR |  | The free text pancreas procurement team. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

