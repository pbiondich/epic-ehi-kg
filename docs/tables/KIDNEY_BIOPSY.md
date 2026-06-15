# KIDNEY_BIOPSY

> Stores data for College of American Pathologists (CAP) form 76026-KIDNEY: Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 5 | `FUHRMAN_NUCLR_GRD_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade (Fuhrman Nuclear Grade). |
| 6 | `SARCOMATOID_FEAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Sarcomatoid Features. |
| 7 | `PERCN_SARCOMAT_ELEM` | NUMERIC |  | CAP synoptic form item: Specify Percentage Sarcomatoid Element. |
| 8 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

