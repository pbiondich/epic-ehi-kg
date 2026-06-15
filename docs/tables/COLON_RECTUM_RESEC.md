# COLON_RECTUM_RESEC

> Stores data for College of American Pathologists (CAP) form 76015-COLON AND RECTUM: Resection, Including Transanal Disk Excision of Rectal Neoplasms.

**Primary key:** `RESULT_ID`  
**Columns:** 70  
**Org-specific columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CLOCK_POSITION_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Clock Position of Tumor Site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `MACRO_TMR_PERFRTN_C_NAME` | VARCHAR | org | CAP synoptic form item: Macroscopic Tumor Perforation. |
| 12 | `MACRO_INTCT_MESRC_C_NAME` | VARCHAR | org | CAP synoptic form item: Macroscopic Intactness of Mesorectum. |
| 13 | `TMR_PENETR_PERITONM` | VARCHAR |  | CAP synoptic form item: Tumor Penetrates to the Surface of Visceral Peritoneum. |
| 14 | `TMR_ADHER_OTHR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify the other organs or structures the tumor is adherent to. |
| 15 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 16 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 17 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 18 | `SPFY_MARGIN_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin Category. |
| 19 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 20 | `TREAT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 21 | `PERINEURAL_INVASN_C_NAME` | VARCHAR |  | CAP synoptic form item: Perineural Invasion. |
| 22 | `TUMOR_DEPOSITS_C_NAME` | VARCHAR |  | CAP synoptic form item: Tumor Deposits (Discontinuous Extramural Extension). |
| 23 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 24 | `SPEC_LENGTH` | NUMERIC |  | CAP synoptic form item: Specimen Length. |
| 25 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 26 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 27 | `INTRA_LYMPHCY_RSP_C_NAME` | VARCHAR | org | CAP synoptic form item: Intratumoral Lymphocytic Response. |
| 28 | `PERTM_LYMPHCY_RSP_C_NAME` | VARCHAR |  | CAP synoptic form item: Peritumor Lymphocytic Response (Crohn-like response). |
| 29 | `PERCN_MUCN_TMR_SPFY` | NUMERIC |  | CAP synoptic form item: Specify Percentage of Mucinous Tumor Component. |
| 30 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 31 | `PROX_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Proximal Margin Cannot Be Assessed. |
| 32 | `PROX_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement by Carcinoma / Adenoma. |
| 33 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 34 | `DIST_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Distal Margin Cannot Be Assessed. |
| 35 | `DIST_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Intramucosal Carcinoma - Adenoma. |
| 36 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 37 | `CIRCUMFERENTL_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Circumferential (Radial) Margin. |
| 38 | `LATERAL_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Lateral Margin. |
| 39 | `NON_CIRCM_DISK_EX_C_NAME` | VARCHAR |  | CAP synoptic form item: For Non-Circumferential Transanal Disk Excision. |
| 40 | `LATER_DIST_INV_CARC` | NUMERIC |  | CAP synoptic form item: Distance of Invasive Carcinoma from Closest Lateral Margin. |
| 41 | `LATERAL_SPFY_LOC` | VARCHAR |  | CAP synoptic form item: Lateral Margin - Specify Location. |
| 42 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 43 | `INV_CARC_AROSE_C_NAME` | VARCHAR | org | CAP synoptic form item: Type of Polyp in Which Invasive Carcinoma Arose. |
| 44 | `MICRO_INSTBLTY_MTHD` | VARCHAR |  | CAP synoptic form item: Microsatellite Instability Testing Method. |
| 45 | `SPECIAL_STDS_MLH1_C_NAME` | VARCHAR | org | CAP synoptic form item: Special Studies MLH1. |
| 46 | `SPECL_STD_MLH1_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies MLH1 Specify. |
| 47 | `SPECIAL_STDS_MSH2_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies MLH2. |
| 48 | `SPECL_STD_MSH2_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies MLH2 Specify. |
| 49 | `SPECIAL_STDS_MSH6_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies MSH6. |
| 50 | `SPECL_STD_MSH6_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2. |
| 51 | `SPECIAL_STDS_PMS2_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2. |
| 52 | `SPECL_STD_PMS2_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2 Specify. |
| 53 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 54 | `BRAF_MUTAT_ANALYS_C_NAME` | VARCHAR | org | CAP synoptic form item: BRAF V600E Mutational Analysis. |
| 55 | `BRAF_MUTATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify BRAF V600E Mutational Analysis. |
| 56 | `BRAF_MUT_TEST_METHD` | VARCHAR |  | CAP synoptic form item: BRAF V600E Mutational Analysis Testing Method. |
| 57 | `KRAS_MUTAT_ANALYS_C_NAME` | VARCHAR | org | CAP synoptic form item: KRAS Mutational Analysis. |
| 58 | `KRAS_MUT_ANLYS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify KRAS Mutational Analysis. |
| 59 | `KRAS_MUT_TEST_METHD` | VARCHAR |  | CAP synoptic form item: KRAS Mutational Analysis Testing Method. |
| 60 | `MUT_KRAS_DTCTD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mutant KRAS Detected. |
| 61 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 62 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 63 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 64 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 65 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 66 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 67 | `DIST_METAST_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Category version of Distant Metastasis Site. |
| 68 | `OTHER_POLYPS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other polyps. |
| 69 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 70 | `LATERAL_ADENOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Lateral Margin - Adenoma Involvement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

