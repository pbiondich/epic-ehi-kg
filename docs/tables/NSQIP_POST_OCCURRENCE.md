# NSQIP_POST_OCCURRENCE

> The NSQIP_POST_OCCURRENCE table contains postoperative occurrence information for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The type of registry. |
| 3 | `CHILD_RECORD_NAME` | VARCHAR |  | The name for a child record. |
| 4 | `CHILD_RECORD_ABBR` | VARCHAR |  | The abbreviated name for a child record. |
| 5 | `NSQIP_POST_OCCURRENCE_CAT_C_NAME` | VARCHAR |  | The category ID for the type of postoperative occurrence. |
| 6 | `NSQIP_POST_OCCURRENCE_PATOS_YN` | VARCHAR |  | Indicates whether the postoperative occurrence was present at the time of surgery. |
| 7 | `NSQIP_POST_OCCURRENCE_TRANS` | INTEGER |  | The number of units of red blood cells, whole blood, autologous blood, and cell-saver products transfused postoperatively within the 72 hours of surgery start time. |
| 8 | `NSQIP_POST_OCCURRENCE_DATE` | DATETIME |  | The date of postoperative occurrence. |
| 9 | `NSQIP_POST_OCCURRENCE_ICD9` | VARCHAR |  | The ICD-9 code associated with the postoperative occurrence if the post-op category is Other. |
| 10 | `NSQIP_POST_OCCURRENCE_ICD10` | VARCHAR |  | The ICD-10 code associated with the postoperative occurrence if the post-op category is Other. |
| 11 | `NSQIP_CDIFF_TYPE_C_NAME` | VARCHAR |  | The type of C. diff test performed. |
| 12 | `NSQIP_CDIFF_RESULT_C_NAME` | VARCHAR |  | The result of C. diff test. |
| 13 | `NSQIP_CDIFF_TREATMENT_YN` | VARCHAR |  | Indicates whether the patient was given treatment for C. diff. |
| 14 | `NSQIP_CDIFF_DIARRHEA_YN` | VARCHAR |  | Indicates whether the patient with C. diff had diarrhea/loose stools. |
| 15 | `NSQIP_CDIFF_PAT_HAS_DX_YN` | VARCHAR |  | Indicates whether a patient has a C. diff diagnosis. 'Y' indicates that the patient does have a C. diff diagnosis. 'N' or NULL indicates that the patient does not have a C. diff diagnosis. |
| 16 | `NSQIP_CDIFF_POSITIVE_TEST_OTHR` | VARCHAR |  | The user-entered name of other C.diff tests performed that resulted positive for a patient. This column should only be populated if Other [10] is included in the NSQIP_CDIFF_POSITIVE_TEST table for the patient. |
| 17 | `NSQIP_CDIFF_NEGATIVE_TEST_OTHR` | VARCHAR |  | The user-entered name of other C.diff tests performed that resulted negative for a patient. This column should only be populated if Other [10] is included in the NSQIP_CDIFF_NEGATIVE_TEST table for the patient. |
| 18 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc...) category ID for the registry data record. |
| 19 | `NSQIP_CREAT_INCREASE_C_NAME` | VARCHAR |  | The category ID corresponding to the most severe level of creatinine increase postoperatively. |
| 20 | `NSQIP_LOW_URINE_OUTPUT_C_NAME` | VARCHAR |  | The category ID corresponding to the lowest level of urine output postoperatively. |
| 21 | `NSQIP_CDIFF_CONF_YN` | VARCHAR |  | This item stores whether the patient's C. diff Colitis lab has been confirmed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

