# INVAS_CARC_BREAS_3

> Stores data for College of American Pathologists (CAP) form 76012-INVASIVE CARCINOMA OF THE BREAST: Complete Excision (Less Than Total Mastectomy, Including Specimens Designated Biopsy, Lumpectomy, Quadrantectomy, and Partial Mastectomy With or Without Axillary Contents) and Mastectomy (Total, Modified Radical, Radical With or Without Axillary Contents).

**Primary key:** `RESULT_ID`  
**Columns:** 20  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `FISH_SPECIMEN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Fluorescence In Situ Hybridization (FISH) Specimen. |
| 3 | `FISH_RESULTS_C_NAME` | VARCHAR | org | CAP synoptic form item: Fluorescence In Situ Hybridization (FISH) Results. |
| 4 | `AVG_NUM_HER2_CELL` | NUMERIC |  | CAP synoptic form item: Average Number of HER2 Gene Copies per Cell. |
| 5 | `AVG_NUM_CHROM_17` | NUMERIC |  | CAP synoptic form item: Average Number of Chromosome 17 per Cell. |
| 6 | `RATIO_HER2_CHROM_17` | NUMERIC |  | CAP synoptic form item: Ratio of HER2 Gene Copies to Chromosome 17. |
| 7 | `FISH_RESULT_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Fluorescence In Situ Hybridization (FISH) Results. |
| 8 | `FISH_NAME_OF_ASSAY` | VARCHAR |  | CAP synoptic form item: Fluorescence In Situ Hybridization (FISH) Name of Assay. |
| 9 | `FISH_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Fluorescence In Situ Hybridization (FISH). |
| 10 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 11 | `LYMPH_ND_MODIFIE_YN` | VARCHAR |  | CAP synoptic form item: Lymph Node Modifier. |
| 12 | `LYMPH_ND_CAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Node Category. |
| 13 | `LYM_ND_CAT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Lymph Node Category. |
| 14 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 15 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 16 | `CARC_INVAD_DERMIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Invasive carcinoma directly invades into the dermis or epidermis. |
| 17 | `RADIOGRAP_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify radiographic findings. |
| 18 | `ESTROGEN_RECP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Estrogen Receptor. |
| 19 | `TMR_NO_RESID_SIZ_YN` | VARCHAR |  | CAP synoptic form item: Tumor No Residual Invasive Carcinoma After Presurgical (Neoadjuvant) Therapy for the Tumor Size section. |
| 20 | `TMR_NO_RESID_SP_YN` | VARCHAR |  | CAP synoptic form item: Tumor No Residual Invasive Carcinoma After Presurgical (Neoadjuvant) Therapy for the Special Studies section. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

