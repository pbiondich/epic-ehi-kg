# THYMUS_RESECTION

> Stores data for College of American Pathologists (CAP) form 76055-THYMUS: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 33  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 4 | `SPECIMEN_WEIGHT` | NUMERIC |  | CAP synoptic form item: Specimen Weight. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 12 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 13 | `VIABLE_TMR_PERCENT` | NUMERIC |  | CAP synoptic form item: Residual Viable Tumor Percentage. |
| 14 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 15 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 16 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 17 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 18 | `TMR_EXTENSION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Extension. |
| 19 | `MRG_IVLV_TM_SPEC` | VARCHAR |  | CAP synoptic form item: Specify site for Margins Involved by Tumor. |
| 20 | `STAGE_THYMOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Stage Thymoma. |
| 21 | `PATH_STAGE_THYM_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic Staging for Thymomas (Modified Masaoka Stage). |
| 22 | `IMP_DIST_META_C_NAME` | VARCHAR | org | CAP synoptic form item: Implants / Distant Metastasis. |
| 23 | `IMP_DIST_SITE_OTH` | VARCHAR |  | CAP synoptic form item: Implants / Distant Metastasis Present - Specify Other. |
| 24 | `IMMUNO_STAINS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunohistochemical Stains. |
| 25 | `LYMPH_ND_NUM_XMD` | NUMERIC |  | CAP synoptic form item: Specify the number of lymph nodes examined. |
| 26 | `LYM_ND_NUM_IVLV` | NUMERIC |  | CAP synoptic form item: Specify number of lymph nodes involved. |
| 27 | `LYMP_NODE_NON_PN_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes category when not using Regional Lymph Nodes (pN) notation. |
| 28 | `PT_THYMIC_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT) for Thymic Carcinomas. |
| 29 | `REG_LYM_THYM_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN) for Thymic Carcinomas. |
| 30 | `HIST_TYP_THYM_OTHER` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Thymoma. |
| 31 | `HIST_TYP_THYMIC_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Thymic carcinoma. |
| 32 | `TUMOR_EXT_LUNG_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Extension - Specify Lobes of Lung. |
| 33 | `TUMOR_EXT_PLEURA` | VARCHAR |  | CAP synoptic form item: Tumor Extension - Specify Pleura Location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

