# RX_DEFERRAL_HISTORY

> This table stores the deferrals that pharmacists have created when reviewing scoring system rules. Each row is a deferral.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | The unique identifier for the intervention record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEFERRAL_ISACTIVE_YN` | VARCHAR |  | Indicates whether the current line is an active deferral for this deferral record. 'Y' indicates that the deferral is active. ('N' or NULL) indicates the deferral is not active. |
| 4 | `DEFERRAL_ORDER_ID` | NUMERIC |  | The unique ID of the order record that is being deferred. The rule isn't triggered for this order, but other orders still trigger the rule. |
| 5 | `DEFERRAL_USER_ID` | VARCHAR |  | The unique ID associated with the user record for the user who created the deferral. |
| 6 | `DEFERRAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `DEFERRAL_START_DTTM` | DATETIME (UTC) |  | The date and time when the deferral was created. |
| 8 | `DEFFERAL_END_DTTM` | DATETIME (UTC) |  | The date and time when the deferral record will end or was scheduled to end if the deferral is no longer active. |
| 9 | `SCORE_DEFERRED_NUM` | INTEGER |  | The score of the rule at the time of deferral. |
| 10 | `DEFERRAL_REASON_C_NAME` | VARCHAR | org | The deferral reason category ID for the deferral record. |
| 11 | `DEFERRAL_COMMENT` | VARCHAR |  | The comments associated with the deferral. |
| 12 | `MINUTES_SPENT_NUM` | INTEGER |  | The amount of time a user spent on an individual deferral. |
| 13 | `FUTURE_WARNING_YN` | VARCHAR |  | Indicates whether the deferral will be cleared if an associated rule or order is updated. |
| 14 | `CLEARED_REASON_C_NAME` | VARCHAR |  | The deferral cleared reason category ID for the deferral record. |
| 15 | `CLEARED_DTTM` | DATETIME (UTC) |  | The date and time when the deferral record was cleared. |
| 16 | `CLEARED_SCORE_NUM` | INTEGER |  | The score of the rule when the deferral was cleared. This item is only populated if the deferral was cleared because the score changed. |
| 17 | `CLEARED_BY_USER_ID` | VARCHAR |  | The unique ID associated with the user record for the user who cleared the deferral. |
| 18 | `CLEARED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `CLEARED_COMMENT` | VARCHAR |  | Comment for the reason that a deferral was cleared. This item gets automatically updated by code when a deferral is cleared. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

