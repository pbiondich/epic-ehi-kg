# SQUAMOUS_CELL_CARC

> Stores data for College of American Pathologists (CAP) form 76051-SQUAMOUS CELL CARCINOMA OF THE SKIN: Biopsy, Excision, Re-excision.

**Primary key:** `RESULT_ID`  
**Columns:** 39  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 6 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 7 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 8 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 9 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 10 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 11 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 12 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 13 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 14 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 15 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 16 | `SPEC_PROC_BIOP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Biopsy. |
| 17 | `SPEC_PROC_EXC_OTHER` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Excision Other. |
| 18 | `SPEC_PROC_RE_EX_OTH` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Re-excision, Other. |
| 19 | `NUM_INV_META_CARC` | NUMERIC |  | CAP synoptic form item: Number of Nodes Involved by Metastatic Carcinoma. |
| 20 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 21 | `NUM_SENT_LYM_EXAM` | NUMERIC |  | CAP synoptic form item: Number of Sentinel Lymph Nodes Examined. |
| 22 | `PROC_LYMPHADENECTM` | VARCHAR |  | CAP synoptic form item: Specimen Procedure - Specify Lymphadenectomy, regional nodes. |
| 23 | `MAX_TUMOR_THICK_C_NAME` | VARCHAR | org | CAP synoptic form item: Maximum Tumor Thickness. |
| 24 | `MAX_TMR_THICK_SPFY` | NUMERIC |  | CAP synoptic form item: Specify Maximum Tumor Thickness. |
| 25 | `MAX_TMR_THICK_LEAST` | NUMERIC |  | CAP synoptic form item: Maximum Tumor Thickness - At Least this Length. |
| 26 | `MAX_TMR_THICK_EXPLN` | VARCHAR |  | CAP synoptic form item: Explain the Maximum Tumor Thickness. |
| 27 | `ANATOMIC_LEVEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Anatomic Level. |
| 28 | `PER_MRG_CNT_ASSE_YN` | VARCHAR |  | CAP synoptic form item: Peripheral Margins Cannot Be Assessed. |
| 29 | `SZE_METASTATIC_FOCS` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Focus (for sentinel node). |
| 30 | `PER_MARG_INV_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Peripheral Margin Invasive Carcinoma. |
| 31 | `PER_MAR_DIST_INV_LA` | NUMERIC |  | CAP synoptic form item: Peripheral Margin Distance of Invasive Carcinoma from Closest Lateral Margin. |
| 32 | `PER_MARG_INV_LOC` | VARCHAR |  | CAP synoptic form item: Specify Peripheral Margin Invasive Carcinoma Location. |
| 33 | `PER_MAR_CARC_SITU_C_NAME` | VARCHAR |  | CAP synoptic form item: Peripheral Margin Carcinoma in Situ. |
| 34 | `PER_MAR_DIS_SITU_LA` | NUMERIC |  | CAP synoptic form item: Peripheral Margin Distance of Carcinoma in Situ from Closest Lateral Margin. |
| 35 | `PER_MAR_SITU_SPECIF` | VARCHAR |  | CAP synoptic form item: Specify Peripheral Margin Carcinoma In Situ Location. |
| 36 | `DSTNC_INV_CCNM_DMNA` | NUMERIC |  | CAP synoptic form item: Specify Distance of Invasive Carcinoma from Margin for Deep Margin when Margins cannot be assessed and Not involved by invasive carcinoma. |
| 37 | `DM_NA_UIC_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Deep Margin when Uninvolved. |
| 38 | `DM_NA_IIC_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Deep Margin when Involved. |
| 39 | `TUMOR_SIZE_INDETER` | VARCHAR |  | CAP synoptic form item: Specify Reason Why Tumor Size Is Indeterminate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

