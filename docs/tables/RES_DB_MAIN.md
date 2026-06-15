# RES_DB_MAIN

> The RES_DB_MAIN is the primary table for storing results data.

**Primary key:** `RESULT_ID`  
**Columns:** 33  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `RES_VAL_STATUS_C_NAME` | VARCHAR |  | The validation status category number for the result. |
| 3 | `RES_SPECIMEN_ID` | VARCHAR |  | The unique ID of the specimen that is associated with the result record. |
| 4 | `RES_SPEC_NO_REL` | VARCHAR |  | The related external specimen ID number for the given result. It gets the specimen ID through related externa ID number (I OVR 10026), which in turn uses the specimen related external ID number (I OVS 26) for the first specimen associated with the result. |
| 5 | `RES_EPT_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient (EPT) associated with the result record. |
| 6 | `RES_GW_RESULT_ID` | VARCHAR |  | The unique ID of the result record for a general workcard associated with this result record. |
| 7 | `RES_OW_RESULT_ID` | VARCHAR |  | The unique ID of the organism workcard result record associated with this result record. |
| 8 | `RES_ABNORMAL_C_NAME` | VARCHAR | org | The abnormal level category number for the result. |
| 9 | `RES_ORDER_ID` | NUMERIC |  | The order ID associated with the result's test. It gets the order ID through the related external ID number (I OVR 10026) , which in turn uses order ID (I OVS 85) for the first specimen associated with the result. |
| 10 | `RES_TEST_MTHD_ID` | VARCHAR |  | The unique ID of the test method. |
| 11 | `RES_TEST_MTHD_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |
| 12 | `RES_VERIFY_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 13 | `RES_RQG_PAT_ID` | NUMERIC | FK→ | The unique ID of the non-participating submitter's patient (RQG) associated with the result record. |
| 14 | `CURRENT_ACTION_ID` | NUMERIC |  | The action which is currently in progress for the workcard. |
| 15 | `CURRENT_ACTION_ID_RECORD_NAME` | VARCHAR |  | The name of the node record. |
| 16 | `SLIDE_REVIEW_RPT_YN` | VARCHAR |  | Setting for a hematology test to determine if the Slide Review part of the test is reported out or not. |
| 17 | `DIFF_REPORTED_C_NAME` | VARCHAR |  | The type of differential reported category number for the result. Note: this item is used for CBC test only. Also note: unlike DIFF_TYPE_RPTD_C, this item is not set only during result transmittal and so may be set when DIFF_TYPE_RPTD_C is not. |
| 18 | `DIFF_CELL_COUNT_EVT` | INTEGER |  | Stores the number of cells to count before which an action will be triggered. This value is used when a manual cell count is being performed such as a CBC Differential. |
| 19 | `MAIN_RPTD_YN` | VARCHAR |  | Setting for a hematology test to determine if the main part of the test is loaded and reported out. |
| 20 | `CAT_INI` | VARCHAR |  | Stores the master file from which to select a category list for multiline component level category comments. |
| 21 | `CAT_ITEM` | NUMERIC |  | Stores the item from which to select a category list for multiline component level category comments. |
| 22 | `TEST_LINE` | INTEGER |  | The test line number for the information associated with the specimen of this result. Along with RES_SPECIMEN_ID, this forms the foreign key to the SPEC_TEST_REL table. |
| 23 | `DIFF_TYPE_RPTD_C_NAME` | VARCHAR |  | The type of differential reported category number for the result. Note: this item is used for CBC test only. Since this item is set only during result transmittal, it is not set for Quality Control (QC) results. Lastly, only the main result will have this item set. |
| 24 | `COSIGN_MAJOR_EDT_YN` | VARCHAR |  | Indicates if a cosigned version of the result has been modified with a major edit. |
| 25 | `LINKED_CBC_TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 26 | `RAND_REFX_FIRED_YN` | VARCHAR |  | Tracks if the random rescreen reflex extension was fired for this result |
| 27 | `REQ_COSIGNER_USER_ID` | VARCHAR |  | Stores the unique ID of the user record requested to cosign this result. If blank, any user can cosign this result. |
| 28 | `REQ_COSIGNER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `VALIDATION_DATE` | DATETIME |  | The date when the result was validated. |
| 30 | `SPEC_TYPE_CONTAINER_TYPE_ID` | VARCHAR |  | The unique ID for the container type of the specimen for this result. |
| 31 | `SPEC_TYPE_CONTAINER_TYPE_ID_CONTAINER_TYPE_NAME` | VARCHAR |  | The name of the container type record. |
| 32 | `VAR_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the variant associated with this result was added, updated, or deleted. |
| 33 | `TEST_INSTRUMENT_PROF_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the test's resulting method at the time of resulting or verification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RES_EPT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `RES_RQG_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

