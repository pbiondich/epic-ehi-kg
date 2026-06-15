# CHAT_CONVERSATIONS

> Table containing Secure Chat conversation level items.

**Primary key:** `CONVERSATION_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 4 | `LST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant the newest message in the conversation was sent. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient linked to the conversation. |
| 6 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 7 | `INSTANT_OF_UPDATE_DTTM` | DATETIME (Local) |  | Stores the instant the record was last locked/unlocked |
| 8 | `CONVERSATION_TYPE_C_NAME` | VARCHAR |  | The type of the conversation record, which indicates the intended audience of the Secure Chat conversation. A null value indicates the conversation is only between staff members. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the patient encounter associated with this conversation. This item will only be populated for Bedside patient-facing conversations. A value here means the conversation may include a patient or their proxies. |
| 10 | `PAT_CONVERSATION_THREAD_ID` | NUMERIC |  | The ID of the MyChart conversation linked to this Secure Chat conversation. |
| 11 | `CHAT_CONTEXT_TYPE_C_NAME` | VARCHAR |  | Stores the Secure Chat conversation context. |
| 12 | `LINKED_PUSH_NOTIF_ID` | NUMERIC |  | Linked PNN (push notification) record ID to the TLK record that provides additional context about the conversation. |
| 13 | `ORIGINAL_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |
| 14 | `ACTIVE_ESCALATION_ID` | NUMERIC |  | The active Chat Request for the conversation, if applicable. |
| 15 | `CREATED_BY_USER_ID` | VARCHAR |  | Stores the ID of the user that created this conversation. |
| 16 | `CREATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

