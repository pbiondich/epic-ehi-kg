# COLON_RECTUM_BIOP

> Stores data for College of American Pathologists (CAP) form 76014-COLON AND RECTUM: Excisional Biopsy (Polypectomy).

**Primary key:** `RESULT_ID`  
**Columns:** 25  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 5 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 6 | `POLYP_CONFIGURATN_C_NAME` | VARCHAR | org | CAP synoptic form item: Polyp Configuration. |
| 7 | `PENDNCLTD_STALK_LEN` | NUMERIC |  | CAP synoptic form item: Pedunculated Stalk Length. |
| 8 | `POLYP_SIZE_C_NAME` | VARCHAR | org | CAP synoptic form item: Polyp Size. |
| 9 | `POLYP_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Polyp Size Greatest Dimension. |
| 10 | `POLYP_SIZE_ADDL_DIM` | NUMERIC |  | CAP synoptic form item: Polyp Size Length. |
| 11 | `POLYP_SIZE_ADDL_2` | NUMERIC |  | CAP synoptic form item: Polyp Size Width. |
| 12 | `POLYP_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Polyp Size. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `INV_CARC_SIZE_C_NAME` | VARCHAR |  | CAP synoptic form item: Size of Invasive Carcinoma. |
| 15 | `INV_CARCINOMA_GREAT` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Greatest Dimension. |
| 16 | `INV_CARC_ADDL_DIM` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Length. |
| 17 | `INV_CARC_ADDL_DIM2` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Width. |
| 18 | `INV_CARCINOMA_SPFY` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Specify. |
| 19 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 20 | `MUCSL_INVL_ADENO_YN` | VARCHAR |  | CAP synoptic form item: Mucosal / Lateral Margin Involved by Adenoma. |
| 21 | `MUCOSAL_LATER_MRG_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucosal / Lateral Margin. |
| 22 | `INV_CARC_AROSE_C_NAME` | VARCHAR | org | CAP synoptic form item: Type of Polyp in Which Invasive Carcinoma Arose. |
| 23 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 24 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 25 | `INFLAM_BOWEL_DIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Inflammatory Bowel Disease. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

