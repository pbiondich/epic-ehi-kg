# TOPIC_HX_NET_TOPICS

> Contains set of topics involved in edits to the agenda.

**Primary key:** `AGENDA_TOPIC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_TOPIC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit agenda topic record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NET_AGENDA_TOPIC_ID` | NUMERIC |  | Contains the set of all topics which have been involved in some edit to the visit agenda topic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENDA_TOPIC_ID` | [AGENDA_TOPIC_INFO](AGENDA_TOPIC_INFO.md) | sole_pk | high |

