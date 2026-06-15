# OR_CASE_AUDIT_TRL

> The OR_CASE_AUDIT_TRL table contains OR management system case audit trail information.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the audit information for the case. |
| 3 | `AUDIT_RESCHED_TO_DT` | DATETIME |  | This column stores the next scheduled date for the case if the rescheduling action took place. The rescheduling action includes the actions of moved, removed, and bumped. |
| 4 | `AUDIT_ADD_ON_SCH_YN` | VARCHAR |  | Indicates whether this case was added on after the schedule was finalized, as defined by settings in Location or System Definitions (not the add-on checkbox in the case). Y is returned if the case is an add-on and the actions are canceled, scheduled, or rescheduled. N is returned if the case is not an add-on and the actions are canceled, scheduled, or rescheduled. Null is returned if the action on the case is not canceled, scheduled, or rescheduled. |
| 5 | `AUDIT_INCLUDE_ORG_CANC_RPT_YN` | VARCHAR |  | Indicates whether the case audit action is included in organizational cancellations reporting based on room, service, holiday, weekend, and add-on exclusions defined in System or Location Definitions. Y indicates that the case is included in cancellations reporting. N indicates that the case is not included in cancellations reporting. This column is only populated if the action is 'canceled', 'scheduled', 'moved', 'swapped OR', 'removed', or 'bumped'. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

