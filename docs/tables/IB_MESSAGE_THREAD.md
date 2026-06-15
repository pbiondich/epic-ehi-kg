# IB_MESSAGE_THREAD

> Shows information regarding all messages in an HTH thread.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | Unique message thread ID. A message thread is similar to a conversation in email - it is a series of messages related to the same patient encounter. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `MESSAGE_CID` | NUMERIC |  | In Basket Message (EOW) CID |
| 4 | `MESSAGE_ID` | VARCHAR | FK→ | In Basket Message (EOW) ID |
| 5 | `ROUTING_COMMENT` | VARCHAR |  | Comments attached to the In Basket message being routed. This column will be automatically truncated at 4000 characters. |
| 6 | `ATTACHED_NOTE_ID` | VARCHAR |  | Note attached to the In Basket message being routed. |
| 7 | `SMART_ROUTE_SRC_MSG_ID` | VARCHAR |  | Cross-deployment permanent storage for the source message of a smart routing event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

