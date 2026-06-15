# ESC_RESPONSIBLE_USERS

> Status of all responsible groups and users.

**Primary key:** `ESCALATION_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESCALATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ID` | VARCHAR | FK→ | The IDs of the users responsible for the escalation |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |
| 6 | `UPDATE_LOCAL_DTTM` | DATETIME (Attached) |  | Instant of responsible users change. |
| 7 | `RESP_USER_STATUS_C_NAME` | VARCHAR |  | Instant there was a change event for the escalation. |
| 8 | `PROVIDERTEAM_ID` | NUMERIC |  | The PCT IDs of the responsible provider teams |
| 9 | `PROVIDERTEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 10 | `CALL_ORDER` | INTEGER |  | The most recently attempted call order for the provider team |
| 11 | `ROLE_TRTMNT_TEAM_REL_C_NAME` | VARCHAR | org | The most recently attempted role for the provider team |
| 12 | `RESPONSIBLE_REASON_C_NAME` | VARCHAR |  | The reason that the user is listed as responsible for the request. |
| 13 | `REASON_USER_ID` | VARCHAR |  | Contains the EMP ID of the user who caused this user to be listed as responsible |
| 14 | `REASON_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `REASON_PROVIDERTEAM_ID` | NUMERIC |  | Contains the PCT ID of the On-Call team this user is a member of that caused them to become responsible |
| 16 | `REASON_PROVIDERTEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 17 | `REASON_ROLE_TRTMNT_TEAM_REL_C_NAME` | VARCHAR |  | Contains the responsible user's role |
| 18 | `REASON_UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ESCALATION_ID` | [ESCALATION_DYN](ESCALATION_DYN.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

