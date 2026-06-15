# ISOLATIONS

> This table contains patient isolation data.

**Primary key:** `ISOLATION_ID`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ISOLATION_ID` | NUMERIC | PK | The unique identifier for the isolation record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The record status category ID for the isolation. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the contact in which this isolation took place. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `ISOLATION_C_NAME` | VARCHAR | org | The isolation type category ID for the isolation. |
| 6 | `ISOLATION_STATUS_C_NAME` | VARCHAR |  | The isolation status category ID for the isolation. |
| 7 | `HOW_ISO_ADDED_C_NAME` | VARCHAR |  | The How Isolation Was Added category ID for the isolation. |
| 8 | `ISOLATION_ORDER_ID` | NUMERIC |  | The unique identifier of the order that added the isolation. |
| 9 | `ADDED_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the isolation was added. |
| 10 | `ADDED_USER_ID` | VARCHAR |  | The unique ID associated with the user record for the user who added this isolation. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `ADDED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `REMOVED_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the isolation was removed. |
| 13 | `REMOVED_USER_ID` | VARCHAR |  | The unique ID associated with the user record for the user who removed this isolation. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `REMOVED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `COMMENTS` | VARCHAR |  | The user-entered comments associated with the isolation |
| 16 | `RECORD_CREATION_DATE` | DATETIME |  | The date when the isolation record was created. |
| 17 | `ADDED_LOCAL_DTTM` | DATETIME (Attached) |  | Local instant when isolation was added. |
| 18 | `REMOVED_LOCAL_DTTM` | DATETIME (Attached) |  | Local instant when isolation was removed. |
| 19 | `INFECTION_LINKS_CALCULATED_YN` | VARCHAR |  | Indicates whether all linked infections have been calculated. 'Y' indicates all linked infections have been calculated. 'N' or NULL indicates that there may be infections that would be considered linked to the isolation, but that the isolation pre-dates the linking calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

