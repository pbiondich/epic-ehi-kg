# MYC_CONVO_ABT_CUST_SVC

> Customer service topics associated with the MyChart message conversation.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NCS_TOPIC_C_NAME` | VARCHAR | org | Contains the category value of the customer service topic associated with the conversation |
| 4 | `TOPIC_DISPLAY_NAME` | VARCHAR |  | Contains the name of the customer service topic that was presented to the user that started the conversation. Note that not all customer service topics are presented to the user. Some contexts are hard-coded by the workflow that generates the message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

