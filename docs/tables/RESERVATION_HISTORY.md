# RESERVATION_HISTORY

> This table contains audit information on changes to admission reservations. Each row represents a change to the related encounter's reservation.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `RES_HX_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 8 | `RES_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `RES_HX_REASON_C_NAME` | VARCHAR |  | The Reason for Change category ID for this row's change to a patient's reservation. |
| 10 | `RES_HX_LINE` | INTEGER |  | The line number for the reservation being changed that is associated with this contact. Multiple changes can be associated with this contact. |
| 11 | `RES_HX_RESRC_TYPE_ID_TANK_NAME` | VARCHAR |  | The name of the tank record. |
| 12 | `RES_HX_RESRC_SUBTYPE_C_NAME` | VARCHAR | org | The category ID for the type of stay associated with this row's change to a patient's reservation. |
| 13 | `RES_HX_START_DATE` | DATETIME |  | The date this reservation started at the instant this row's change took effect on the patient's reservation. |
| 14 | `RES_HX_START_TIME_C_NAME` | VARCHAR | org | The approximate start time category ID that was applicable at the instant of this row's change to a patient's reservation. |
| 15 | `RES_HX_END_DATE` | DATETIME |  | The date this reservation ended at the instant this row's change took effect on the patient's reservation. If this is populated, then RES_HX_INDEF_YN will not be populated for this row. |
| 16 | `RES_HX_END_TIME_C_NAME` | VARCHAR |  | The approximate end time category ID that was applicable at the instant of this row's change to a patient's reservation. If this is populated, then RES_HX_INDEF_YN will not be populated for this row. |
| 17 | `RES_HX_INDEF_YN` | VARCHAR |  | Indicates whether this row's reservation was indefinite at the instant of this change. If Y, then RES_HX_END_DATE and RES_HX_END_TIME_C will not be populated for this row. |
| 18 | `RES_HX_CONFRMD_YN` | VARCHAR |  | Indicates whether this reservation was confirmed at the time of this change. Y indicates that this was scheduled and on the calendar. |
| 19 | `RES_HX_UTC_DTTM` | DATETIME (UTC) |  | The instant when this row's change took effect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

