# OR_LNLG_GENERAL

> This table contains the general information about the surgical log line (ORM) record. This table also contains the information that can apply to several different types of surgical log line records.

**Primary key:** `RECORD_ID`  
**Columns:** 28  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID associated with the line record for this row. |
| 2 | `RECORD_NAME` | VARCHAR |  | The name of the line record. |
| 3 | `RECORD_STATE_C_NAME` | VARCHAR |  | The status category number for the line record. A null status means that the record is active. |
| 4 | `PREALL_REC_TYPE_C_NAME` | VARCHAR |  | The pre-allocated record type category number for the line record. |
| 5 | `PREALLOCATED_LOG_ID` | VARCHAR |  | The surgical log to which this record has been pre-allocated. If record is in use or was pre-allocated by the pre-allocation process, this item will not be populated. |
| 6 | `ORM_REC_TYPE_C_NAME` | VARCHAR | org | The surgical log data type category number for the line record. For example, the types of data stored in line records include delays, staff, and equipment. |
| 7 | `MARKED_FOR_DEL_YN` | VARCHAR |  | Indicates whether the line record has been marked for deletion. Y indicates the record has been marked for deletion. A null value indicates that the record has not been marked for deletion. An N will not be populated for this column. |
| 8 | `LOG_ID` | VARCHAR | shared | ID of the log to which this ORM record belongs. |
| 9 | `PRESERVE_RECORD_YN` | VARCHAR |  | Determines whether the ORM resource needs to be preserved during rebuild since it has been documented in the log. |
| 10 | `MAN_ENTERED_TM_SEC` | NUMERIC |  | The manually entered total time that a resource was used in seconds. |
| 11 | `LOANED_EQUIP_YN` | VARCHAR |  | Indicates if a particular piece of equipment is loaned or rented. Y indicates that the piece of equipment is loaned or rented. N indicates that the piece of equipment is not loaned or rented. A null value indicates that the line record is not any type of equipment or the value is not populated. |
| 12 | `LOANED_EQUIP_ID` | VARCHAR |  | The ID of the loaned or rented piece of equipment that does not have a provider record in Epic. |
| 13 | `EQUIP_POSITION_DTTM` | DATETIME (Local) |  | The date and time a piece of equipment was positioned for use in a procedure. |
| 14 | `EQUIP_PRESSURE` | NUMERIC |  | General item for storing the recorded equipment pressure, e.g. as measured on a CO2 Insufflator. |
| 15 | `CASE_ID` | VARCHAR | shared | The unique ID of the case whose log will contain this line of documentation. |
| 16 | `CREATED_EXTERNAL_YN` | VARCHAR |  | Indicates whether this line of log documentation was created in an external system. |
| 17 | `PREP_AREA_MOD_C_NAME` | VARCHAR | org | This column displays the modifier for the prep area to allow a more discrete documentation of laterality. |
| 18 | `DEVICE_TEST_DTTM` | DATETIME (UTC) |  | Item to document time at which device was tested. |
| 19 | `TTL_DISSIPATD_ENRGY` | NUMERIC |  | The cumulative dissipated energy used by the equipment. |
| 20 | `EQUIP_FLOW_RATE` | NUMERIC |  | The flow rate for the equipment. |
| 21 | `EQUIP_TOTAL_ENERGY` | NUMERIC |  | The total energy used by the equipment. |
| 22 | `MAN_ENTERED_TM_MIN` | INTEGER |  | The total length of time the tourniquet was inflated (in minutes). |
| 23 | `DEFIB_NUM_APPLIED` | INTEGER |  | Stores the number of times the defibrillator was used on the patient. |
| 24 | `EQUIP_MEASURED_LEN` | NUMERIC |  | This item stores the length measured by a piece of equipment. |
| 25 | `FREQUENCY` | INTEGER |  | This column stores the equipment frequency. |
| 26 | `STAFF_NOTIFIED_DTTM` | DATETIME (UTC) |  | This item stores the time that staff were notified. |
| 27 | `BACKGROUND_READING` | NUMERIC |  | Reading of the background radiation |
| 28 | `FREQUENCY_AVERAGE` | NUMERIC |  | This item is to document the frequency average. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

