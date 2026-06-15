# CHAT_MESSAGE_EDITS

> Audit history of messages that have been edited or deleted. Each line stores the time of an edit and the previous text.

**Primary key:** `CONVERSATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MESSAGE_EDIT_LINE` | INTEGER |  | The message line number from I TLK 3000 that has been edited. Other items in this row of the related group describe an edit to the indicated message. |
| 6 | `MSG_EDIT_PREV_TEXT` | VARCHAR |  | Stores the previous value of the message text after it was edited or deleted to keep an audit history. |
| 7 | `MSG_EDITED_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The time at which the edit or delete of the message text occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

