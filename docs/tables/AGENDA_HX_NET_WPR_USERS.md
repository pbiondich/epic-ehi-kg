# AGENDA_HX_NET_WPR_USERS

> Contains set of MyChart users involved in edits to the agenda.

**Primary key:** `AGENDA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit agenda record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MYPT_ID` | VARCHAR | shared | Contains the set of all MyChart users which have been involved in some edit to the visit agenda. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENDA_ID` | [AGENDA_INFO](AGENDA_INFO.md) | sole_pk | high |

