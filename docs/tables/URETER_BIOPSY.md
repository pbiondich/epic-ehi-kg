# URETER_BIOPSY

> Stores data for College of American Pathologists (CAP) form 76058-URETER, RENAL PELVIS: Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 18  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 4 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 5 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 6 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 7 | `OTHER_TM_CONFIG_S` | VARCHAR |  | CAP synoptic form item: Specify other tumor configuration. |
| 8 | `ADQCY_DETER_T_CAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Adequacy of Material for Determining T Category. |
| 9 | `HG_URTL_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Urothelial Carcinoma. |
| 10 | `HG_URTL_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify the details of Histologic Grade Urothelial carcinoma. |
| 11 | `HG_ADEN_SQUA_CC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 12 | `ADEN_SQUA_CCS` | VARCHAR |  | CAP synoptic form item: Specify Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 13 | `UROT_CCM_W_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Urothelial carcinoma with variant histology. |
| 14 | `SQM_C_CCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Squamous cell carcinoma, variant histology. |
| 15 | `ADNCCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Adenocarcinoma, variant histology. |
| 16 | `UNDIFF_CCNM` | VARCHAR |  | CAP synoptic form item: Specify the details of undifferentiated carcinoma. |
| 17 | `HIST_TP_MIX_CT` | VARCHAR |  | CAP synoptic form item: Specify the details of mixed cell type. |
| 18 | `HIST_GRADE_CBD_YN` | VARCHAR |  | CAP synoptic form item: Histologic Grade Cannot Be Determined. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

