# ADVERSE_EVENT_INFO

> The ADVERSE_EVENT_INFO table contains information about adverse event records for a patient.

**Primary key:** `ADVERSE_EVENT_ID`  
**Columns:** 13  
**Org-specific columns:** 1  
**Joined by:** 19 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK | The unique identifier for the adverse event record. |
| 2 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 3 | `RESEARCH_ATTRIBUTION_C_NAME` | VARCHAR | org | The category ID for the attribution level of the associated research study to this adverse event. |
| 4 | `SERIOUS_YN` | VARCHAR |  | Indicates whether or not this adverse event is considered serious. |
| 5 | `EXPECTED_YN` | VARCHAR |  | Indicates whether or not this adverse event is expected. |
| 6 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `STATUS_C_NAME` | VARCHAR |  | The category ID of the status of this adverse event. |
| 8 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note record containing the comments for this adverse event. |
| 9 | `RESOLVED_DATE` | DATETIME |  | The date this adverse event was resolved. |
| 10 | `RESEARCH_ATTR_NOT_COLL_YN` | VARCHAR |  | Indicates whether the attribution for the associated research study was collected for this adverse event. 'Y' indicates that an attribution was not collected. 'N' or NULL indicate that an attribution was collected. |
| 11 | `ENROLL_ID` | NUMERIC | FK→ | The unique ID of the research study association that has been linked to this adverse event. Linking an adverse event to a research study association means the adverse event may be related to or caused by the research study. |
| 12 | `CLINICALLY_SIGNIFICANT_YN` | VARCHAR |  | Indicates whether or not this adverse event is considered clinically significant. |
| 13 | `BASELINE_YN` | VARCHAR |  | Indicates whether or not this adverse event is considered baseline. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

## Joined in — referenced by (19)

| From | Column | Confidence |
|------|--------|------------|
| [ADVERSE_EVENT_ACT_TAKEN](ADVERSE_EVENT_ACT_TAKEN.md) | `ADVERSE_EVENT_ID` | high |
| [ADVERSE_EVENT_GRADE](ADVERSE_EVENT_GRADE.md) | `ADVERSE_EVENT_ID` | high |
| [ADVERSE_EVENT_HISTORY](ADVERSE_EVENT_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADVERSE_EVENT_MED_ATTR](ADVERSE_EVENT_MED_ATTR.md) | `ADVERSE_EVENT_ID` | high |
| [ADVERSE_EVENT_OUTCOMES](ADVERSE_EVENT_OUTCOMES.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_ACTIONS_TAKEN_HX](ADV_EVT_ACTIONS_TAKEN_HX.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_GRADE_HISTORY](ADV_EVT_GRADE_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_GRADE_START_HX](ADV_EVT_GRADE_START_HX.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_MED_ATTR_HISTORY](ADV_EVT_MED_ATTR_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_MED_HISTORY](ADV_EVT_MED_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_OUTCOME_HISTORY](ADV_EVT_OUTCOME_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_PROC_ATTR](ADV_EVT_PROC_ATTR.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_PROC_ATTR_HISTORY](ADV_EVT_PROC_ATTR_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_PROC_HISTORY](ADV_EVT_PROC_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_SUPPLY_ATTR](ADV_EVT_SUPPLY_ATTR.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_SUPPLY_ATTR_HX](ADV_EVT_SUPPLY_ATTR_HX.md) | `ADVERSE_EVENT_ID` | high |
| [ADV_EVT_SUPPLY_HISTORY](ADV_EVT_SUPPLY_HISTORY.md) | `ADVERSE_EVENT_ID` | high |
| [OR_LOG_LN_ADVEVTS](OR_LOG_LN_ADVEVTS.md) | `ADVERSE_EVENT_ID` | high |
| [PAT_ADVERSE_EVENT](PAT_ADVERSE_EVENT.md) | `ADVERSE_EVENT_ID` | high |

