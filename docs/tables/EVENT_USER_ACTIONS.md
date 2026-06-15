# EVENT_USER_ACTIONS

> This table contains information on the user actions taken during an event.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ACTIONS` | VARCHAR |  | This column lists the user actions associated with this event. |
| 4 | `USER_ACTION_INFO` | VARCHAR |  | Extra Information about the user's action. |
| 5 | `USER_ACTION_DTTM` | DATETIME (Attached) |  | The time a user's action took place. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

