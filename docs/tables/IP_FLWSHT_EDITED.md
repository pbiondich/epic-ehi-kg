# IP_FLWSHT_EDITED

> This table contains the previous values from edited flowsheet records.

**Primary key:** `FSD_ID`, `LINE`  
**Columns:** 39  
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
| 6 | `LINE_NUM` | INTEGER |  | The line number of the reading that replaced this flowsheet reading. |
| 7 | `RECORDED_TIME` | DATETIME (Local) |  | The instant the reading was taken. |
| 8 | `ENTRY_TIME` | DATETIME (Local) |  | The instant the reading was entered. |
| 9 | `TAKEN_USER_ID` | VARCHAR |  | The unique ID of the user taking the flowsheet readings. |
| 10 | `TAKEN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user entering the readings. |
| 12 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `EDIT_COMMENT` | VARCHAR |  | The free text comments associated with the reading. |
| 14 | `EDITED_LINE` | INTEGER |  | Determines if this flowsheet record has been edited. |
| 15 | `ACCEPTED_YN` | VARCHAR |  | Determines if this flowsheet record has been accepted. |
| 16 | `IP_SIGNIFCNT_EDI_YN` | VARCHAR |  | Stores edited information on whether the user marked the data value as being significant. |
| 17 | `EDITED_DEV_ID` | VARCHAR |  | This item stores information of the Device ID for the device from which data is captured from when the data is edited. |
| 18 | `EDITED_DEV_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 19 | `EDITED_RECEIVE_INST` | DATETIME (Local) |  | This item stores the Instant at which value was received at the interface when the data is edited. |
| 20 | `AUDIT_NEED_COSIG_YN` | VARCHAR |  | Indicates whether a value needing a co-sign is stored for the audit record for the flowsheet data record. Yes indicates that a value needing a co-sign gets over-written with a value not needing a co-sign. |
| 21 | `EDITED_FLT_ID` | VARCHAR |  | The unique ID of the flowsheet template (FLT) which was used to enter this data into the cell. |
| 22 | `EDITED_FLT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 23 | `EDT_FLO_DAT_USED` | NUMERIC |  | If the contact date (DAT) used to define data for a flowsheet group or row (see column FLO_DAT_USED) is changed, this column stores the prior value. |
| 24 | `EDITED_PENDED_ID` | VARCHAR |  | History of the user ID of the user who pended a flowsheet value. |
| 25 | `EDITED_PENDED_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `EDITED_INSTANT_DTTM` | DATETIME (Local) |  | History of date/time at which a flowsheet value was pended. |
| 27 | `AUDIT_ABNORMAL_C_NAME` | VARCHAR |  | Stores whether or not the edited value is abnormal |
| 28 | `FLO_CNCT_DATE_REAL` | NUMERIC |  | This column converts the contact date (DAT) of the flowsheet group or row to DTE, based on the value in column FLO_DAT_USED. |
| 29 | `EDITD_3P_SRC_C_NAME` | VARCHAR | org | History of identification of the third-party framework that a Flowsheets value originally came from, if applicable. Intended to be used to track values that are sourced from health/fitness frameworks (e.g. Apple's HealthKit) to provide additional context when examining attached metadata. |
| 30 | `PAT_REPORTED_STATUS_C_NAME` | VARCHAR | org | Indicates if the edited data was directly entered by the patient or a patient proxy and whether the data has been validated by a clinician |
| 31 | `MYPT_ID` | VARCHAR | shared | The MyChart account from which the edited data was entered. |
| 32 | `EDIT_IS_FROM_SPEECH_YN` | VARCHAR |  | Indicates whether an edited flowsheet value was entered using speech entry. |
| 33 | `EDITED_ABNORMAL_TYPE_C_NAME` | VARCHAR |  | This column stores metadata for abnormal flowsheet values. Edited Abnormal Type is only populated for data where AUDIT_ABNORMAL_C is set to 1-Yes. It is set to 1-Low for data that is below the minimum warning level and it is set to 2-High for data that is above the maximum warning level for flowsheet data of types: numeric, blood pressure, temperature, height, patient height, weight and patient weight. It is set to 0-Unspecified for data that is abnormal for other reasons. This is the only value that can be set for flowsheet data of type: custom list. |
| 34 | `EDIT_FLO_NET_INI` | VARCHAR |  | The INI to which the value for this row is associated. |
| 35 | `EDIT_DOC_METHOD_C_NAME` | VARCHAR |  | Indicates the method the user used to enter the line of flowsheet data. |
| 36 | `EDITED_MACRO_RECORD_ID` | NUMERIC |  | When the documentation method in FSD-2360 is 1-Value From Macro this is the macro HGM record ID. |
| 37 | `EDITED_MACRO_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |
| 38 | `DOCUMENTING_INPATIENT_DATA_ID` | VARCHAR |  | Stores the INP ID of the encounter where the property documentation occurred. This item will not be populated for non-property rows, or for any property values documented prior to the existence of this item. |
| 39 | `EDIT_SPEECH_ENTERED_METHOD_C_NAME` | VARCHAR | org | Indicates whether an edited flowsheet value was entered using speech entry. A value of 1 ("Y") indicates that the value was entered using speech entry. A value of 0 ("N") or (null) indicates that the value was entered using manual entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

