# URIN_BLADDER_BIOPS

> Stores single response data for College of American Pathologists (CAP) form 76060: URINARY BLADDER: Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 16  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `UROT_CCM_W_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Urothelial carcinoma with variant histology. |
| 5 | `SQM_C_CCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Squamous cell carcinoma, variant histology. |
| 6 | `ADNCCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Adenocarcinoma, variant histology. |
| 7 | `UNDIFF_CCNM` | VARCHAR |  | CAP synoptic form item: Specify the details of undifferentiated carcinoma. |
| 8 | `HIST_TP_MIX_CT` | VARCHAR |  | CAP synoptic form item: Specify the details of mixed cell type. |
| 9 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 10 | `HG_URTL_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Urothelial Carcinoma. |
| 11 | `HG_URTL_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify the details of Histologic Grade Urothelial carcinoma. |
| 12 | `HG_ADEN_SQUA_CC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 13 | `ADEN_SQUA_CCS` | VARCHAR |  | CAP synoptic form item: Specify Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 14 | `OTHER_TM_CONFIG_S` | VARCHAR |  | CAP synoptic form item: Specify other tumor configuration. |
| 15 | `AM_MUS_PROP_INV_C_NAME` | VARCHAR | org | CAP synoptic form item: Determine Adequacy of Material for Muscularis Propria Invasion. |
| 16 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

