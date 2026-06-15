# ESCALATION_EVENTS

> Audit events for the escalation.

**Primary key:** `ESCALATION_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESCALATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_LOCAL_DTTM` | DATETIME (Attached) |  | Instant there was a change event for the escalation. |
| 4 | `CHANGE_LEVEL` | INTEGER |  | Level in the path the change event occurred for the escalation. |
| 5 | `ESC_CHANGE_TYPE_C_NAME` | VARCHAR |  | Change type for the escalation. |
| 6 | `CHANGE_USER_ID` | VARCHAR |  | EMP ID of recipient who changed escalation. |
| 7 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AFFECTED_PROVIDERTEAM_ID` | NUMERIC |  | PCT ID of a provider team affected by an escalation change. |
| 9 | `AFFECTED_PROVIDERTEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 10 | `AFFECTED_CALL_ORDER` | INTEGER |  | The call order of a PCT affected by an escalation event. |
| 11 | `AFF_ROLE_TRTMNT_TEAM_REL_C_NAME` | VARCHAR | org | The role in the role hierarchy of a PCT affected by an escalation event. |
| 12 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | UTC instant there was a change event for the escalation. |
| 13 | `USER_LOGIN_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 14 | `USER_WORKSTATION_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ESCALATION_ID` | [ESCALATION_DYN](ESCALATION_DYN.md) | sole_pk | high |

