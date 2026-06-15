# STG_INFO

> This table stores general information about the stage of a patient's cancer, including clinical and pathologic staging attributes that were determined using methods defined by the American Joint Committee on Cancer (AJCC).

**Primary key:** `STAGE_ID`  
**Columns:** 38  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The cancer stage ID. |
| 2 | `STAGE_TITLE_NM` | VARCHAR |  | The title of this cancer stage row, usually indicative of the body site or cancer type being staged. |
| 3 | `STAGE_TYPE_C_NAME` | VARCHAR |  | The type of stage in this record: Free Text, AJCC, SEER, or Pediatric. |
| 4 | `STAGE_CLASS_C_NAME` | VARCHAR |  | The classification of the stage in this row, for example Clinical or Pathologic. |
| 5 | `STAGE` | VARCHAR |  | The free text stage in this row. |
| 6 | `STG_PAT_ID` | VARCHAR | FK→ | The ID of the patient to which the stage in this row applies. |
| 7 | `STG_BODY_SITE_C_NAME` | VARCHAR | org | The body site to which the stage in this row applies. |
| 8 | `AJCC_LV_INV_C_NAME` | VARCHAR | org | The lymphatic vessel invasion of the AJCC stage. |
| 9 | `AJCC_VENOUS_INV_C_NAME` | VARCHAR | org | The venous invasion of the AJCC stage. |
| 10 | `AJCC_RESIDUAL_C_NAME` | VARCHAR | org | The residual tumor of the AJCC stage. |
| 11 | `AJCC_HIST_GRADE_C_NAME` | VARCHAR | org | The histologic grade of the AJCC stage. |
| 12 | `AJCC_STAGE_C_NAME` | VARCHAR | org | The AJCC stage for the diagnosis. |
| 13 | `AJCC_PATH_STAGE_C_NAME` | VARCHAR |  | The AJCC pathologic stage. |
| 14 | `AJCC_CLIN_STAGE_C_NAME` | VARCHAR |  | The AJCC clinical stage. |
| 15 | `AJCC_T_C_NAME` | VARCHAR | org | The primary tumor component of the summary stage. |
| 16 | `AJCC_PATH_T_C_NAME` | VARCHAR |  | The primary tumor component of the pathologic stage. |
| 17 | `AJCC_CLIN_T_C_NAME` | VARCHAR |  | The primary tumor component of the clinical stage. |
| 18 | `AJCC_N_C_NAME` | VARCHAR | org | The regional lymph nodes component of the summary stage. |
| 19 | `AJCC_PATH_N_C_NAME` | VARCHAR |  | The regional lymph nodes component of the pathologic stage. |
| 20 | `AJCC_CLIN_N_C_NAME` | VARCHAR |  | The regional lymph nodes component of the clinical stage. |
| 21 | `AJCC_M_C_NAME` | VARCHAR | org | The distant metastasis component of the summary stage. |
| 22 | `AJCC_PATH_M_C_NAME` | VARCHAR |  | The distant metastasis component of the pathologic stage. |
| 23 | `AJCC_CLIN_M_C_NAME` | VARCHAR |  | The distant metastasis component of the clinical stage. |
| 24 | `CLIN_STAGE_STS_C_NAME` | VARCHAR |  | The clinical stage status, such as New, Assigned, or Started. |
| 25 | `CLIN_SIGN_USR_ID` | VARCHAR |  | The user ID of the last person to sign the clinical stage in this row. |
| 26 | `CLIN_SIGN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `CLIN_SIGN_INST` | DATETIME (Local) |  | The date/time in external format of the last time the clinical stage in this row was signed. |
| 28 | `PATH_STAGE_STS_C_NAME` | VARCHAR |  | The pathologic stage status. |
| 29 | `PATH_SIGN_USR_ID` | VARCHAR |  | The user ID of the last person to sign the pathologic stage in this row. |
| 30 | `PATH_SIGN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `PATH_SIGN_INST` | DATETIME (Local) |  | The date/time in external format of the last time the pathologic stage in this row was signed. |
| 32 | `UNK_PRIM_SITE_YN` | VARCHAR |  | Yes/no flag as to whether the primary tumor site or cancer type listed in the Body Site (I STG 65, STG_BODY_SITE_C) is merely suspected instead of being known for certain. |
| 33 | `HAS_CS_INFO_YN` | VARCHAR |  | Yes/no flag as to whether this STG row contains any collaborative staging (CS) information. |
| 34 | `STAGE_METHOD_VERS_C_NAME` | VARCHAR | org | Specifies the staging methodology (or version of that methodology) that is used to stage this cancer, from the Staging Method or Version (I FCS 60) of the corresponding Cancer Staging Definitions (FCS) record. |
| 35 | `STAGE_CONV_SRC_ID` | NUMERIC |  | For each new stage (STG) record created by the Epic 2014 cancer staging conversion, this item will store the ID of the stage record that it was created from. |
| 36 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category number for the stage (e.g. soft-deleted). |
| 37 | `LINKED_PROBLEM_LIST_ID` | NUMERIC |  | Virtual item that holds the problem list record ID (LPL) the stage belongs to. |
| 38 | `IS_STAGE_DELETED_YN` | VARCHAR |  | Virtual item that checks the latest contact of the Data Model Version (I STG 64) and Status (I STG 620) to determine if the stage record is deleted or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `STG_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

