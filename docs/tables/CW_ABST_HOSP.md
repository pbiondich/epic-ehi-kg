# CW_ABST_HOSP

> The hospitalization information from the clinical information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HOSP_ID` | VARCHAR |  | The dialysis patient's hospitalization ID. |
| 4 | `HOSP_ADMSN_DATE` | DATETIME |  | The dialysis patient's hospitalization start date. |
| 5 | `HOSP_ADMSN_DATE_NA_YN` | VARCHAR |  | Whether the dialysis patient's hospitalization start date is available. |
| 6 | `HOSP_TYPE_C_NAME` | VARCHAR | org | The dialysis patient's hospitalization type. |
| 7 | `HOSP_TYPE_NA_YN` | VARCHAR |  | Whether the name of the hospital for where a dialysis patient was admitted is available. |
| 8 | `HOSP_NAME` | VARCHAR |  | The name of the hospital where a dialysis patient was admitted. |
| 9 | `HOSP_NAME_NA_YN` | VARCHAR |  | Whether the name of the hospital for where the dialysis patient was admitted is available. |
| 10 | `HOSP_DISCH_DATE` | DATETIME |  | The dialysis patient's hospitalization discharge date. |
| 11 | `HOSP_DISCH_DATE_NA_YN` | VARCHAR |  | Whether the dialysis patient's hospitalization discharge date is available. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

