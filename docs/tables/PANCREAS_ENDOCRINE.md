# PANCREAS_ENDOCRINE

> Stores single response data for College of American Pathologists (CAP) form 76038-PANCREAS (ENDOCRINE): Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 37  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 6 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 7 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 8 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 9 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 10 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 11 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 12 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 13 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 14 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 15 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 16 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 17 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 18 | `SPEC_ADJ_VES_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Adjacent large vessels. |
| 19 | `WHO_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: World Health Organization (WHO) Grading System. |
| 20 | `TUMOR_NEC_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Necrosis. |
| 21 | `MITOTIC_ACT_C_NAME` | VARCHAR | org | CAP synoptic form item: Mitotic Activity. |
| 22 | `KI67_INDEX_C_NAME` | VARCHAR | org | CAP synoptic form item: Ki67 Labeling Index. |
| 23 | `MITOTIC_RATE` | NUMERIC |  | CAP synoptic form item: Mitotic Rate. |
| 24 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 25 | `HIS_TYP_POOR_DIFF_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Poorly differentiated endocrine carcinoma. |
| 26 | `TMR_FOC_NUM_FOCI` | NUMERIC |  | CAP synoptic form item: Tumor Focality Number of Foci. |
| 27 | `DIST_INV_TMR_MRG` | NUMERIC |  | CAP synoptic form item: Distance of Invasive Tumor from Closest Margin. |
| 28 | `INV_IMP_SITE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Invasive Implant Site. |
| 29 | `FUNC_TYPE_C_NAME` | VARCHAR | org | CAP synoptic form item: Functional Type. |
| 30 | `FUN_PAN_FUNC_C_NAME` | VARCHAR | org | CAP synoptic form item: Functional Type Pancreatic endocrine tumor, functional. |
| 31 | `FNC_PAN_FNC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Functional Type Pancreatic endocrine tumor, functional. |
| 32 | `MRG_IVLV_TM_SPEC` | VARCHAR |  | CAP synoptic form item: Specify site for Margins Involved by Tumor. |
| 33 | `MAR_TMR_INV_PAN_YN` | VARCHAR |  | CAP synoptic form item: Tumor Involves posterior retroperitoneal surface of pancreas. |
| 34 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 35 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 36 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 37 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

