# DCIS_BREAST_EXCIS

> Stores data for College of American Pathologists (CAP) form 76013-DCIS OF THE BREAST: Complete Excision (Less Than Total Mastectomy, Including Specimens Designated Biopsy, Lumpectomy, Quadrantectomy, and Partial Mastectomy; With or Without Axillary Contents) and Mastectomy (Total, Modified Radical, Radical; With or Without Axillary Contents).

**Primary key:** `RESULT_ID`  
**Columns:** 69  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CLOCK_POSITION_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Clock Position of Tumor Site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 6 | `SPEC_INTEGRITY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify specimen integrity. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 9 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 10 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 11 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 12 | `MARGIN_DCIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin DCIS. |
| 13 | `RADIOLOG_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Radiologic Findings. |
| 14 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 15 | `HST_BRST_CANCR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Prior History of Breast Cancer. |
| 16 | `LYMPH_ND_SAMPL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify lymph node sampling. |
| 17 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 18 | `SIZE_DCIS_GREAT_DIM` | NUMERIC |  | CAP synoptic form item: Estimated Size of DCIS Greatest Dimension. |
| 19 | `DCIS_ADDL_DIMENSION` | NUMERIC |  | CAP synoptic form item: DCIS Additional Dimension Length. |
| 20 | `DCIS_ADDL_DIM_2` | NUMERIC |  | CAP synoptic form item: DCIS Additional Dimension Width. |
| 21 | `NUM_BLOCK_EXAM_DCIS` | NUMERIC |  | CAP synoptic form item: Number of Blocks Examined for DCIS. |
| 22 | `NUM_BLOCKS_DCIS` | NUMERIC |  | CAP synoptic form item: Number of Blocks With DCIS. |
| 23 | `ARCHITECT_PAT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Architectural Patterns. |
| 24 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 25 | `NUCLEAR_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Nuclear Grade. |
| 26 | `DCIS_CLOSEST_MARGIN` | NUMERIC |  | CAP synoptic form item: DCIS Distance from Closest Margin. |
| 27 | `DCIS_SUPERIOR_MRG` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Superior Margin. |
| 28 | `DCIS_INFERIOR_MRG` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Inferior Margin. |
| 29 | `DCIS_ANTERIOR_MRG` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Anterior Margin. |
| 30 | `DCIS_POSTERIOR_MRG` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Posterior margin. |
| 31 | `DCIS_MEDIAL_MARGIN` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Medial Margin. |
| 32 | `DCIS_LATERAL_MARGIN` | NUMERIC |  | CAP synoptic form item: DCIS Distance to Lateral Margin. |
| 33 | `DCIS_OTHER_MARGIN` | NUMERIC |  | CAP synoptic form item: DCIS Distance from Other Specified margin. |
| 34 | `DCIS_DESIGNAT_MRG` | VARCHAR |  | CAP synoptic form item: DCIS Designation of Margin. |
| 35 | `DCIS_SUPERIOR_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: DCIS Superior Margin Extent. |
| 36 | `DCIS_INFERIOR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: DCIS Inferior Margin Extent. |
| 37 | `DCIS_ANTERIOR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: DCIS Anterior Margin Extent. |
| 38 | `DCIS_POSTERR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: DCIS Posterior Margin Extent. |
| 39 | `DCIS_MEDIAL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: DCIS Medial Margin Extent. |
| 40 | `DCIS_LATER_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: DCIS Lateral Margin Extent. |
| 41 | `LYM_ND_NOT_PRES_YN` | VARCHAR |  | CAP synoptic form item: Lymph Nodes Present in Specimen. |
| 42 | `TOT_NUM_LYM_ND_EXAM` | NUMERIC |  | CAP synoptic form item: Total Number of Lymph Nodes Examined (Sentinel and Nonsentinel). |
| 43 | `NUM_LYM_ND_ISO_TMR` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Isolated Tumor Cells. |
| 44 | `MIC_MC_METAS_PRE_YN` | VARCHAR |  | CAP synoptic form item: Micro/Macro Metastases Present. |
| 45 | `NUM_LYM_ND_MACROMET` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Macrometastases. |
| 46 | `NUM_LYM_ND_MICROMET` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Micrometastases. |
| 47 | `SZ_LRGST_METAS_DEP` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Deposit. |
| 48 | `LYMPH_NODES_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes - Specify Units. |
| 49 | `SENT_BIOP_NT_PER_YN` | VARCHAR |  | CAP synoptic form item: Sentinel Lymph Node - Biopsy Not Performed. |
| 50 | `NUM_SENT_LYM_EXAM` | NUMERIC |  | CAP synoptic form item: Number of Sentinel Lymph Nodes Examined. |
| 51 | `EVAL_SENT_ND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Method of Evaluation of Sentinel Lymph Nodes. |
| 52 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 53 | `ESTRGN_RECEPTOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor. |
| 54 | `ESTROGEN_RECP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Estrogen Receptor. |
| 55 | `ESTRGN_ANTBOD_VEND` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Antibody Vendor and Clone. |
| 56 | `ESTRGN_TYPE_FIXTVE` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Type of Fixative. |
| 57 | `PROGESTERONE_RECP_C_NAME` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor. |
| 58 | `PRGSTRN_RECP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Progesterone Receptor. |
| 59 | `PRGSTN_ANTBOD_VEND` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Antibody Vendor. |
| 60 | `PRGSTN_TYPE_FIXTIVE` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Type of Fixative. |
| 61 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 62 | `LYMPH_ND_MODIFIE_YN` | VARCHAR |  | CAP synoptic form item: Lymph Node Modifier. |
| 63 | `LYMPH_ND_CAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Node Category. |
| 64 | `LYM_ND_CAT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Lymph Node Category. |
| 65 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 66 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 67 | `PR_TREAT_DCIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Prior Neoadjuvant Treatment for this Diagnosis of DCIS. |
| 68 | `ESTROGEN_ANTIBODY` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Antibody. |
| 69 | `PROGESTER_ANTIBODY` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Antibody. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

