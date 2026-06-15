# IP_LDA_NOADDSINGLE

> This table stores LDA information for a patient. A record is created in LDA for insertion of every line, drain, airway, or wound for a patient, as well as entering a trip into a patient's travel history. The no-add information for this LDA is stored in the table.

**Primary key:** `IP_LDA_ID`  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | The internal ID of the Lines/Drains/Airways (LDA) record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | This item stores the ID of the patient to which this line record was added. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the contact serial number of the encounter in which the record was created. |
| 4 | `FLO_MEAS_ID` | VARCHAR | FK→ | This item stores the Flowsheet ID that defines the structure of this record. It is the flowsheet group that is used to define the set of rows for the Line/Drain/Airway (LDA). |
| 5 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 6 | `REMOVAL_INSTANT` | DATETIME (Local) |  | This item stores the instant at which the line/drain was removed. If the line or drain has not been removed, it will store 11/19/2157 17:46:39 as the end instant. |
| 7 | `PLACEMENT_INSTANT` | DATETIME (Local) |  | This item stores the placement instant of the record. |
| 8 | `FSD_ID` | VARCHAR | FK→ | This item stores the flowsheet data (FSD) ID of the record that has information about the properties of the line/drain/airway (LDA). |
| 9 | `DESCRIPTION` | VARCHAR |  | This item stores the name/description of the line/drain. |
| 10 | `PROPERTIES_DISPLAY` | VARCHAR |  | Stores the properties display string to be displayed in Doc Flowsheets and Reports. |
| 11 | `SITE` | VARCHAR |  | This item stores site information for the inserted Line/Drain/Airway. |
| 12 | `LDA_GROUP_CDR` | FLOAT |  | This column stores the contact date real of the Line/Drain/Airway (LDA) Group contact that created this LDA. This column is stored in Epic's datetime (DTE) format. |
| 13 | `LINKED_SUPPLY_ID` | VARCHAR |  | The unique ID of the supply record that is associated with this Line/Drain/Airway. |
| 14 | `LINKED_SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 15 | `REMOVAL_DTTM` | DATETIME (Local) |  | This item stores the date and time at which the line/drain was removed. Unlike REMOVAL_INSTANT, if the line or drain has not been removed, it will store null. |
| 16 | `TRIP_REGION_ID` | NUMERIC |  | Represents where the patient traveled for this trip |
| 17 | `TRIP_REGION_ID_GEO_REGION_NAME` | VARCHAR |  | The record name for the geographical region record. |
| 18 | `TRIP_BEGIN_DATE` | DATETIME |  | Represents when a patient began their trip |
| 19 | `TRIP_END_DATE` | DATETIME |  | Represents the end of this patient trip |
| 20 | `TRIP_DATE_APPROX_C_NAME` | VARCHAR |  | Whether the dates for this trip are exact or approximate |
| 21 | `TRIP_PAT_ENTERED_YN` | VARCHAR |  | Whether some of the details of this trip were provided by patient directly |
| 22 | `AVATAR_PROPERTY_OVERRIDE_YN` | VARCHAR |  | Specifies whether the current region for the LDA was determined by a user override and may not have been calculated from the property values. |
| 23 | `AVATAR_RECORD_ID` | NUMERIC |  | The unique ID of the Anatomy record associated with the region in which this Line/Drain/Airway (LDA) is located on the LDA Avatar activity. |
| 24 | `AVATAR_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 25 | `AVATAR_CALCULATED_RECORD_ID` | NUMERIC |  | Used to store the current region (VEL) record calculated from the Lines/Drains/Airways (LDA) properties and the Avatar LDA Mapping Configuration. |
| 26 | `AVATAR_CALCULATED_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 27 | `RECORDED_DTTM` | DATETIME (Local) |  | The recorded time used in IP_FLWSHT_MEAS for storing the property data for this LDA. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

