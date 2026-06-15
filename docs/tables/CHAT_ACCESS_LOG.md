# CHAT_ACCESS_LOG

> Table containing log of when Secure Chat was accessed.

**Primary key:** `CONVERSATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `READER_USER_ID` | VARCHAR |  | The user ID of the user that read the message. |
| 5 | `READER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ACCESSED_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant the participant read the message. |
| 7 | `ACCESSED_MSG_LN` | INTEGER |  | The line of the message that was read. |
| 8 | `READER_MYPT_ID` | VARCHAR |  | The ID of the MyChart user that read the message. |
| 9 | `ACCESSED_INST_LOCAL_DTTM` | DATETIME (Local) |  | The local instant the participant read the message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

