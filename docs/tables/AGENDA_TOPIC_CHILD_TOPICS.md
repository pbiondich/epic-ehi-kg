# AGENDA_TOPIC_CHILD_TOPICS

> Child topics of the given parent topic.

**Primary key:** `AGENDA_TOPIC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_TOPIC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the topic record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHILD_AGENDA_TOPIC_ID` | NUMERIC |  | This topic's child topics. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENDA_TOPIC_ID` | [AGENDA_TOPIC_INFO](AGENDA_TOPIC_INFO.md) | sole_pk | high |

