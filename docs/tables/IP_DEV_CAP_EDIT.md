# IP_DEV_CAP_EDIT

> This table displays device capture information.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INST_START_EDIT_TM` | DATETIME (Local) |  | This column stores the old start time value from before the device start time was edited. |
| 4 | `INTERVAL_EDITED` | INTEGER |  | This item is used to store edited interval information. |
| 5 | `DEVICE_ID_EDITED` | VARCHAR |  | This item is used to store device id for edited line. |
| 6 | `DEVICE_ID_EDITED_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 7 | `SEL_VAR_IDS_EDITED` | VARCHAR |  | This item is used to store edited selected variables information. |
| 8 | `REMOVE_INST_EDIT_TM` | DATETIME (Local) |  | This item stores the edited stop instant for a device. |
| 9 | `RCRD_INST_EDIT_TM` | DATETIME (Local) |  | This item is used to store recorded instant for the event. |
| 10 | `REC_USER_ID_EDIT` | VARCHAR |  | This item is used to store recorded user ID (edited data). |
| 11 | `REC_USER_ID_EDIT_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `LINKED_ORD_EDIT_ID` | NUMERIC |  | The ID of the order associated with the edited device data. |
| 13 | `EDIT_SEC_ORD_ID` | NUMERIC |  | Stores the secondary order id when second order is linked to the device (edited data). |
| 14 | `LINE_NUMBER_EDITED` | INTEGER |  | This item is used as a pointer to audit trail line. (edited data). |
| 15 | `EDIT_FLO_TEMPLAT_ID` | VARCHAR |  | This item is used for saving audit trail information for flowsheet template. |
| 16 | `EDIT_FLO_TEMPLAT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 17 | `DRCT_CPTR_INTER_ED` | INTEGER |  | Audit trail for Anesthesia direct capture interval, in minutes |
| 18 | `AUTOFILE_EFF_ED_UTC_DTTM` | DATETIME (UTC) |  | The instant at which Auto Filing for this device association was enabled or disabled (as described in I INP 9360). |
| 19 | `AUTO_FILE_ED_C_NAME` | VARCHAR |  | Stores whether device data is auto filed for old association |
| 20 | `AUTOFILE_INTERVAL_EDIT` | INTEGER |  | This item determined the filing interval for this device association as described in I INP 9162. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

