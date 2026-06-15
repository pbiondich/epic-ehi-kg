# PHYS_PRESENCE_VER

> This table contains a row for each time a user was confirmed to be physically present in a patient's home.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 6 | `METHOD_C_NAME` | VARCHAR |  | The method of physical presence verification |
| 7 | `VERIFICATION_DTTM` | DATETIME (UTC) |  | The instant of verification of physical presence |
| 8 | `PRESENT_USER_ID` | VARCHAR |  | The user who was physically present at the patient's home. |
| 9 | `PRESENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LATITUDE` | NUMERIC |  | This item stores the latitude of the user's mobile device at the time of physical presence verification. |
| 11 | `LONGITUDE` | NUMERIC |  | This item stores the longitude of the user's mobile device at the time of physical presence verification. |
| 12 | `POS_LATITUDE` | VARCHAR |  | The latitude of the location used for electronic visit verification. |
| 13 | `POS_LONGITUDE` | VARCHAR |  | The longitude of the location used for electronic visit verification. |
| 14 | `POS_ADDR` | VARCHAR |  | The address string of the location used for electronic visit verification. |
| 15 | `ACCURACY` | NUMERIC |  | The radius of uncertainty associated with the location coordinate captured at the time of physical presence verification, measured in meters. A higher value means lower accuracy of the retrieved coordinate. |
| 16 | `POS_STREET_ADDRESS` | VARCHAR |  | The street address of the location used for electronic visit verification. |
| 17 | `POS_CITY` | VARCHAR |  | The city of the location used for electronic visit verification. |
| 18 | `POS_STATE_C_NAME` | VARCHAR | org | The state of the location used for electronic visit verification. |
| 19 | `POS_ZIP` | VARCHAR |  | The ZIP code of the location used for electronic visit verification. |
| 20 | `POS_COUNTY_C_NAME` | VARCHAR | org | The county of the location used for electronic visit verification. |
| 21 | `POS_COUNTRY_C_NAME` | VARCHAR | org | The country of the location used for electronic visit verification. |
| 22 | `MANUAL_ENTER_TM_YN` | VARCHAR |  | This column stores if the time log for the physical presence verification event was manually entered by the user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

