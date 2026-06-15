# CHAT_PARTICIPATING_GROUPS

> Table with Unified Communication groups in chat conversation.

**Primary key:** `CONVERSATION_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |
| 4 | `GROUP_ACTIVE_C_NAME` | VARCHAR |  | This indicates if the group is considered active in the conversation or not |
| 5 | `GROUP_SYNC_DTTM` | DATETIME (UTC) |  | This item stores the last time a group's members were synchronized with the conversation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

