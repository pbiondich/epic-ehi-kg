# SPEC_TASK_LIST

> This table contains task information for Microbiology specimens and Anatomic Pathology cases.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 31  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TASK_TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 4 | `TASK_C_NAME` | VARCHAR | org | The task category number for the specimen |
| 5 | `TASK_ACTION_C_NAME` | VARCHAR |  | The task action category number for the corresponding task. |
| 6 | `TASK_PARAMS` | VARCHAR |  | Stores the parameters for the action associated with task on the corresponding line. For instance, this column may store the media type of the created container. |
| 7 | `TASK_INSTANT` | DATETIME (Local) |  | The instant when the task was completed. |
| 8 | `TASK_PERSON_ID` | VARCHAR |  | The unique employee identifier of the person completing the task. |
| 9 | `TASK_PERSON_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `TASK_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 11 | `TASK_INST` | DATETIME (Local) |  | The user-editable instant when the task was completed. |
| 12 | `TASK_LINKED_CTNR_ID` | VARCHAR |  | The unique container identifier that might be created if the action associated with the task on the corresponding line is to create a media plate, a block or a slide that is related to a block. |
| 13 | `TASK_GROUP` | VARCHAR |  | This item is used to group tasks together. This feature is most commonly used to link multiple slides to a block. |
| 14 | `TASK_ACTION_QTY` | INTEGER |  | Stores the number of times the action associated with this task must be performed. |
| 15 | `TASK_CHARGE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 16 | `TASK_CHARGE_QTY` | INTEGER |  | Stores the number of times the billing code associated with this task must be charged. |
| 17 | `TASK_INT_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 18 | `TASK_LEVEL` | INTEGER |  | Stores number of levels. |
| 19 | `TASK_BLOCK_START_TM` | DATETIME (Local) |  | Stores the block fixation start time. |
| 20 | `TASK_BLOCK_END_TM` | DATETIME (Local) |  | Stores the block fixation end time. |
| 21 | `TASK_NOTES` | VARCHAR |  | Stores any free text notes describing the task. |
| 22 | `TASK_DELETED_YN` | VARCHAR |  | Indicates whether the related task has been soft-deleted. "Y" indicates that the task has been soft-deleted. "N" or an empty value indicates that the task has not been soft-deleted. |
| 23 | `TASK_AP_PART_ID` | VARCHAR |  | Returns the part ID for this anatomic pathology task, such as "A1". |
| 24 | `TASK_PROTOCOL_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 25 | `TASK_COMP_UTC_DTTM` | DATETIME (UTC) |  | The instant that the user indicated the task was completed in UTC. |
| 26 | `TASK_CHG_TR_STAT_C_NAME` | VARCHAR |  | The charge trigger status category ID for the task. |
| 27 | `TASK_UPD_LINE` | INTEGER |  | The line in the tasks related table (SI 51310) that the current line is created to restore for when task was updated. |
| 28 | `TASK_UPD_ALERT_ID` | NUMERIC |  | The unique alert record identifier created when the task was updated. |
| 29 | `TEST_LINE` | INTEGER |  | The line number of the associated test on the specimen. Together with SPECIMEN_ID, this forms the foreign key to the SPEC_TEST_REL table. |
| 30 | `CHARGE_SS_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 31 | `CHARGE_QTY_SS` | INTEGER |  | The quantity for the last dropped charge for the associated specimen task. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

