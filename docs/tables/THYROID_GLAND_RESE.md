# THYROID_GLAND_RESE

> Stores data for College of American Pathologists (CAP) form 76056-THYROID GLAND: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 60  
**Org-specific columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `RADIATION_EXPOSUR_C_NAME` | VARCHAR | org | CAP synoptic form item: Radiation Exposure. |
| 3 | `RADIATION_EXPO_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Radiation Exposure. |
| 4 | `SPEC_RECEIVED_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Received. |
| 5 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 6 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 7 | `SPECIMEN_WEIGHT` | NUMERIC |  | CAP synoptic form item: Specimen Weight. |
| 8 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 9 | `TUMOR_OTHER_SIZE_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Tumor Size. |
| 10 | `TUMOR_OTHER_GREAT` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Greatest. |
| 11 | `TUMOR_OTHER_ADDT1` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Additional. |
| 12 | `TUMOR_OTHER_ADDT2` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Additional 2. |
| 13 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 14 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 15 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 16 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 17 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 18 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 19 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 20 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 21 | `ANC_STDIES_SPFY_RSL` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Results. |
| 22 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 23 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 24 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 25 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 26 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 27 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 28 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 29 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 30 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 31 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 32 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 33 | `OTHER_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Margin. |
| 34 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 35 | `ADD_PATH_THY_SPCFY` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings - Specify Thyroiditis. |
| 36 | `ADD_PTH_PARATHY_SPY` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings - Specify Parathyroid Glands. |
| 37 | `HIS_TYP_PAP_VAR_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type Papillary Carcinoma Variant - Specify Other. |
| 38 | `HIS_TYPE_ARCH_OTHER` | VARCHAR |  | CAP synoptic form item: Histologic Type Architecture - Specify Other. |
| 39 | `HIS_TYP_FOL_VAR_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type Follicular Carcinoma Variant - Specify Other. |
| 40 | `TUMOR_CAPSULE_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Capsule. |
| 41 | `TMR_CAP_INV_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Capsular Invasion Present. |
| 42 | `EXTRATHYROID_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Extrathyroidal Extension. |
| 43 | `EXTRATYH_EXT_PRES_C_NAME` | VARCHAR |  | CAP synoptic form item: Extrathyroidal Extension Present. |
| 44 | `MARGIN_INV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Margins Invasive Specify Margins Per Orientation. |
| 45 | `TUMOR_OTHER_SPEC1` | VARCHAR |  | CAP synoptic form item: Other Tumor Size Specify. |
| 46 | `HIS_TYP_PAP_V_SPY_2` | VARCHAR |  | CAP synoptic form item: Second Histologic Type - Specify Papillary Variant. |
| 47 | `HIS_TYP_PAP_ARC_O_2` | VARCHAR |  | CAP synoptic form item: Second Histologic Type - Specify Papillary Architecture. |
| 48 | `HIST_GRADE_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Histologic Grade. |
| 49 | `HIST_TYPE_SPECIFY_2` | VARCHAR |  | CAP synoptic form item: Second Specify Histologic Type. |
| 50 | `HIST_GRADE_SPECFY_2` | VARCHAR |  | CAP synoptic form item: Second Specify Histologic Grade. |
| 51 | `TUMOR_CAPSULE_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Tumor Capsule. |
| 52 | `LYMP_VAS_INV_PR_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Second Lymph-Vascular Invasion Present. |
| 53 | `TMR_CP_INV_PRS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Tumor Capsular Invasion Present. |
| 54 | `PERIN_INV_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Perineural Invasion. |
| 55 | `OTH_MRG_DIST_CLSEST` | NUMERIC |  | CAP synoptic form item: Other Margin: Distance from closest margin. |
| 56 | `EXTRA_EXT_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Extrathyroidal Extension. |
| 57 | `EXTRA_EXT_PRES_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Second Extrathyroidal Extension Present. |
| 58 | `HT_FOL_VAR_2_SPCFY` | VARCHAR |  | CAP synoptic form item: Second Histologic Type - Specify Follicular Variant. |
| 59 | `SRC_PATH_METAS_SPEC` | VARCHAR |  | CAP synoptic form item: Source of Pathologic Metastatic Specimen Specify. |
| 60 | `SPEC_RECV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Specimens Received. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

