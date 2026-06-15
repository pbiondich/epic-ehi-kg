# VARIANCE

> This table contains data on variance (IVR) records associated with a patient.

**Primary key:** `VARIANCE_ID`  
**Columns:** 17  
**Org-specific columns:** 1  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANCE_ID` | VARCHAR | PK | The unique ID for the variance record. |
| 2 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user creating this record. |
| 3 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `USER_DISC_TYPE_ID` | VARCHAR |  | The unique ID of the discipline of the user creating this variance record. |
| 5 | `USER_DISC_TYPE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 6 | `CREATED_TIME` | DATETIME (Local) |  | The instant this variance record was created. |
| 7 | `CSN` | NUMERIC |  | The patient contact serial number for this variance. |
| 8 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `VARIANCE_TYPE_ID` | VARCHAR | FK→ | The unique ID for the variance type associated with this record. |
| 10 | `VARIANCE_TYPE_ID_VARIANCE_NAME` | VARCHAR |  | The name of the variance type record. |
| 11 | `VAR_CAT_C_NAME` | VARCHAR | org | The category assigned to this variance record. |
| 12 | `GOAL_ID` | VARCHAR | FK→ | The unique ID of the goal associated with this variance record. |
| 13 | `GOAL_TYPE_ID` | VARCHAR | FK→ | The unique ID of the goal type associated with this variance record. |
| 14 | `GOAL_TYPE_ID_GOAL_NAME` | VARCHAR |  | The name of the goal type record. |
| 15 | `INTERVENTION_ID` | VARCHAR | FK→ | The unique ID of the intervention associated with this variance record. |
| 16 | `INTRVNTN_TYPE_ID_INTRVNTN_TYPE_NAME` | VARCHAR |  | The name of the intervention type. |
| 17 | `DISPLAY_NAME` | VARCHAR |  | The display name for this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `GOAL_TYPE_ID` | [GOAL_TYPE](GOAL_TYPE.md) | sole_pk | high |
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |
| `VARIANCE_TYPE_ID` | [VARIANCE_TYPE](VARIANCE_TYPE.md) | sole_pk | high |

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [GOAL_VARIANCE](GOAL_VARIANCE.md) | `VARIANCE_ID` | high |
| [HH_INTVTN_VARIANCE](HH_INTVTN_VARIANCE.md) | `VARIANCE_ID` | high |
| [IVR_WEBLINKS](IVR_WEBLINKS.md) | `VARIANCE_ID` | high |
| [VARIANCE_COMMENT](VARIANCE_COMMENT.md) | `VARIANCE_ID` | high |
| [VARIANCE_READING_HX](VARIANCE_READING_HX.md) | `VARIANCE_ID` | high |
| [VAR_CONTACT](VAR_CONTACT.md) | `VARIANCE_ID` | high |

