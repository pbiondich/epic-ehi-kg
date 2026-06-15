# SPEC_TEST_REL

> The SPEC_TEST_REL table contains information stored on each specimen record that relates to the tests performed on the specimen. Each test appears as a distinct row in this table.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 54  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_TEST_PRI_C_NAME` | VARCHAR | org | The test priority category number for the specimen. |
| 4 | `SPEC_TST_ORDER_ID` | NUMERIC |  | The unique identifier of the order that is associated with this specimen |
| 5 | `SPEC_TST_CANC_C_NAME` | VARCHAR | org | The reason for cancelation category number for a canceled specimen. |
| 6 | `SPEC_TST_CANC_INST` | DATETIME (Local) |  | The instant when a test on the specimen was cancelled. |
| 7 | `SPEC_TST_ACC_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 8 | `TEST_DEST_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 9 | `REDRAWN_ORDERS_ID` | NUMERIC |  | Stores an order after a test has been marked as canceled but the order should be redrawn. |
| 10 | `ORD_PERF_LINE` | INTEGER |  | Stores the line number of the performable procedure linked to this test in the order record's superitem 51300. |
| 11 | `TIERED_TAT` | INTEGER |  | The amount of time, in minutes, from when a specimen is received that can pass before its tests are considered overdue. |
| 12 | `NOT_REPORT_FLAG_C_NAME` | VARCHAR |  | The not reported flag category number for this test. 1-Yes (or 2-Tmp) indicates that this test is not reported (temporarily) to the submitter. 0-No indicates that this test is reported to the submitter. |
| 13 | `LAST_RECV_UTC_DTTM` | DATETIME (UTC) |  | The date and time this test was last received into the lab in UTC. This is used to calculate turnaround times if you have configured them to be based on the last receive instant. |
| 14 | `LAB_CHG_TRG_FLG` | INTEGER |  | Bit flag to track charge triggering. The flag tracks whether different types of charges, such as primary charges and additional billing charges, have been triggered. |
| 15 | `CHG_TRG_LVL_C_NAME` | VARCHAR |  | Primary charge trigger level of the test. It is used to evaluate if void & repost should be performed when the test's billing information is updated. |
| 16 | `SPEC_TST_SEC_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 17 | `TEST_VAL_STATUS_C_NAME` | VARCHAR |  | The validation status of the test. In the case of multiple tests on a specimen, this column will store the validation status of each test in the corresponding row. There are two other columns in the SPEC_TEST_REL table that store the user ID and instant associated with the status that is stored in this column. Those columns are TEST_STATUS_PERSON and TEST_STATUS_DTTM. |
| 18 | `TEST_STATUS_PERSON` | VARCHAR |  | The unique ID of the user associated with the validation status of the test. In the case of multiple tests on a specimen, this column will store the validation status of each test in the corresponding row. There are two other columns in the SPEC_TEST_REL table that store the status and instant associated with the user ID that is stored in this column. Those columns are TEST_VAL_STATUS_C and TEST_STATUS_DTTM. |
| 19 | `TEST_STATUS_PERSON_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `TEST_STATUS_DTTM` | DATETIME (Local) |  | The instant associated with the validation status of the test. In the case of multiple tests on a specimen, this column will store the validation status of each test in the corresponding row. There are two other columns in the SPEC_TEST_REL table that store the status and user ID associated with the instant that is stored in this column. Those columns are TEST_VAL_STATUS_C and TEST_STATUS_PERSON. |
| 21 | `TST_CANCEL_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the test was canceled or redrawn. |
| 22 | `TEST_VER_UTC_DTTM` | DATETIME (UTC) |  | Stores the verification instant of the test in the UTC format. The item is set/updated when the test is either prelim verified or final verified and is cleared when a result correction is done. |
| 23 | `ORDERED_UTC_DTTM` | DATETIME (UTC) |  | This stores the date the test was associated with the specimen in UTC. |
| 24 | `ORDER_INST_DTTM` | DATETIME (Local) |  | The instant the order associated with this test was placed or released. If this test is associated with the performable procedure of a panel, the instant is returned from the orderable procedure. |
| 25 | `ORDER_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant the order associated with this test was placed or released in UTC. If this test is associated with the performable procedure of a panel, the instant is returned from the orderable procedure. |
| 26 | `MISSING_REQ_DATA_C_NAME` | VARCHAR |  | Indicates if any missing required result data was detected for this test at resulting. |
| 27 | `REPORTABLE_YN` | VARCHAR |  | Indicates if this test includes any component or isolate that is flagged as reportable. |
| 28 | `LEVEL_INTERACTION_C_NAME` | VARCHAR |  | Indicates the level of automated or manual interaction during the resulting process. |
| 29 | `AUTO_VERIFIED_YN` | VARCHAR |  | Indicates if this test was ever auto-verified. |
| 30 | `DELTA_YN` | VARCHAR |  | Indicates if this test includes a component flagged as a delta. |
| 31 | `INSTRUMENT_ERROR_YN` | VARCHAR |  | Indicates if this test includes any component or isolate that is flagged with an instrument error. |
| 32 | `TEST_RESULT_TYPE_ID` | VARCHAR |  | The unique identifier of the result type that is assigned to this test. |
| 33 | `TEST_RESULT_TYPE_ID_RESULT_TYPE_NAME` | VARCHAR |  | This is the name of the Result Type record - item OVG .2. |
| 34 | `CHARGE_ID` | VARCHAR |  | The unique ID of the charge associated with the test. |
| 35 | `TST_STAT_ABNORMS_C_NAME` | VARCHAR | org | The category number for the overall test abnormality. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 36 | `GEN_WORKCARD_RESULT_TYPE_ID` | VARCHAR |  | The unique ID of the workcard result type which is associated with the test. |
| 37 | `GEN_WORKCARD_RESULT_TYPE_ID_RESULT_TYPE_NAME` | VARCHAR |  | This is the name of the Result Type record - item OVG .2. |
| 38 | `LNK_SPEC_TST_TOGETHER_YN` | VARCHAR |  | May only be populated in legacy records. Indicates whether linked specimens are tested together with this test. 'Y' indicates that a linked specimen should be tested with this test. 'N' or NULL indicate that linked specimens are not tested with this test. |
| 39 | `CHRG_METHOD_ID` | VARCHAR | FK→ | The unique ID associated with the previous charge method used for this test. |
| 40 | `CHRG_METHOD_ID_CHRG_METHOD_NAME` | VARCHAR |  | The name of the charge trigger method. |
| 41 | `CHG_UPD_FLAG` | INTEGER |  | May only be populated for legacy records. A value in this column means the charges associated with the test require updating. |
| 42 | `EXTRA_RESULT_CNT` | INTEGER |  | The number of extra results remaining. |
| 43 | `RESULT_CNT` | INTEGER |  | The number of results needing to be performed for this test. |
| 44 | `BATCH_QUEUE_IDENT` | VARCHAR |  | The position of this test in the batch queue. |
| 45 | `VALIDATED_RESULT_ID` | VARCHAR |  | The unique ID of the finalized result for the test. |
| 46 | `REPEAT_CNT` | INTEGER |  | The number of repeats required for this test. |
| 47 | `DEL_FROM_BATCH_QUEUE` | VARCHAR |  | May only be populated for legacy records. When a value is present in this column, this test was removed from the Batch Queue. |
| 48 | `ORDER_PRIORITY_C_NAME` | VARCHAR | org discont. | The order priority categroy ID for the test. |
| 49 | `SHIPPING_NUMBER` | INTEGER |  | Represents a unique ID associated with transferring this test to another lab. |
| 50 | `PREV_RSLT_DISP_FLAG_C_NAME` | VARCHAR |  | May only be populated for legacy records. The previous result display method category ID for the test. |
| 51 | `RR_EXCEPT_LIST` | VARCHAR |  | May only be populated for legacy records. Contains flags for not reporting or sending result reports for this test to specific recipients. |
| 52 | `CANCEL_RESULT_ID` | VARCHAR |  | The unique ID of a canceled result, if one exists, for each test on the specimen. |
| 53 | `REFLEX_TRIGGERED_YN` | VARCHAR |  | Indicates whether reflex testing has executed on the result for each test on the specimen. 'Y' indicates that reflex testing has executed. 'N' or NULL indicate that reflex testing has not executed. |
| 54 | `SOURCE_ORDER_ID` | NUMERIC |  | The unique ID of the source order for the test. For tests that have been redrawn or moved, this is the removed order. For tests that have not be redrawn or removed, this is the order that results will file to. This is the culture order for susceptibility tests. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CHRG_METHOD_ID` | [CHRG_TRIG_MTHD](CHRG_TRIG_MTHD.md) | sole_pk | high |

