# LIP_AND_ORAL_CAV_2

> Stores single response data for College of American Pathologists (CAP) form 76029-LIP AND ORAL CAVITY: INCISIONAL BIOPSY, EXCISIONAL BIOPSY, RESECTION.

**Primary key:** `RESULT_ID`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `MARGIN_IN_SITU_SPFY` | VARCHAR |  | CAP synoptic form item: Margins In Situ Specify Margins Per Orientation. |
| 3 | `SPECIAL_STUDY_TYPES` | VARCHAR |  | CAP synoptic form item: Special Studies - Specify Types. |
| 4 | `PT_FOR_MUC_MAL_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor for Mucosal Malignant Melanoma. |
| 5 | `REG_LYM_MUCOS_MEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN) for Mucosal Malignant Melanoma. |
| 6 | `MARGIN_SITU_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins in Situ Distance of Carcinoma in Situ from Closest. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

