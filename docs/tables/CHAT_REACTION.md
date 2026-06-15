# CHAT_REACTION

> Stores chat reactions.

**Primary key:** `CONVERSATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `REACT_MSG_LINE` | INTEGER |  | The line of the message that a reaction corresponds to. |
| 6 | `REACT_TYPE_C_NAME` | VARCHAR |  | The type of reaction to a message. (For example, Heart, Sad, or Angry.) |
| 7 | `REACT_SENDER_USER_ID` | VARCHAR |  | The EMP ID of the user that sent the reaction. |
| 8 | `REACT_SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `REACT_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant the reaction was sent. |
| 10 | `REACT_INST_LOCAL_DTTM` | DATETIME (Local) |  | The local instant the reaction was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

