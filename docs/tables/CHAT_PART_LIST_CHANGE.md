# CHAT_PART_LIST_CHANGE

> Monitors participant changes in secure chat messages.

**Primary key:** `CONVERSATION_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CHANGED_USER_ID` | VARCHAR |  | This tracks which user joined or left the conversation |
| 5 | `CHANGED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHANGED_BY_USER_ID` | VARCHAR |  | This tracks which user changed another user's status in the conversation |
| 7 | `CHANGED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CHANGE_INSTANT_DTTM` | DATETIME (UTC) |  | This tracks when a participant change happened |
| 9 | `CHANGE_TYPE_5_C_NAME` | VARCHAR |  | This tracks what sort of participant change occurred: a user joined the conversation, a user left the conversation, etc. |
| 10 | `CHANGED_TGR_ID_UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |
| 11 | `CHANGED_BY_ESCALATION_ID` | NUMERIC |  | This contains the ID of the DEX record which changed another user's status in the conversation |
| 12 | `CHANGE_INSTANT_LOCAL_DTTM` | DATETIME (Local) |  | This tracks the local instant when a participant change happened |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

