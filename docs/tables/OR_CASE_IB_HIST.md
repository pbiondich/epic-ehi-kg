# OR_CASE_IB_HIST

> The OR_CASE_IB_HIST table contains OR management system case In Basket history.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the In Basket history for the case. |
| 3 | `IB_HIST_ACTION_C_NAME` | VARCHAR | org | The category value which indicates the type of action the message serves to notify. |
| 4 | `IB_HIST_SENDER_ID` | VARCHAR |  | The unique ID of the user who sent the message. |
| 5 | `IB_HIST_SENDER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `IB_HIST_RECP_ID` | VARCHAR |  | The unique ID of the user who is the first recipient of the message. |
| 7 | `IB_HIST_RECP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `IB_HIST_DATE` | DATETIME (Local) |  | The date and time the message was sent. |
| 9 | `IB_HIST_SUBJECT` | VARCHAR |  | The subject line of the message. |
| 10 | `IB_HIST_BODY_LINE` | INTEGER |  | The line number where the message body begins in the case record. |
| 11 | `IB_HIST_BODY_LEN` | INTEGER |  | The length of the message body in the case record. |
| 12 | `IB_HIST_RECIP_INI` | VARCHAR |  | The database initials of the recipient registry in the message. |
| 13 | `IB_HIST_MESSAGE_ID` | VARCHAR |  | The message ID of the message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

