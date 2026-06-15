# CHAT_PARTICIPANT_GROUPS

> Table for Unified Communication groups in a conversation that a chat user is a part of. To extract data to CHAT_PARTICIPANT_GROUPS: 1. In Clinical Administration, open EMR System Definitions and select Note, Trans, Communication. 2. Go to the Secure Chat Clarity Settings screen. 3. In the Enable Clarity extraction for Secure Chat conversations field, enter 1-Yes.

**Primary key:** `CONVERSATION_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `USER_IN_UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

