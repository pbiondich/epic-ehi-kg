# ANUS_EXCISION_BIOP

> Stores single response data for College of American Pathologists (CAP) form 76003-ANUS: EXCISIONAL BIOPSY OR LOCAL EXCISION.

**Primary key:** `RESULT_ID`  
**Columns:** 27  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `NEOADJ_THRPY_TYPE` | VARCHAR |  | CAP synoptic form item: Neoadjuvant Therapy Type. |
| 3 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 6 | `SPEC_INTEGRITY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify specimen integrity. |
| 7 | `NUM_PIECE_FRAG_SPEC` | NUMERIC |  | CAP synoptic form item: Number of Pieces in Fragmented Specimens. |
| 8 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 9 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 10 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 11 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 12 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 13 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 14 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 15 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 16 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 17 | `TREATMNT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 18 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 19 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 20 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 21 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 22 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 23 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 24 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 25 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 26 | `MUC_MRG_CARC_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucosal Margin Carcinoma in Situ. |
| 27 | `MARGINS_NA` | VARCHAR |  | CAP synoptic form item: Margins Not Applicable. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

