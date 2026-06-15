# LENGTH_OF_STAY

> The LENGTH_OF_STAY table contains information about the duration of the inpatient stay for a hospital encounter. It contains information for only discharged hospital encounters. Hospital encounters which have a currently admitted status are not included because their length of stay information changes every minute and will therefore not be up to date.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LENGTH_OF_STAY_DAYS` | INTEGER |  | This column holds the length of stay for the hospital encounter measured in midnights. The length of stay is the total number of midnights or a same-day discharge a patient had as a patient base class of inpatient. This includes all leaves of absence while the patient was an inpatient. |
| 5 | `LENGTH_OF_STAY_MINS` | INTEGER |  | This column holds the length of stay for the hospital encounter measured in minutes. The length of stay is the total time a patient had a patient base class of inpatient. This includes all leaves of absence while the patient was an inpatient. |
| 6 | `INPATIENT_DAYS` | INTEGER |  | This column holds the patient days for the hospital encounter. Patient days include same-day discharges, census events, and days on leave of absence with a patient base class of inpatient. Only leaves of absence with a leave of absence reason configured to count towards total patient days are included. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

