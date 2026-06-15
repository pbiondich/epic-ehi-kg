# NSQIP_READMISSION

> The NSQIP_READMISSION table contains readmission information for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 24  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The type of registry. |
| 3 | `CHILD_RECORD_NAME` | VARCHAR |  | The name for a child record. |
| 4 | `CHILD_RECORD_ABBR` | VARCHAR |  | The abbreviated name for a child record. |
| 5 | `NSQIP_READM_WITHIN_30_YN` | VARCHAR |  | Indicates whether there was a readmission within 30 days of principal operative procedure. |
| 6 | `NSQIP_READM_DT` | DATETIME |  | The readmission date. |
| 7 | `NSQIP_READM_DT_UNKWN_YN` | VARCHAR |  | Indicates whether the date of readmission is unknown. |
| 8 | `NSQIP_READM_INFO_SRC_C_NAME` | VARCHAR |  | The category ID for the source of information for readmission. |
| 9 | `NSQIP_READM_UNPLANNED_YN` | VARCHAR |  | Indicates whether the readmission was unplanned. |
| 10 | `NSQIP_READM_RELATED_YN` | VARCHAR |  | Indicates whether the readmission is related to the principal operative procedure. |
| 11 | `NSQIP_READM_REL_RSN_C_NAME` | VARCHAR |  | The category ID for the primary reason for readmission related to the principal operative procedure. |
| 12 | `NSQIP_READM_REL_RSN_ICD9` | VARCHAR |  | The ICD-9 code associated with readmission reason if the readmission is related to the principal operative procedure. |
| 13 | `NSQIP_READM_REL_RSN_TXT` | VARCHAR |  | The ICD-9 free text comment associated with readmission reason if the readmission is related to the principal operative procedure. |
| 14 | `NSQIP_READM_UNREL_RSN_C_NAME` | VARCHAR |  | The category ID for the primary reason for readmission unrelated to the principal operative procedure. |
| 15 | `NSQIP_READM_UNREL_RSN_ICD9` | VARCHAR |  | The ICD-9 code associated with readmission reason if the readmission is unrelated to the principal operative procedure. |
| 16 | `NSQIP_READM_UNREL_RSN_TXT` | VARCHAR |  | The ICD-9 free text comment associated with readmission reason if the readmission is unrelated to the principal operative procedure. |
| 17 | `NSQIP_READM_REL_RSN_ICD10` | VARCHAR |  | The ICD-10 code associated with readmission reason if the readmission is related to the principal operative procedure. |
| 18 | `NSQIP_READM_REL_RSN_ICD10_TXT` | VARCHAR |  | The ICD-10 free text comment associated with readmission reason if the readmission is related to the principal operative procedure. |
| 19 | `NSQIP_READM_UNREL_RSN_ICD10` | VARCHAR |  | The ICD-10 code associated with readmission reason if the readmission is unrelated to the principal operative procedure. |
| 20 | `NSQIP_READM_UNREL_RSN_ICD10TXT` | VARCHAR |  | The ICD-10 free text comment associated with readmission reason if the readmission is unrelated to the principal operative procedure. |
| 21 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc...) category ID for the registry data record. |
| 22 | `NSQIP_READM_DISCHARGE_DATE` | DATETIME |  | This item stores the patient's readmission discharge date. |
| 23 | `NSQIP_READM_DISCH_DT_UKNWN_YN` | VARCHAR |  | This item stores a value if the patient's readmission discharge date is unknown. |
| 24 | `NSQIP_READM_STILL_HOSP_30_YN` | VARCHAR |  | This item stores whether the readmitted patient is still in the hospital after 30 days. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

