# TROPHOBLAST_RESECT

> Stores data for College of American Pathologists (CAP) form 76057-TROPHOBLAST: Dilation and Curettage, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 25  
**Org-specific columns:** 4

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
| 8 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 9 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 10 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 11 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 12 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 13 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 14 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 15 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 16 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 17 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 18 | `MIC_EXT_ORG_SEP_MET` | VARCHAR |  | CAP synoptic form item: Microscopic Tumor Extension: Specify Organs with Separate Metastasis. |
| 19 | `FETAL_TISSUE_C_NAME` | VARCHAR | org | CAP synoptic form item: Fetal Tissue (Macroscopic or Microscopic). |
| 20 | `FETAL_TISSUE_TYPE` | VARCHAR |  | CAP synoptic form item: Fetal Tissue - Specify Type. |
| 21 | `FETAL_ANOMALIES_C_NAME` | VARCHAR |  | CAP synoptic form item: Fetal Anomalies. |
| 22 | `FETAL_ANOM_SPECIFY` | VARCHAR |  | CAP synoptic form item: Fetal Anomalies - Specify Type. |
| 23 | `NUM_METASTASES_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis Number of Metastases. |
| 24 | `DIST_META_NA_YN` | VARCHAR |  | CAP synoptic form item: Distant Metastasis: Not Applicable. |
| 25 | `TMR_OTH_NON_GENITAL` | VARCHAR |  | CAP synoptic form item: Tumor Extends to Other nongenital Organs or Structures. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

