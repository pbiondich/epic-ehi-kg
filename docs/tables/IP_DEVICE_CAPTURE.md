# IP_DEVICE_CAPTURE

> This table contains device capture information for the given Inpatient Data (INP) record.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INST_START_DTTM` | DATETIME (Local) |  | This column displays the start instant of capture for the associated device. |
| 4 | `DEVICE_ID` | VARCHAR | FK→ | This column displays the unique ID of the associated device record. |
| 5 | `DEVICE_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 6 | `SELECT_VAR_IDS` | VARCHAR |  | This column displays the ID of the associated variable record. |
| 7 | `ATTACH_INSTANT_DTTM` | DATETIME (Local) |  | This column displays the instant at which the associated device record was attached to the patient for the given encounter. |
| 8 | `REMOVE_INSTANT_DTTM` | DATETIME (Local) |  | This column displays the instant at which the associated device record was removed from the patient for the given encounter. |
| 9 | `INSTANT_TO_VAL_DTTM` | DATETIME (Local) |  | This column displays the instant at which the associated device was validated. |
| 10 | `VALIDATED_USER_ID` | VARCHAR |  | This column displays the users who validated the associated device. |
| 11 | `VALIDATED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `LINKED_ORD_ID` | NUMERIC |  | This column displays the order ID that is linked with the device |
| 13 | `SECONDARY_ORD_ID` | NUMERIC |  | This column displays the secondary order id when second order is linked to the device |
| 14 | `LINE_NUMBER` | INTEGER |  | This column stores the audit trail line number for edited device data. |
| 15 | `FLO_TEMPLATE_ID` | VARCHAR |  | This column displays the flowsheet template that will be updated when device data is filed in the flowsheet. |
| 16 | `FLO_TEMPLATE_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 17 | `DRCT_CPTR_INTERVAL` | INTEGER |  | Interval for direct capture of Anesthesia device data, in minutes |
| 18 | `AUTOFILE_EFF_UTC_DTTM` | DATETIME (UTC) |  | The instant at which Auto Filing for this device association was enabled or disabled (as described in I INP 9160). |
| 19 | `AUTO_FILE_C_NAME` | VARCHAR |  | Stores whether device data is auto filed for this device association |
| 20 | `AUTOFILE_INTERVAL` | INTEGER |  | This item determines the filing interval for this device association when using Inpatient automatic filing. This item overrides the Device Type, Department, and/or System level interval values. |
| 21 | `AUTOFILE_ERR_C_NAME` | VARCHAR |  | Stores whether the auto filing process has encountered an error and data cannot be filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DEVICE_ID` | [DEVICE_INFO](DEVICE_INFO.md) | sole_pk | high |

