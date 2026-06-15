# LUNG_RESECTION

> Stores single response data for College of American Pathologists (CAP) form 76030-Lung: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 52  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 12 | `CLOSEST_MRG_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Closest Margin. |
| 13 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 14 | `VISC_PLEURA_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Visceral Pleura Invasion. |
| 15 | `SPECIAL_STD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Special Studies. |
| 16 | `EPIDRM_GRWTH_FACTOR` | VARCHAR |  | CAP synoptic form item: Specify Epidermal Growth Factor Receptor (EGFR) Analysis Results. |
| 17 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 18 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 19 | `REG_LMPH_SITE_SPEC` | VARCHAR |  | CAP synoptic form item: Specify Regional Lymph Nodes Site. |
| 20 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 21 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 22 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 23 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 24 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 25 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 26 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 27 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 28 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 29 | `TUM_FOC_SEP_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Separate Tumor Nodules in Different Lobes. |
| 30 | `TUM_FOC_SYNC_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Synchronous carcinomas. |
| 31 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 32 | `KRAS_MUT_ANLYS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify KRAS Mutational Analysis. |
| 33 | `TMR_EXTENSION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Extension. |
| 34 | `PARENCHYMAL_MRG_C_NAME` | VARCHAR | org | CAP synoptic form item: Parenchymal margin. |
| 35 | `INFLAMMATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Inflammation. |
| 36 | `HST_TYP_OTHR_NONSML` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify type of other non-small cell carcinoma component. |
| 37 | `CHEST_WALL_STRUCT` | VARCHAR |  | CAP synoptic form item: Tumor Extension - Specify Chest Wall Involved Structures. |
| 38 | `MEDIAST_INV_STRUCT` | VARCHAR |  | CAP synoptic form item: Tumor Extension - Specify Mediastinum Involved Structures. |
| 39 | `BRON_MRG_INV_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Bronchial Margin Involvement by Invasive Carcinoma. |
| 40 | `BRON_MRG_SQM_CIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Bronchial Margin Involvement by Squamous Cell Carcinoma in situ (CIS). |
| 41 | `VASCULAR_MARGIN_C_NAME` | VARCHAR |  | CAP synoptic form item: Vascular Margin. |
| 42 | `PARIETL_PLEUR_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Parietal Pleural Margin. |
| 43 | `CHEST_WALL_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Chest Wall Margin. |
| 44 | `OTHR_ATT_TISS_MRG_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Attached Tissue Margin. |
| 45 | `OTHR_ATT_TISS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Other Attached Tissue Margin. |
| 46 | `OTHR_ATT_TISS_ASM_C_NAME` | VARCHAR |  | CAP synoptic form item: Other Attached Tissue Margin Assessment. |
| 47 | `TMR_ASSC_ATELECTS_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Associated Atelectasis or Obstructive Pneumonitis. |
| 48 | `ADDL_PATH_METAPLASI` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings - Specify Metaplasia. |
| 49 | `SPEC_LOBE_SPCFY` | VARCHAR |  | CAP synoptic form item: Specimen - Specify Lobes of Lung. |
| 50 | `SPEC_BRONC_SPFY` | VARCHAR |  | CAP synoptic form item: Specimen - Specify Bronchus. |
| 51 | `REG_LMPH_NUM_CBT_YN` | VARCHAR |  | CAP synoptic form item: Regional Lymph Nodes Number Cannot be Determined. |
| 52 | `HST_TYP_NONSML_CARC` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify type of non-small cell carcinoma component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

