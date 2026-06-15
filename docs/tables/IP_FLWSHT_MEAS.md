# IP_FLWSHT_MEAS

> This table contains the patient-specific measurements from flowsheets.

**Primary key:** `FSD_ID`, `LINE`  
**Columns:** 38  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique ID for the flowsheet data record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `FLO_MEAS_ID` | VARCHAR | FK→ | The unique ID for the flowsheet group/row associated with this reading. |
| 4 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 5 | `OCCURANCE` | INTEGER |  | If the flowsheet group/row appears multiple times, this will distinguish the occurrence. |
| 6 | `RECORDED_TIME` | DATETIME (Local) |  | The instant the reading was taken. |
| 7 | `ENTRY_TIME` | DATETIME (Local) |  | The instant the reading was entered. |
| 8 | `TAKEN_USER_ID` | VARCHAR |  | The unique ID of the user taking the flowsheet readings. |
| 9 | `TAKEN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user entering the readings. |
| 11 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `MEAS_COMMENT` | VARCHAR |  | The free text comments associated with the reading. |
| 13 | `EDITED_LINE` | INTEGER |  | The line number of the previous value of an edited record. |
| 14 | `ISACCEPTED_YN` | VARCHAR |  | Determines if this flowsheet record has been accepted. |
| 15 | `IP_SIGNIFICANT_YN` | VARCHAR |  | This stores whether the flowsheet data is marked as significant. If a value is not marked as significant, this column returns NULL. |
| 16 | `CAPTURE_DEVICE_ID` | VARCHAR |  | This item stores information of the Device ID for the device from which data is captured from. |
| 17 | `CAPTURE_DEVICE_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 18 | `RECEIVED_INSTANT` | DATETIME (Local) |  | Instant at which value was received at the interface |
| 19 | `NEEDS_COSIGN_C_NAME` | VARCHAR |  | If this item is blank or 0 (No), then this flowsheet data does not need a cosign. If this item is 1 (Required Yes), then a cosign is required for this data and can only be pended. If this item is 2 (Chosen Yes), then a cosign has been requested for this data but it is not required. If this item is 3 (Required Yes Can File), then a cosign is required for the data and the data can be filed. |
| 20 | `FLT_ID` | VARCHAR |  | The unique ID of the flowsheet template (FLT) which was used to enter the data in this cell. |
| 21 | `FLT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 22 | `FLO_DAT_USED` | NUMERIC |  | This column stores the contact date (DAT) of the flowsheet row or group that is used to define the data. |
| 23 | `FLO_CNCT_DATE_REAL` | NUMERIC |  | This column converts the contact date (DAT) of the flowsheet group or row to DTE, based on the value in column FLO_DAT_USED. |
| 24 | `USER_PENDED_BY_ID` | VARCHAR |  | User ID of the user who pended this flowsheet value. |
| 25 | `USER_PENDED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `INSTANT_PENDED_DTTM` | DATETIME (Local) |  | Date/time at which a flowsheet value is pended. |
| 27 | `ABNORMAL_C_NAME` | VARCHAR |  | Stores whether or not the value is abnormal |
| 28 | `THRDPRTY_SRC_C_NAME` | VARCHAR | org | Identifies the third-party framework that a Flowsheets value originally came from, if applicable. Intended to be used to track values that are sourced from health/fitness frameworks (e.g. Apple's HealthKit) to provide additional context when examining attached metadata. |
| 29 | `PAT_REPORTED_STATUS_C_NAME` | VARCHAR | org | Indicates if the data was directly entered by the patient or a patient proxy and whether the data has been validated by a clinician |
| 30 | `MYPT_ID` | VARCHAR | shared | The MyChart account from which the data was entered. |
| 31 | `IS_FROM_SPEECH_YN` | VARCHAR |  | Indicates whether a filed flowsheet value was entered using speech entry. |
| 32 | `ABNORMAL_TYPE_C_NAME` | VARCHAR |  | This column stores metadata for abnormal flowsheet values. It is only populated for data where ABNORMAL_C - Abnormal is set to 1-Yes. It is set to 1-Low for data that is below the minimum warning level and it is set to 2-High for data that is above the maximum warning level for flowsheet data of types: numeric, blood pressure, temperature, height, patient height, weight and patient weight. It is set to 0-Unspecified for data that is abnormal for other reasons. This is the only value that can be set for flowsheet data of type: custom list. |
| 33 | `FLO_NETWORKED_INI` | VARCHAR |  | The INI to which the value for this row is associated. |
| 34 | `DOC_METHOD_C_NAME` | VARCHAR |  | Indicates the method the user used to enter the line of flowsheet data. |
| 35 | `MACRO_RECORD_ID` | NUMERIC |  | When the documentation method in FSD-1360 is 1-Value From Macro this is the macro HGM record ID. |
| 36 | `MACRO_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |
| 37 | `DOCUMENTING_INPATIENT_DATA_ID` | VARCHAR |  | Stores the INP ID of the encounter where the property documentation occurred. This item will not be populated for non-property rows, or for any property values documented prior to the existence of this item. |
| 38 | `SPEECH_ENTERED_METHOD_C_NAME` | VARCHAR | org | Indicates what speech-based entry method was used to enter this value. A value of 0 ("N") or (null) indicates that the value was entered using manual entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

