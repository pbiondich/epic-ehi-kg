# COMM_TRACE_SMS_AWAIT

> Information about the actions to be taken on 2-way SMS messages.

**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `AWAIT_KEYWORD` | VARCHAR |  | Part of the table that contains data about how and what should trigger 2-way application actions from a message. This item contains the keyword for which we are waiting. |
| 5 | `AWAIT_ACTION_C_NAME` | VARCHAR | org | Part of the table that contains data about how and what should trigger 2-way application actions from a message. This item contains the action to be performed by the keyword. We also store the action on the incoming mobile originated (MO) message where the item contains the action to be performed in response to this MO message. |
| 6 | `AWAIT_LPP_ID` | NUMERIC |  | Part of the table that contains data about how and what should trigger 2-way application actions from a message. This item contains the LPP to be used to handle the 2-way action. We also store the LPP on the incoming mobile originated (MO) message where the item contains the LPP to be used to handle the MO message. |
| 7 | `AWAIT_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 8 | `AWAIT_ACTION_SETTING_ID` | NUMERIC |  | Part of the table that contains data about how and what should trigger 2-way application actions. This item contains the settings record for the action to be performed. |
| 9 | `AWAIT_ACTION_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

