# CAL_CHAT_ASGN_HX

> The CAL_CHAT_ASGN_HX table contains information about the history of a live chat. This table tracks what agent was assigned to a chat and what queue was assigned to a chat. This table also contains data on who updated the chat assignment and when it was updated.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHAT_HX_REASON_C_NAME` | VARCHAR | org | The reason for changing the assignment or queue of a chat. Categories that are below 500 will automatically be set by system in certain automated workflows that change the chat history. Users will only have the ability to select category that have an ID 500 or above. |
| 4 | `CHAT_HX_CMT` | VARCHAR |  | Comments on the change of chat history that will be shown to future users reviewing the chat history. The comment is left by the user changing the chat assignment. The comment will be the message to the next agent if the change was done during the transfer workflow. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

