# DD_DIA_CMS_DISCONTINUED

> This table contains fields that have been discontinued from dialysis regulatory reporting forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 16  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `CURRENT_STATUS_C_NAME` | VARCHAR | org | The current state of the registry record. |
| 3 | `FLU_NOT_RECV_RSN_C_NAME` | VARCHAR | org discont. | It stores a dialysis patient's influenza vaccination not received reason. |
| 4 | `FLU_NOT_RECV_MED_RSN_C_NAME` | VARCHAR | org discont. | It stores the medical reason why a dialysis patient did not receive an influenza vaccination. |
| 5 | `FLU_NOT_RECV_PAT_RSN_C_NAME` | VARCHAR | org discont. | It stores the non-medical reason why a dialysis patient did not receive an influenza vaccination. This is known as the patient reason. |
| 6 | `PCV_NOT_RECV_RSN_C_NAME` | VARCHAR | discont. | It stores a dialysis patient's pneumococcal vaccination not received reason. |
| 7 | `PCV_NOT_RECV_MED_RSN_C_NAME` | VARCHAR | discont. | It stores the medical reason why a dialysis patient did not receive a pneumococcal vaccination. |
| 8 | `PCV_NOT_RECV_PAT_RSN_C_NAME` | VARCHAR | discont. | It stores the non-medical reason why a dialysis patient did not receive a pneumococcal vaccination. This is known as the patient reason. |
| 9 | `HOSP_IDENT` | VARCHAR | discont. | It stores the dialysis patient's hospitalization ID. |
| 10 | `HOSP_ADMIT_DATE` | DATETIME | discont. | It stores the dialysis patient's hospitalization admission date. |
| 11 | `HOSP_NAME` | VARCHAR | discont. | It stores the name of the hospital where the dialysis patient is admitted. |
| 12 | `HOSP_TYPE_C_NAME` | VARCHAR | discont. | It stores the dialysis patient's hospitalization type. |
| 13 | `HOSP_DISCH_DATE` | DATETIME | discont. | It stores the dialysis patient's hospitalization discharge date. |
| 14 | `INFECTION_IDENT` | VARCHAR | discont. | It stores the dialysis patient's infection ID. |
| 15 | `INFECTION_REQ_HOSP_YN` | VARCHAR | discont. | It stores whether or not hospitalization is required for a dialysis patient's infection. |
| 16 | `INFECTION_HOSP_DATE` | DATETIME | discont. | It stores the date of admission that occurred because of dialysis infection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

