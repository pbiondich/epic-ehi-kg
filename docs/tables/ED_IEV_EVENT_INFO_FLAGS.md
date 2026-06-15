# ED_IEV_EVENT_INFO_FLAGS

> Holds the Event Value Flags for Events Database (IEV) Events.

**Primary key:** `EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier for the event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this event. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple flags associated with a specific group of data within this record. |
| 4 | `EVENT_FLAGS_C_NAME` | VARCHAR |  | The flags for a value that was added as an ED course comment, such as "abnormal" or "critical" for a lab result value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

