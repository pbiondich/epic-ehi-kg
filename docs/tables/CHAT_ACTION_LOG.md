# CHAT_ACTION_LOG

> Table containing an audit log of actions taken by users on a Unified Communications conversation. This is how we store a history of certain actions that would otherwise only store their current status, like a user muting a conversation.

**Primary key:** `CONVERSATION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

