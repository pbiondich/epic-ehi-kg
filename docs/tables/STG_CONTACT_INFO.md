# STG_CONTACT_INFO

> This table stores contact-specific information for a cancer stage (STG) record. Each row in this table corresponds to a single set of edits that were all saved at the same time.

**Primary key:** `STAGE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 88  
**Org-specific columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The cancer stage (STG) row ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `STG_CSN` | NUMERIC |  | A unique serial number for this contact. This number is unique across all stage (STG) contacts in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 6 | `CONTACT_NUM` | INTEGER |  | A sequential number to identify this contact uniquely within the cancer stage (STG) row. The first contact is number 1, the second is number 2, etc. |
| 7 | `STAGE_EDIT_DATETIME` | DATETIME (Local) |  | The instant this contact was created. |
| 8 | `STAGE_EDIT_USR_ID` | VARCHAR |  | The user ID of the person who created this contact. |
| 9 | `STAGE_EDIT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LATERALITY_C_NAME` | VARCHAR |  | A category value indicating the laterality (left, right, or both) of the cancer being staged, for a disease such as lung cancer or breast cancer which might affect one or both sides of the body. This column should be empty for a disease such as colon cancer which can only affect one area of the body. |
| 11 | `TUMOR_SIZE_MM` | NUMERIC |  | The size of the primary tumor. This value is always stored in millimeters, although the user may choose to display this value in centimeters instead. |
| 12 | `TUM_SIZ_DISP_UNIT_C_NAME` | VARCHAR |  | The preferred unit of measurement (millimeters or centimeters) to use when displaying the primary tumor size for this contact of the cancer stage record. |
| 13 | `STG_SPECMN_TYPE_C_NAME` | NUMERIC | org | A category value indicating the type of specimen that was collected to analyze the tumor. |
| 14 | `HISTOPATH_TYPE_C_NAME` | VARCHAR | org | A category value indicating the histopathologic type of the patient's cancer. |
| 15 | `PATH_NODES_EXAM` | INTEGER |  | The number of regional lymph nodes examined for pathologic staging. |
| 16 | `PATH_POS_NODES` | INTEGER |  | The number of regional lymph nodes that tested positive for cancer for pathologic staging. |
| 17 | `CLIN_NODES_EXAM` | INTEGER |  | The number of regional lymph nodes examined for clinical staging. |
| 18 | `CLIN_POS_NODES` | INTEGER |  | The number of regional lymph nodes that tested positive for cancer for clinical staging. |
| 19 | `PATH_CEA_LVL` | NUMERIC |  | The patient's carcinoembryonic antigen (CEA) level, in ng/mL, entered as part of the pathologic stage for an incidence of colorectal cancer. |
| 20 | `CLIN_CEA_LVL` | NUMERIC |  | The patient's carcinoembryonic antigen (CEA) level, in ng/mL, entered as part of the clinical stage for an incidence of colorectal cancer. |
| 21 | `PATH_PSA_LVL` | NUMERIC |  | The patient's prostate-specific antigen (PSA) level, in ng/mL, entered as part of the pathologic stage for an incidence of prostate cancer. |
| 22 | `PATH_PRIM_GLEASON` | INTEGER |  | The primary Gleason pattern (1-5), entered as part of the pathologic stage for an incidence of prostate cancer. |
| 23 | `PATH_SEC_GLEASON` | INTEGER |  | The secondary Gleason pattern (1-5), entered as part of the pathologic stage for an incidence of prostate cancer. |
| 24 | `CLIN_PSA_LVL` | NUMERIC |  | The patient's prostate-specific antigen (PSA) level, in ng/mL, entered as part of the clinical stage for an incidence of prostate cancer. |
| 25 | `CLIN_PRIM_GLEASON` | INTEGER |  | The primary Gleason pattern (1-5), entered as part of the clinical stage for an incidence of prostate cancer. |
| 26 | `CLIN_SEC_GLEASON` | INTEGER |  | The secondary Gleason pattern (1-5), entered as part of the clinical stage for an incidence of prostate cancer. |
| 27 | `PATH_FIBROSIS_SCORE` | INTEGER |  | A numeric score (0-6) indicating the severity of fibrosis, entered as part of the pathologic stage for an incidence of liver cancer. |
| 28 | `PATH_FIBROSIS_C_NAME` | VARCHAR |  | A code value (0 meaning "F0", or 1 meaning "F1") indicating the severity of fibrosis, entered as part of the pathologic stage for an incidence of liver cancer. F0 corresponds to a fibrosis score of 0 to 4, while F1 corresponds to a score of 5 or 6. |
| 29 | `CLIN_FIBROSIS_SCORE` | INTEGER |  | A numeric score (0-6) indicating the severity of fibrosis, entered as part of the clinical stage for an incidence of liver cancer. |
| 30 | `CLIN_FIBROSIS_C_NAME` | VARCHAR |  | A code value (0 meaning "F0", or 1 meaning "F1") indicating the severity of fibrosis, entered as part of the clinical stage for an incidence of liver cancer. F0 corresponds to a fibrosis score of 0 to 4, while F1 corresponds to a score of 5 or 6. |
| 31 | `PATH_VISUAL_ACUITY` | VARCHAR |  | A description of the patient's visual acuity, using Snellen shorthand or an equivalent system, entered as part of the pathologic stage for a malignant melanoma of the uvea. |
| 32 | `CLIN_VISUAL_ACUITY` | VARCHAR |  | A description of the patient's visual acuity, using Snellen shorthand or an equivalent system, entered as part of the clinical stage for a malignant melanoma of the uvea. |
| 33 | `PATH_METS_BIOPSY_YN` | VARCHAR |  | Yes/no flag indicating whether a biopsy of the metastatic site was taken in conjunction with the pathologic stage. |
| 34 | `PATH_METS_SPEC_C_NAME` | VARCHAR | org | A category value specifying the source of the metastatic specimen taken in conjunction with the pathologic stage (if any). |
| 35 | `CLIN_METS_BIOPSY_YN` | VARCHAR |  | Yes/no flag indicating whether a biopsy of the metastatic site was taken in conjunction with the clinical stage. |
| 36 | `CLIN_METS_SPEC_C_NAME` | VARCHAR |  | A category value specifying the source of the metastatic specimen taken in conjunction with the clinical stage (if any). |
| 37 | `OT_AJCC_CLIN_STG_C_NAME` | VARCHAR | org | The AJCC clinical stage grouping for this contact. |
| 38 | `OT_CLIN_MULT_TUM_YN` | VARCHAR |  | Yes/no flag indicating whether the clinical stage was documented based on the presence of multiple primary tumors. |
| 39 | `OT_AJCC_CLIN_T_C_NAME` | VARCHAR | org | The AJCC primary tumor (T) assessment for this contact of the clinical stage. |
| 40 | `OT_AJCC_CLIN_N_C_NAME` | VARCHAR | org | The AJCC regional lymph nodes (N) assessment for this contact of the clinical stage. |
| 41 | `OT_AJCC_CLIN_M_C_NAME` | VARCHAR | org | The AJCC distant metastasis (M) assessment for this contact of the clinical stage. |
| 42 | `OT_AJCC_CLIN_G_C_NAME` | VARCHAR | org | The AJCC histologic grade (G) assessment for this contact of the clinical stage. |
| 43 | `OT_AJCC_CLIN_SER_C_NAME` | VARCHAR | org | The AJCC serum tumor markers (S) assessment for this contact of the clinical stage. |
| 44 | `OT_AJCC_CLIN_RISK_C_NAME` | VARCHAR | org | The AJCC risk factors assessment for this contact of the clinical stage. |
| 45 | `OT_FIGO_CLIN_STG_C_NAME` | VARCHAR |  | The clinical FIGO stage for an incidence of gynecologic cancer. |
| 46 | `OT_AJCC_PATH_STG_C_NAME` | VARCHAR |  | The AJCC pathologic stage grouping for this contact. |
| 47 | `OT_PATH_MULT_TUM_YN` | VARCHAR |  | Yes/no flag indicating whether the pathologic stage was documented based on the presence of multiple primary tumors. |
| 48 | `OT_AJCC_PATH_T_C_NAME` | VARCHAR |  | The AJCC primary tumor (T) assessment for this contact of the pathologic stage. |
| 49 | `OT_AJCC_PATH_N_C_NAME` | VARCHAR |  | The AJCC regional lymph nodes (N) assessment for this contact of the pathologic stage. |
| 50 | `OT_AJCC_PATH_M_C_NAME` | VARCHAR |  | The AJCC distant metastasis (M) assessment for this contact of the pathologic stage. |
| 51 | `OT_AJCC_PATH_G_C_NAME` | VARCHAR |  | The AJCC histologic grade (G) assessment for this contact of the pathologic stage. |
| 52 | `OT_AJCC_PATH_SER_C_NAME` | VARCHAR |  | The AJCC serum tumor markers (S) assessment for this contact of the pathologic stage. |
| 53 | `OT_AJCC_PATH_RISK_C_NAME` | VARCHAR |  | The AJCC risk factors assessment for this contact of the pathologic stage. |
| 54 | `OT_FIGO_PATH_STG_C_NAME` | VARCHAR |  | The pathologic FIGO stage for an incidence of gynecologic cancer. |
| 55 | `OT_AJCC_RESIDUAL_C_NAME` | VARCHAR | org | The AJCC residual tumor (R) assessment for this contact of the pathologic stage. |
| 56 | `OT_AJCC_LV_INV_C_NAME` | VARCHAR | org | The AJCC lymphatic vessel invasion (L) assessment for this contact of the pathologic stage. |
| 57 | `OT_AJCC_VEN_INV_C_NAME` | VARCHAR | org | The AJCC venous invasion (V) assessment for this contact of the pathologic stage. |
| 58 | `OT_UNK_PRIM_SITE_YN` | VARCHAR |  | Yes/no flag indicating whether the primary tumor site is uncertain and therefore can only be suspected. |
| 59 | `OT_CLIN_STAGE_STS_C_NAME` | VARCHAR |  | The status of the clinical stage on this contact. |
| 60 | `OT_CLIN_SIGN_USR_ID` | VARCHAR |  | The user ID of the person who signed the clinical stage. |
| 61 | `OT_CLIN_SIGN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 62 | `OT_CLIN_SIGN_DTTM` | DATETIME (Attached) |  | The instant at which the clinical stage was signed. |
| 63 | `OT_PATH_STAGE_STS_C_NAME` | VARCHAR |  | The status of the pathologic stage on this contact. |
| 64 | `OT_PATH_SIGN_USR_ID` | VARCHAR |  | The user ID of the person who signed the pathologic stage. |
| 65 | `OT_PATH_SIGN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 66 | `OT_PATH_SIGN_DTTM` | DATETIME (Attached) |  | The instant at which the pathologic stage was signed. |
| 67 | `STAGE_EPT_ENC_DAT` | VARCHAR |  | Stores the contact date (DAT) of the patient (EPT) contact in which this STG contact was edited. Set to 99999 if the stage is edited in a patient chart outside of an encounter. |
| 68 | `STAGE_EPT_ENC_CSN` | NUMERIC | FK→ | Stores the contact serial number (CSN) of the patient encounter in which this stage contact was edited. Empty if the stage is edited in a patient chart outside of an encounter. |
| 69 | `STAGE_ENC_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 70 | `STAGE_LOGIN_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 71 | `STG_DEF_ID_STG_DEF_NAME` | VARCHAR |  | The name of the FCS record containing the Cancer Staging Definitions for a kind of cancer to be staged. |
| 72 | `STG_DEF_DAT` | NUMERIC |  | Contact date of the cancer staging form (FCS) contact for the staging form that was used when entering the cancer staging information in this contact. |
| 73 | `STG_DEF_CSN` | NUMERIC |  | Contact serial number of the cancer staging form (FCS) contact for the staging form that was used when entering the cancer staging information in this contact. |
| 74 | `DX_CONFIRM_C_NAME` | VARCHAR | org | Indicates the best method used to confirm the presence of a patient's cancer being reported to a cancer registry. |
| 75 | `CLIN_STAGED_BY_C_NAME` | VARCHAR | org | Indicates the person or people who assigned the AJCC staging elements and stage group when staging a patient's cancer diagnosis. |
| 76 | `STAGING_DATE` | DATETIME |  | Allows the user to specify a date associated with the staging information being entered. |
| 77 | `BODY_SITE_C_NAME` | VARCHAR | org | Stores the calculated or user-selected body site of this cancer stage. |
| 78 | `STAGE_FORM_METHOD_C_NAME` | VARCHAR | org | Stores the method or version of the staging form used to document this stage. |
| 79 | `CLASSIFICATION_C_NAME` | VARCHAR | org | Stores the specific classification (clinical, pathologic, etc.) of this stage. |
| 80 | `DATA_MODEL_VER_C_NAME` | VARCHAR |  | Stores the version of this stage record's data model, used to indicate which items it uses in the Diagnosis Stage (STG) master file. |
| 81 | `STAGE_DATE` | DATETIME |  | Stores the date associated with this stage. |
| 82 | `STAGE_GROUP` | VARCHAR |  | Stores the stage group as an easily accessible string. This value is obtained from a SmartData element on the stage form. |
| 83 | `STAGE_DESC` | VARCHAR |  | Stores a short description of this stage, typically including key values recorded by the user. |
| 84 | `STAGE_STATUS_C_NAME` | VARCHAR |  | Stores the status (unsigned, signed, deleted, etc.) of this stage. |
| 85 | `SIGN_USER_ID` | VARCHAR |  | If signed, stores the user who signed this stage. |
| 86 | `SIGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 87 | `SIGN_DATETIME` | DATETIME (UTC) |  | If signed, stores the instant in UTC that the stage was signed. |
| 88 | `STAGE_DT_FALLBACK_TO_CREATE_DT` | DATETIME |  | Stores the user-entered stage date, or if empty, the record creation date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `STAGE_EPT_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

