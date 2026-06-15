# GOAL_CONTACT

> This table contains contact specific data for the IGO (Discrete Goals) master file.

**Primary key:** `GOAL_ID`, `CONTACT_DATE_REAL`  
**Columns:** 19  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique ID for the goal record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The DTE contact date for the goal record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CP_PRIORITY_C_NAME` | VARCHAR | org | The priority assigned to this goal. |
| 5 | `START_DATE` | DATETIME |  | The date to begin work on this goal. |
| 6 | `END_DATE` | DATETIME |  | The date work on this goal was completed. |
| 7 | `EXP_END_DATE` | DATETIME |  | The date work on this goal is expected to be completed. |
| 8 | `GOAL_OUTCOME_C_NAME` | VARCHAR | org | The outcome(s) associated with a care plan goal. |
| 9 | `EDIT_USER_ID` | VARCHAR |  | This item holds edited user ID information. |
| 10 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `PATH_OUTCOME_VAL_C_NAME` | VARCHAR |  | The category number for the documentation value assigned to this pathway outcome for this contact. |
| 12 | `PATH_OUTCOME_VAR_ID` | VARCHAR |  | The unique ID of the variance that was documented on this pathway outcome for this contact. |
| 13 | `CARE_PLAN_CSN_ID` | NUMERIC |  | Links to the care plan contact. Used to recreate historic versions of the care plan. |
| 14 | `INCLUDE_DESC_YN` | VARCHAR |  | If set to Yes, the goal description will be included on the plan of care. If set to No or left blank, the goal description will be omitted. |
| 15 | `HAS_NOTE_EDIT_YN` | VARCHAR |  | Y means that, for this reading, the default smarttext has been pulled in at least once. |
| 16 | `READING_UTC_DTTM` | DATETIME (UTC) |  | Documents when the original reading contact was documented. Used to order active documentation readings in the order they clinically happened. |
| 17 | `UPDATED_GOAL_ID` | VARCHAR |  | This item links to the new goal ID that was created when this original goal was resolved and updated. |
| 18 | `REASON_FOR_UPDATE` | VARCHAR |  | This item contains the reason as to why this goal was completed and updated. |
| 19 | `WC_PILLAR_C_NAME` | NUMERIC |  | The primary target pillar of a MyChart Care Companion Wellness Companion Goal. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

