# STG_CS_INFO

> This table stores cancer staging information that was determined using Collaborative Staging (CS) or Surveillance, Epidemiology, and End Results (SEER) methods. Note that the only records extracted into this table are those with the Has Collaborative Staging Info (I STG 32) item (KB_SQL column HAS_CS_INFO_C) set to 1.

**Primary key:** `STAGE_ID`  
**Columns:** 32  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The cancer stage ID. |
| 2 | `STAGE_TITLE_NM` | VARCHAR |  | The title of this cancer stage row, usually indicative of the body site or cancer type being staged. |
| 3 | `CS_SITE` | VARCHAR |  | The collaborative staging primary tumor site, using an ICD-O-3 code. |
| 4 | `CS_HISTOLOGY` | VARCHAR |  | The collaborative staging histology, using an ICD-O-3 code. |
| 5 | `CS_GRADE` | VARCHAR |  | The tumor cell grade for collaborative staging. |
| 6 | `CS_BEHAVIOR` | VARCHAR |  | The tumor behavior for collaborative staging. |
| 7 | `CS_SIZE` | VARCHAR |  | The tumor size for collaborative staging. |
| 8 | `CS_EXTENSION` | VARCHAR |  | The tumor extension for collaborative staging. |
| 9 | `CS_EXT_EVAL` | VARCHAR |  | The collaborative staging extension evaluation methods. |
| 10 | `CS_NODES` | VARCHAR |  | The regional lymph nodes for collaborative staging. |
| 11 | `CS_REG_LN_EVAL` | VARCHAR |  | The regional lymph nodes evaluation methods for collaborative staging. |
| 12 | `CS_REG_LN_POS` | VARCHAR |  | The number of regional lymph nodes that were positive, as documented using the corresponding code for collaborative staging. |
| 13 | `CS_REG_LN_EXAM` | VARCHAR |  | The number of regional lymph nodes that were examined, as documented using the corresponding code for collaborative staging. |
| 14 | `CS_METS` | VARCHAR |  | The distant metastasis component for collaborative staging. |
| 15 | `CS_METS_EVAL` | VARCHAR |  | The metastasis evaluation methods for collaborative staging. |
| 16 | `CS_SSF1` | VARCHAR |  | The collaborative staging site specific factor 1. |
| 17 | `CS_SSF2` | VARCHAR |  | The collaborative staging site specific factor 2. |
| 18 | `CS_SSF3` | VARCHAR |  | The collaborative staging site specific factor 3. |
| 19 | `CS_SSF4` | VARCHAR |  | The collaborative staging site specific factor 4. |
| 20 | `CS_SSF5` | VARCHAR |  | The collaborative staging site specific factor 5. |
| 21 | `CS_SSF6` | VARCHAR |  | The collaborative staging site specific factor 6. |
| 22 | `CS_TDESCR` | VARCHAR |  | The primary tumor description for collaborative staging. |
| 23 | `CS_NDESCR` | VARCHAR |  | The regional lymph nodes description for collaborative staging. |
| 24 | `CS_MDESCR` | VARCHAR |  | The distant metastasis description for collaborative staging. |
| 25 | `CS_SS77_C_NAME` | VARCHAR | org | The SEER stage according to Summary Stage 1977. |
| 26 | `CS_SS2000_C_NAME` | VARCHAR |  | The SEER stage according to Summary Stage 2000. |
| 27 | `SEER77_T_C_NAME` | VARCHAR |  | The SEER 77 primary tumor grade. |
| 28 | `SEER77_N_C_NAME` | VARCHAR |  | The SEER 77 regional lymph nodes grade. |
| 29 | `SEER77_M_C_NAME` | VARCHAR |  | The SEER 77 distant metastasis grade. |
| 30 | `SEER00_T_C_NAME` | VARCHAR |  | The SEER 2000 primary tumor grade. |
| 31 | `SEER00_N_C_NAME` | VARCHAR |  | The SEER 2000 regional lymph nodes grade. |
| 32 | `SEER00_M_C_NAME` | VARCHAR |  | The SEER 2000 distant metastasis grade. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

