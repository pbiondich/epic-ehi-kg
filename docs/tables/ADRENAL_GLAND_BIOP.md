# ADRENAL_GLAND_BIOP

> Stores single response data for College of American Pathologists (CAP) form 76000-ADRENAL GLAND: BIOPSY.

**Primary key:** `RESULT_ID`  
**Columns:** 38  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `NON_PATH_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Non-Pathology Findings. |
| 3 | `NEOADJUVANT_THRPY_C_NAME` | VARCHAR | org | CAP synoptic form item: Neoadjuvant Therapy. |
| 4 | `NEOADJ_THRPY_TYPE` | VARCHAR |  | CAP synoptic form item: Neoadjuvant Therapy Type. |
| 5 | `OTHER_CLIN_FNDGS` | VARCHAR |  | CAP synoptic form item: Other Clinical Findings. |
| 6 | `SPEC_RECEIVED_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Received. |
| 7 | `SPEC_RECV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Specimens Received. |
| 8 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 9 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 10 | `SPEC_LATERALITY_SPF` | VARCHAR |  | CAP synoptic form item: Other specimen laterality data. |
| 11 | `TUMOR_GLAND_WT` | NUMERIC |  | CAP synoptic form item: Tumor Gland Weight. |
| 12 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 13 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 14 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 15 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 16 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 17 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 18 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 19 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 20 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 21 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 22 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 23 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 24 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 25 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 26 | `TUMOR_DESC_E_A_SPFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description for extra-adrenal. |
| 27 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 28 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 29 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 30 | `ANC_STDIES_SPFY_RSL` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Results. |
| 31 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 32 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 33 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 34 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 35 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 36 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 37 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 38 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

