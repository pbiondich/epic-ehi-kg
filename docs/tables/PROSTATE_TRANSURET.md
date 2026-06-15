# PROSTATE_TRANSURET

> Stores data for College of American Pathologists (CAP) form 76044-PROSTATE GLAND: Transurethral Prostatic Resection (TUR), Enucleation Specimen (Subtotal Prostatectomy).

**Primary key:** `RESULT_ID`  
**Columns:** 25  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPECIMEN_WEIGHT` | NUMERIC |  | CAP synoptic form item: Specimen Weight. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 6 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 7 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 10 | `SEMINAL_VESICLE_C_NAME` | VARCHAR | org | CAP synoptic form item: Seminal Vesicle Invasion. |
| 11 | `PERIPROSTATIC_FAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Periprostatic Fat Invasion. |
| 12 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `PRIMARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Gleason Pattern. |
| 15 | `SECONDARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Secondary Gleason Pattern. |
| 16 | `TOTAL_GLEASON_SCORE` | INTEGER |  | CAP synoptic form item: Total Gleason Score. |
| 17 | `NUM_POSITIVE_CHIPS` | INTEGER |  | CAP synoptic form item: Number of Positive Chips. |
| 18 | `TOTAL_NUM_CHIPS` | INTEGER |  | CAP synoptic form item: Total Number of Chips. |
| 19 | `PATH_INFLAM_SPFY` | VARCHAR |  | CAP synoptic form item: Additional Pathological Findings - Specify Inflammation. |
| 20 | `SPECIMEN_SIZE_SPEC1` | NUMERIC |  | CAP synoptic form item: Specimen Size Specify. |
| 21 | `SPECIMEN_SIZE_SPEC2` | NUMERIC |  | CAP synoptic form item: Specimen Size Specify 2. |
| 22 | `SPECIMEN_SIZE_SPEC3` | NUMERIC |  | CAP synoptic form item: Specimen Size Specify 3. |
| 23 | `TUR_SPEC_PROPORTION` | NUMERIC |  | CAP synoptic form item: TUR Specimens - Proportion (%) of prostatic tissue involved by tumor. |
| 24 | `ENU_SPEC_PROPORTION` | NUMERIC |  | CAP synoptic form item: Enucleation Specimens - Proportion (%) of prostatic tissue involved by tumor. |
| 25 | `TUR_SPE_TUMOR_QT_C_NAME` | VARCHAR | org | CAP synoptic form item: TUR Specimens - Tumor Quantitation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

