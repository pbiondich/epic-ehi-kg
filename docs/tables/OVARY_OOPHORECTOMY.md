# OVARY_OOPHORECTOMY

> Stores single response data for College of American Pathologists (CAP) form 76037-OVARY: Oophorectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 52  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_INT_RGHT_OV_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity - Right Ovary. |
| 4 | `SPEC_RGHT_OV_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Integrity - Right Ovary. |
| 5 | `SPEC_INT_LEFT_OV_C_NAME` | VARCHAR |  | CAP synoptic form item: Specimen Integrity - Left Ovary. |
| 6 | `SPEC_LEFT_OV_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Integrity - Left Ovary. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 10 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 11 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 12 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 13 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 14 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 15 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 16 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 17 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 18 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 19 | `WHO_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: World Health Organization (WHO) Grading System. |
| 20 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 21 | `EXTENT_UTERUS_C_NAME` | VARCHAR | org | CAP synoptic form item: Extent Uterus. |
| 22 | `EXTENT_UTER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent Uterus. |
| 23 | `EXTENT_PERIT_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Peritoneum. |
| 24 | `EXT_RIGHT_OVARY_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Right ovary. |
| 25 | `EXTENT_LEFT_OVARY_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Left Ovary. |
| 26 | `EXT_RIGHT_FALL_TB_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Right Fallopian Tube. |
| 27 | `EXT_LEFT_FALL_TB_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Left Fallopian Tube. |
| 28 | `EXTENT_OMENTUM_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Omentum. |
| 29 | `EXTENT_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Other Extent. |
| 30 | `TUMOR_OVARY_RIGHT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Size Right Ovary. |
| 31 | `TUMOR_OVARY_RI_GR` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Greatest. |
| 32 | `TUMOR_OVARY_RI_GR2` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Greatest 2. |
| 33 | `TUMOR_OVARY_GR_ADD` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Additional Dimension. |
| 34 | `TUMOR_OVARY_GR_SPEC` | VARCHAR |  | CAP synoptic form item: Tumor Size Right Ovary Specify. |
| 35 | `TUMOR_OVARY_LEFT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Size Left Ovary. |
| 36 | `TUMOR_OVARY_LF_GR` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Greatest. |
| 37 | `TUMOR_OVARY_LF_GR2` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Greatest 2. |
| 38 | `TUMOR_OVARY_LF_ADD` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Additional Dimension. |
| 39 | `TUMOR_OVARY_LF_SPEC` | VARCHAR |  | CAP synoptic form item: Tumor Size Left Ovary Specify. |
| 40 | `TWO_TIER_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Two-Tier Grading System. |
| 41 | `TWO_TIER_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Grade in Two-Tier Grading System. |
| 42 | `IMPLANTS_NA_YN` | VARCHAR |  | CAP synoptic form item: Implants Not Applicable / Not Sampled. |
| 43 | `NONINV_IMPLANTS_C_NAME` | VARCHAR | org | CAP synoptic form item: Noninvasive Implants. |
| 44 | `TYPE_NONINV_IMP_C_NAME` | VARCHAR | org | CAP synoptic form item: Type of Noninvasive Implants. |
| 45 | `NONINV_IMP_SIT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Noninvasive Implant Site. |
| 46 | `INV_IMPLANTS_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Implants. |
| 47 | `INV_IMP_SITE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Invasive Implant Site. |
| 48 | `OVARIAN_INV_C_NAME` | VARCHAR | org | CAP synoptic form item: Ovarian Surface Involvement. |
| 49 | `HIS_TYP_SX_CRD_STRM` | VARCHAR |  | CAP synoptic form item: Histologic Type Sex Cord-Stromal Tumor. |
| 50 | `HIS_TYP_MIX_BRDR_SP` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Mixed Epithelial Borderline Tumor. |
| 51 | `HIS_TYP_MIX_CARC_SP` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Mixed Epithelial Carcinoma. |
| 52 | `HIST_TYP_GERM_SPFY` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Malignant Germ Cell Tumor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

