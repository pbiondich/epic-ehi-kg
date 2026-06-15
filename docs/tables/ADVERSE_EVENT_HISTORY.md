# ADVERSE_EVENT_HISTORY

> The ADVERSE_EVENT_HISTORY table contains the history of adverse event records for a patient.

**Primary key:** `ADVERSE_EVENT_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the adverse event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | The date and time when this update to the adverse event was made. |
| 4 | `EDIT_USER_ID` | VARCHAR |  | The unique ID of the user who made this update to the adverse event. |
| 5 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_NOTE_CSN` | NUMERIC |  | The unique contact serial number of the note containing the comments for this update of the adverse event record. |
| 7 | `HX_RESEARCH_ATTRIBUTION_C_NAME` | VARCHAR | org | The category ID of the study attribution level for the adverse event at the time the adverse event was documented. |
| 8 | `HX_SERIOUS_YN` | VARCHAR |  | Indicates whether or not this adverse event was considered serious at the time the adverse event was documented. |
| 9 | `HX_EXPECTED_YN` | VARCHAR |  | Indicates whether or not this adverse event was considered expected at the time the adverse event was documented. |
| 10 | `HX_RESOLVED_DATE` | DATETIME |  | The date the adverse event was resolved at the time the adverse event was documented. |
| 11 | `HX_AE_STATUS_C_NAME` | VARCHAR |  | The category ID of the status of this adverse event at the time of this update. |
| 12 | `HX_RESEARCH_ATTR_NOT_COLL_YN` | VARCHAR |  | Indicates whether the attribution for the associated research study was collected for this adverse event at the time of the update. 'Y' indicates that an attribution was not collected. 'N' or NULL indicate that an attribution was collected. |
| 13 | `HX_CLINICALLY_SIGNIFICANT_YN` | VARCHAR |  | Indicates whether or not this adverse event was considered clinically significant at the time the adverse event was documented. |
| 14 | `HX_BASELINE_YN` | VARCHAR |  | Indicates whether or not this adverse event was considered baseline at the time the adverse event was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADVERSE_EVENT_ID` | [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | sole_pk | high |

