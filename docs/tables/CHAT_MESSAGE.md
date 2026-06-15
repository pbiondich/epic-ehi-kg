# CHAT_MESSAGE

> Table containing Secure Chat message info.

**Primary key:** `CONVERSATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `INST_SENT_UTC_DTTM` | DATETIME (UTC) |  | The instant the message was sent. |
| 5 | `MESSAGE_TYPE_C_NAME` | VARCHAR |  | This defines the type of message (for example, a normal message, a user joining the conversation, or a user leaving) |
| 6 | `MESSAGE_PRIORITY_C_NAME` | VARCHAR |  | This item stores the priority for the message |
| 7 | `SENDER_USER_ID` | VARCHAR |  | The ID of the user that sent the message. |
| 8 | `SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `SENDER_MYPT_ID` | VARCHAR |  | The ID of the MyChart user who sent a Secure Chat message. |
| 10 | `PAT_MESSAGE_ID` | VARCHAR |  | The ID of the MyChart message linked to this Secure Chat message. |
| 11 | `DESCRIPTION_SS` | VARCHAR |  | Description of the order or saved work linked to this message |
| 12 | `MESSAGE_IS_EDITED_YN` | VARCHAR |  | Whether the text of this message has been edited or deleted since it was originally sent. |
| 13 | `PRIORITY_CHANGE_REASON_C_NAME` | VARCHAR |  | The priority change reason category ID for the conversation message. |
| 14 | `SENDER_LOGIN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `SENDER_CLIENT_APP_TARGET_C_NAME` | VARCHAR | org | This item contains the type of client application - such as Hyperspace or Haiku - from which this chat message was sent. |
| 16 | `INST_SENT_LOCAL_DTTM` | DATETIME (Local) |  | The local instant the message was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

