# MYC_CONVO_ABT_MED_ADVICE

> Medical advice topic associated with the MyChart message conversation.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MED_ADV_TOPIC_C_NAME` | VARCHAR | org | Contains the category value of the medical advice topic that was selected for this conversation. Note that not all medical advice messages may have this data. |
| 4 | `TOPIC_DISPLAY_NAME` | VARCHAR |  | Contains the name of the topic that was presented to the user when the conversation was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

