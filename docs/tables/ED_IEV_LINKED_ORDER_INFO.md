# ED_IEV_LINKED_ORDER_INFO

> This table extracts the link between orders and events. An event can have multiple orders linked in this table. This table can be used to link to other orders tables with the order ID.

**Primary key:** `EVENT_ID`, `EVENT_LINE`, `ORDER_LINK_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier for the event record. |
| 2 | `EVENT_LINE` | INTEGER | PK | The line number for the event associated with this record. |
| 3 | `ORDER_LINK_LINE` | INTEGER | PK | Events may be triggered by multiple orders and when this occurs, each order is stored on its own line. This column stores the line number associated with each order that triggered the event. |
| 4 | `EVENT_LINKED_ORD_ID` | NUMERIC |  | Stores the order IDs linked to this event line indicating the orders that triggered the event |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

