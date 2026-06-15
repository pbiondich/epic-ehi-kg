# PT_GOALS_INFO

> This table contains data in the Discrete Goals (IGO) master file that is no-add data.

**Primary key:** `GOAL_ID`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `USER_ID` | VARCHAR | FK→ | The user ID of the person who entered this goal. |
| 3 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `GOAL_TEMPLATE_ID` | NUMERIC | FK→ | Stores the goal template used to create this record |
| 5 | `GOAL_TEMPLATE_ID_GOAL_TEMPLATE_NAME` | VARCHAR |  | The goal template name. |
| 6 | `GOAL_TEMPLATE_DAT` | NUMERIC |  | Stores the Goal Template Contact |
| 7 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient who is associated with this goal. |
| 8 | `CREATE_INST_DTTM` | DATETIME (Local) |  | The instant this goal was created. |
| 9 | `GOAL_USAGE_C_NAME` | VARCHAR |  | Context in which the goal is used. |
| 10 | `REC_VAL_COMPLIAN_YN` | VARCHAR |  | Contains a category value denoting whether or not the most recent compliance value is compliant |
| 11 | `MOST_RECENT_VALUE` | VARCHAR |  | Contains the most recent compliance value for the goal |
| 12 | `RECENT_VALUE_I_DTTM` | DATETIME (Local) |  | The instant that the most recent compliance value was recorded |
| 13 | `REC_VALUE_CHEC_DTTM` | DATETIME (Local) |  | The instant that this goal was checked to determine its most recent compliance value |
| 14 | `AMB_GOAL_TYPE_C_NAME` | VARCHAR | org | Ambulatory goal type category (for example, Blood Pressure, Diet, etc.). |
| 15 | `MYC_CREATE_USER_ID` | VARCHAR |  | Stores the ID of patient account record of the MyChart (Epic Patient Portal) user who created the goal. |
| 16 | `GOAL_STATUS_C_NAME` | VARCHAR |  | The current status of the goal. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `GOAL_TEMPLATE_ID` | [GOAL_TEMPLATES](GOAL_TEMPLATES.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

