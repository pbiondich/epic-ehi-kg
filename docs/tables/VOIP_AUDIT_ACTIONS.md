# VOIP_AUDIT_ACTIONS

> The audited actions for VoIP call logs.

**Primary key:** `VIDEO_VISIT_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VIDEO_VISIT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the video visit record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VOIP_AUDIT_ACTION_C_NAME` | VARCHAR |  | The single audit action for a VoIP call log. |
| 4 | `PARTICIPANT_GUID` | VARCHAR |  | This item stores the participant GUIDs of each participant connected to the call. |
| 5 | `VOIP_USER_ID` | VARCHAR |  | This item stores the EMP ID associated with the participant in the call. |
| 6 | `VOIP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VOIP_ACTION_INST_DTTM` | DATETIME (UTC) |  | The instant of the audit action. |
| 8 | `DID_NOT_CONN_RSN_C_NAME` | VARCHAR |  | The reason the participant did not connect to the call. |
| 9 | `ADD_BY_PARTICIPANT_GUID` | VARCHAR |  | The participant GUID of the participant that added the participant to the call. |
| 10 | `VOIP_CLIENT_APP_TARGET_C_NAME` | VARCHAR | org | This item stores the Epic application used to make/receive the call for the participant. |
| 11 | `VOIP_PHONE_NUMBER` | VARCHAR |  | The number that was dialed attempting to reach the participant in the call. It can contain keypad characters like * and # in addition to digits. |
| 12 | `AVB_STATUS_C_NAME` | VARCHAR |  | Availability status for VoIP audit actions. |
| 13 | `IS_USER_FORWARDING_YN` | VARCHAR |  | Call forwarding flag for VoIP audit actions. |
| 14 | `ACTION_LOCAL_DTTM` | DATETIME (Attached) |  | The instant of the audit action in local time. |
| 15 | `CALL_RESULT_C_NAME` | VARCHAR |  | Call result for VoIP audit actions. |
| 16 | `PARTICIPANT_TYPE_C_NAME` | VARCHAR |  | The type of connection for participant in the call, such as an Epic device or external phone. |
| 17 | `RESOLVED_PHONE_NUMBER` | VARCHAR |  | The number that was used to route the call to the participant. |
| 18 | `RESOLVED_SIP_ADDRESS` | VARCHAR |  | The SIP address that was used to route the call to the participant. |
| 19 | `VOIP_ADDED_REASON_C_NAME` | VARCHAR |  | Reason why participant of the call was added. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VIDEO_VISIT_ID` | [VOIP_CALL](VOIP_CALL.md) | sole_pk | high |

