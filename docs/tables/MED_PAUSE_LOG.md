# MED_PAUSE_LOG

> This table holds a log of all changes made to the medication reminders pause anchor event items for the patient's encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the UTC instant value of when an action was performed. |
| 7 | `ACTION_C_NAME` | VARCHAR |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the action that was performed. |
| 8 | `EVENT_TYPE_C_NAME` | VARCHAR |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the type of event. |
| 9 | `EVENT_UTC_DTTM` | DATETIME (UTC) |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the UTC instant value of when the event was scheduled. |
| 10 | `PAUSE_UTC_DTTM` | DATETIME (UTC) |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the UTC instant value for when all medication reminders have been paused. |
| 11 | `RESUME_UTC_DTTM` | DATETIME (UTC) |  | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds the UTC instant value for when all medication reminders have been resumed. |
| 12 | `LPP_ID` | NUMERIC | FK→ | This item is part of a related group of items that logs all actions conducted on the medication pause anchor events items. This item holds a reference to the anchor event extension used to identify this encounter. |
| 13 | `LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LPP_ID` | [CLARITY_LPP](CLARITY_LPP.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

